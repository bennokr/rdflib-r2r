import logging
import re
import urllib.parse
from dataclasses import dataclass
import base64
import datetime
import parse
from string import Formatter

from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, Namespace

from sqlalchemy import text, table, literal_column
from sqlalchemy import types as sqltypes, func as sqlfunc
from sqlalchemy import or_ as sql_or, and_ as sql_and
from sqlalchemy.sql.schema import Column, Table

from rdflib_r2r.sql_view import view2obj

rr = Namespace("http://www.w3.org/ns/r2rml#")


def iri_safe(v):
    return urllib.parse.quote(v, safe="")


def iri_unsafe(v):
    return urllib.parse.unquote(v)


def _get_table(graph, tmap, meta=None):
    logtable = graph.value(tmap, rr.logicalTable)
    if graph.value(logtable, rr.tableName):
        tname = graph.value(logtable, rr.tableName).toPython()
        dbtable = table(tname.strip('"'))
        if meta is not None:
            dbtable = meta.tables.get(dbtable.name, dbtable)
            if isinstance(dbtable, Table):
                dbtable.append_column(Column("rowid", sqltypes.Integer))
            dbtable = dbtable.alias()
        return dbtable
    else:
        tname = f'"View_{base64.b32encode(str(tmap).encode()).decode()}"'
        sqlquery = graph.value(logtable, rr.sqlQuery).strip().strip(";")

        # parse views to SQLAlchemy objects to get column types
        cols = view2obj(sqlquery)

        return text(sqlquery).columns(*cols).subquery(tname.strip('"'))

def _get_col(dbtable, colname, template=False):
    colname = colname.strip('"')

    if hasattr(dbtable, 'c') and dbtable.c and (colname in dbtable.c):
        dbcol = dbtable.c[colname]

        if isinstance(dbcol.type, sqltypes.Numeric):
            if dbcol.type.precision:
                if template:
                    # Binary data
                    return sqlfunc.hex(dbcol)
                else:
                    return dbcol

        if (not template) and isinstance(dbcol.type, sqltypes.CHAR):
            if dbcol.type.length:
                l = dbcol.type.length
                return sqlfunc.substr(dbcol + " " * l, 1, l)

        return dbcol
    else:
        tname = getattr(dbtable, 'original', dbtable).name
        logging.warn(f"Getting column {colname} of {dbtable.__repr__()}")
        return literal_column(f'"{tname}"."{colname}"')

class R2RMapping:
    graph = None
    baseuri = None

    @dataclass(eq=True, order=True, frozen=True)
    class Matcher:
        t: str
        const: str = None
        field: str = None
        parser: str = None
        inverse: str = None

    @classmethod
    def from_db(cls, db, baseuri="http://example.com/base/"):
        """Create RDB2RDF Direct Mapping

        See also: https://www.w3.org/TR/rdb-direct-mapping/

        Args:
            db (sqlalchemy.Engine): Database
            baseuri (str, optional): Base URI. Defaults to "http://example.com/base/".

        Returns:
            R2RMapping
        """
        base = Namespace(baseuri)
        mg = Graph(base=baseuri)

        with db.connect() as conn:
            tmaps = {}
            for tablename in db.dialect.get_table_names(conn, schema="main"):
                tmap = tmaps.setdefault(tablename, BNode())
                mg.add([tmap, RDF.type, rr.TriplesMap])
                logtable = BNode()
                mg.add([tmap, rr.logicalTable, logtable])
                mg.add([logtable, rr.tableName, Literal(f'"{tablename}"')])

                s_map = BNode()
                mg.add([tmap, rr.subjectMap, s_map])
                mg.add([s_map, rr["class"], base[iri_safe(tablename)]])

                # TEMPORARY: duckdb hack
                pk = db.dialect.get_pk_constraint(conn, tablename, schema="main")
                if pk and any(pk.values()):
                    primary_keys = pk["constrained_columns"] or eval(
                        pk["name"].partition("KEY")[-1]
                    )
                    if not (type(primary_keys) in [tuple, list]):
                        primary_keys = (primary_keys,)
                else:
                    primary_keys = []

                if primary_keys:
                    parts = ['%s={"%s"}' % (iri_safe(c), c) for c in primary_keys]
                    template = iri_safe(tablename) + "/" + ";".join(parts)
                    mg.add([s_map, rr.template, Literal(template)])
                    mg.add([s_map, rr.termType, rr.IRI])
                else:
                    mg.add([s_map, rr.termType, rr.BlankNode])

                for column in db.dialect.get_columns(conn, tablename, schema="main"):
                    colname = column["name"]
                    coltype = column["type"]
                    # Add a predicate-object map per column
                    pomap = BNode()
                    mg.add([tmap, rr.predicateObjectMap, pomap])
                    pname = f"{iri_safe(tablename)}#{iri_safe(colname)}"
                    mg.add([pomap, rr.predicate, base[pname]])

                    o_map = BNode()
                    mg.add([pomap, rr.objectMap, o_map])
                    mg.add([o_map, rr.column, Literal(f'"{colname}"')])
                    if isinstance(coltype, sqltypes.Integer):
                        mg.add([o_map, rr.datatype, XSD.integer])

                foreign_keys = db.dialect.get_foreign_keys(
                    conn, tablename, schema="main"
                )
                for fk in foreign_keys:
                    # Add another predicate-object map for every foreign key
                    pomap = BNode()
                    mg.add([tmap, rr.predicateObjectMap, pomap])
                    parts = [iri_safe(part) for part in fk["constrained_columns"]]
                    pname = f"{iri_safe(tablename)}#ref-{';'.join(parts)}"
                    mg.add([pomap, rr.predicate, base[pname]])

                    o_map = BNode()
                    mg.add([pomap, rr.objectMap, o_map])
                    reftable = fk["referred_table"]
                    refmap = tmaps.setdefault(reftable, BNode())
                    mg.add([o_map, rr.parentTriplesMap, refmap])

                    colpairs = zip(fk["constrained_columns"], fk["referred_columns"])
                    for colname, refcol in colpairs:
                        join = BNode()
                        mg.add([o_map, rr.joinCondition, join])
                        mg.add([join, rr.child, Literal(f'"{colname}"')])
                        mg.add([join, rr.parent, Literal(f'"{refcol}"')])

        logging.warn("\n" + mg.serialize(format="turtle").decode())
        return cls(mg, baseuri=baseuri)

    @classmethod
    def _template_to_parser(cls, template, irisafe=None):
        # TODO: iri safe?
        # escape curly braces by doubling {{ }}
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)
        template = re.sub('{"', "{", template)
        template = re.sub('"}', "}", template)
        # Replace space by double underscore...
        template = re.sub(
            "{([^{}]+)}", lambda x: x.group(0).replace(" ", "__"), template
        )
        return template

    @classmethod
    def _term_pat(cls, graph, dbtable, parent, mapper, shortcut, obj=False):
        """Get pattern matchers based on term mappings

        Args:
            graph: Mapping graph
            parent: Parent mapping
            shortcut: Shortcut property
            mapper: Mapper property
            obj (bool, optional): Whether this is an object mapping. Defaults to False.

        Yields:
            R2RMapping.Matcher: Node n3 pattern
        """
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
                yield cls.Matcher(const=const.toPython(), t=dbtable)
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield cls.Matcher(const=const.toPython(), t=dbtable)
                else:
                    # Inverse Expression
                    inverse = None
                    for inv_exp in graph[tmap : rr.inverseExpression]:
                        inverse = cls._template_to_parser(inv_exp)

                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        col = graph.value(tmap, rr.column)
                        col = re.sub('(^"|"$)', "", col)
                        yield cls.Matcher(field=col, inverse=inverse, t=dbtable)
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        parser = cls._template_to_parser(
                            template, irisafe=(termtype == rr.IRI)
                        )
                        yield cls.Matcher(parser=parser, inverse=inverse, t=dbtable)
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        rt = _get_table(graph, ref)
                        rs = cls._term_pat(graph, rt, ref, rr.subjectMap, rr.subject)
                        yield from rs
                    else:
                        t = getattr(dbtable, "original", dbtable).name
                        parser = cls._template_to_parser(f"{t}#{{rowid}}")
                        yield cls.Matcher(parser=parser, inverse=inverse, t=dbtable)

    def __init__(self, g, baseuri="http://example.com/base/"):
        self.graph = g
        self.baseuri = baseuri

        # Track triple maps per node pattern matcher
        self.spat_tmaps, self.ppat_pomaps, self.opat_pomaps = {}, {}, {}
        for tmap in g[: RDF.type : rr.TriplesMap]:
            t = _get_table(g, tmap)
            for s_pat in self._term_pat(g, t, tmap, rr.subjectMap, rr.subject):
                self.spat_tmaps.setdefault(s_pat, []).append(tmap)
            for po_i, pomap in enumerate(g[tmap : rr.predicateObjectMap :]):
                for p_pat in self._term_pat(g, t, pomap, rr.predicateMap, rr.predicate):
                    self.ppat_pomaps.setdefault(p_pat, []).append(pomap)
                for o_pat in self._term_pat(g, t, pomap, rr.objectMap, rr.object, True):
                    self.opat_pomaps.setdefault(o_pat, []).append(pomap)

    def inverse_condition(self, inverse_expr, field_values):
        col_replace = {
            col: f'"{col}"'
            for _, col, _, _ in Formatter().parse(inverse_expr)
            if (col != None) and (col not in field_values)
        }
        param_replace = {field: ":" + field for field in field_values}
        t = text(inverse_expr.format(**col_replace, **param_replace))
        return t.bindparams(**field_values)

    def get_filters(self, node, dbtable, pat_maps):

        # A pattern may be used in multiple places, so use sql_or
        # (but what happens if the table name is out of scope ...? )
        map_conditions = {}
        if node is not None:
            for pat, maps in pat_maps.items():
                if pat.const:
                    if node.toPython() == pat.const:
                        for m in maps:
                            # No condition, select all
                            map_conditions.setdefault(m, []).append(True)
                elif pat.field:
                    val = node.toPython()
                    if isinstance(val, str):
                        # not super sure of this:
                        val = iri_unsafe(val).replace(self.baseuri, "").strip()
                    elif isinstance(val, datetime.date):
                        val = str(val)
                    elif isinstance(val, bytes):
                        val = text(f"x'{base64.b16encode(val).decode()}'")

                    if pat.inverse:
                        fields = {pat.field: val}
                        where = self.inverse_condition(pat.inverse, fields)
                    else:
                        key = dbtable.c[pat.field]
                        where = key == val
                    for m in maps:
                        if not (where is True):
                            map_conditions.setdefault(m, []).append(where)
                elif pat.parser:
                    parser = parse.compile(pat.parser)
                    val = str(node.toPython()).replace(self.baseuri, "").strip()

                    if parser.parse(val):
                        fields = parser.parse(val).named
                        if pat.inverse:
                            where = self.inverse_condition(pat.inverse, fields)
                        else:
                            # A template pattern may have multiple fields;
                            #   all must match, so use sql_and
                            where_clauses = []
                            for key, val in fields.items():
                                key = dbtable.c[key.replace("__", " ")]
                                if pat.parser.startswith("data:"):
                                    val = text(f"x'{val}'")
                                else:
                                    val = iri_unsafe(val)
                                clause = key == val
                                where_clauses.append(clause)
                            where = sql_and(*where_clauses) if where_clauses else True
                        for m in maps:
                            if not (where is True):
                                map_conditions.setdefault(m, []).append(where)
            return {
                m: ([sql_or(*wheres)] if wheres and (wheres != [True]) else [])
                for m, wheres in map_conditions.items()
            }
        else:
            return {None: []}
