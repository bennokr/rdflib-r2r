"""
rdflib_r2r.r2r_store
=======================
"""
from os import linesep
from typing import Iterable
import logging
import functools
import operator
import base64
import urllib.parse
import re
from string import Formatter
from dataclasses import dataclass
import datetime

import parse
from rdflib import Graph, URIRef, Literal, BNode, Variable
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

import sqlalchemy
from sqlalchemy import MetaData, select, text, null, literal_column, literal
from sqlalchemy import union_all, or_ as sql_or, and_ as sql_and
from sqlalchemy import schema as sqlschema, types as sqltypes, func as sqlfunc
from sqlalchemy.sql.expression import Operators as SQLOperators

from sqlalchemy.engine import Engine

from rdflib_r2r.types import Any, Optional, Triple, NamedTuple
from rdflib_r2r.sql_view import view2obj

rr = Namespace("http://www.w3.org/ns/r2rml#")


def iri_safe(v):
    return urllib.parse.quote(v, safe="")


def iri_unsafe(v):
    return urllib.parse.unquote(v)

def sql_safe(literal):
    # return "<ENCODE>" + sqlfunc.cast(literal, sqltypes.VARCHAR) + "</ENCODE>"
    # This is a terrible idea due to the large number of chars.
    # ... but the alternative messes up SPARQL query rewriting
    literal = sqlfunc.replace(literal, " ", "%20")
    literal = sqlfunc.replace(literal, "/", "%2F")
    literal = sqlfunc.replace(literal, "(", "%28")
    literal = sqlfunc.replace(literal, ")", "%29")
    literal = sqlfunc.replace(literal, ",", "%2C")
    literal = sqlfunc.replace(literal, ":", "%3A")
    return literal
    

def _get_table(graph, tmap):
    logtable = graph.value(tmap, rr.logicalTable)
    if graph.value(logtable, rr.tableName):
        tname = graph.value(logtable, rr.tableName).toPython()
        return text(tname), tname
    else:
        tname = f'"View_{base64.b32encode(str(tmap).encode()).decode()}"'
        sqlquery = graph.value(logtable, rr.sqlQuery).strip().strip(";")

        view2obj(sqlquery)

        return text(f"({sqlquery}) AS {tname}"), tname


class R2RMapping:
    graph = None
    baseuri = None

    @dataclass(eq=True, order=True, frozen=True)
    class Matcher:
        tname: str
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
    def _term_pat(cls, graph, tname, parent, mapper, shortcut, obj=False):
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
                yield cls.Matcher(const=const.toPython(), tname=tname)
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield cls.Matcher(const=const.toPython(), tname=tname)
                else:
                    # Inverse Expression
                    inverse = None
                    for inv_exp in graph[tmap : rr.inverseExpression]:
                        inverse = cls._template_to_parser(inv_exp)

                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        col = graph.value(tmap, rr.column)
                        col = re.sub('(^"|"$)', "", col)
                        yield cls.Matcher(field=col, inverse=inverse, tname=tname)
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        parser = cls._template_to_parser(
                            template, irisafe=(termtype == rr.IRI)
                        )
                        yield cls.Matcher(parser=parser, inverse=inverse, tname=tname)
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        _, rt = _get_table(graph, ref)
                        rs = cls._term_pat(graph, rt, ref, rr.subjectMap, rr.subject)
                        yield from rs
                    else:
                        t = tname.strip('"')
                        parser = cls._template_to_parser(f"{t}#{{rowid}}")
                        yield cls.Matcher(parser=parser, inverse=inverse, tname=tname)

    def __init__(self, g, baseuri="http://example.com/base/"):
        self.graph = g
        self.baseuri = baseuri

        self.spat_tmaps, self.ppat_pomaps, self.opat_pomaps = {}, {}, {}
        for tmap in g[: RDF.type : rr.TriplesMap]:
            _, t = _get_table(g, tmap)
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

    def get_node_filter(self, node, pat_maps):
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
                        where = literal_column(f'{pat.tname}."{pat.field}"') == val
                    for m in maps:
                        map_conditions.setdefault(m, []).append(where)
                elif pat.parser:
                    parser = parse.compile(pat.parser)
                    val = str(node.toPython()).replace(self.baseuri, "").strip()

                    if parser.parse(val):
                        fields = parser.parse(val).named
                        if pat.inverse:
                            where = self.inverse_condition(pat.inverse, fields)
                        else:
                            where_clauses = []
                            for key, val in fields.items():
                                key = f'{pat.tname}."{key.replace("__", " ")}"'
                                if pat.parser.startswith("data:"):
                                    val = text(f"x'{val}'")
                                else:
                                    val = iri_unsafe(val)
                                clause = literal_column(key) == val
                                where_clauses.append(clause)

                            where = sql_and(*where_clauses)
                        for m in maps:
                            map_conditions.setdefault(m, []).append(where)
            return {m: [sql_or(*wheres)] for m, wheres in map_conditions.items()}
        else:
            return {None: []}


class R2RStore(Store):
    """
    Args:
      - db: SQLAlchemy engine.
    """

    def __init__(
        self,
        db: Engine,
        mapping: Optional[R2RMapping] = None,
        base: str = "http://example.com/base/",
        configuration=None,
        identifier=None,
    ):
        super(R2RStore, self).__init__(
            configuration=configuration, identifier=identifier
        )
        self.db = db
        self.mapping = mapping or R2RMapping.from_db(db)
        self.base = base
        assert self.db
        assert self.mapping

    def __len__(self) -> int:
        """The number of RDF triples in the DB mapping."""
        raise NotImplementedError

    @property
    def nb_subjects(self) -> int:
        """The number of subjects in the DB mapping."""
        raise NotImplementedError

    @property
    def nb_predicates(self) -> int:
        """The number of predicates in the DB mapping."""
        raise NotImplementedError

    @property
    def nb_objects(self) -> int:
        """The number of objects in the DB mapping."""
        raise NotImplementedError

    @property
    def nb_shared(self) -> int:
        """The number of shared subject-object in the DB mapping."""
        raise NotImplementedError

    @staticmethod
    def _get_col(dbtable, tname, col, template=False):
        if type(dbtable) is sqlschema.Table:
            dbcol = dbtable.c[col.strip('"')]

            if isinstance(dbcol.type, sqltypes.Numeric):
                if dbcol.type.precision:
                    if template:
                        return sqlfunc.hex(dbcol)
                    else:
                        return literal_column(f"{tname}.{col}")

            if (not template) and isinstance(dbcol.type, sqltypes.CHAR):
                if dbcol.type.length:
                    l = dbcol.type.length
                    return sqlfunc.substr(dbcol + " " * l, 1, l)

            return dbcol
        else:
            return literal_column(f"{tname}.{col}")


    @classmethod
    def _template_to_function(cls, dbtable, tname, template, irisafe=False):
        # make python format string: escape curly braces by doubling {{ }}
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)

        parts = []
        for prefix, col, _, _ in Formatter().parse(template):
            parts.append(prefix)
            if col:
                c = cls._get_col(dbtable, tname, col, template=True)
                if irisafe:
                    c = sql_safe(c)
                parts.append(c)
        parts = [sqlfunc.cast(x, sqltypes.VARCHAR) for x in parts if x != ""]
        return functools.reduce(operator.add, parts)

    @classmethod
    def _term_map(cls, graph, tname, dbtable, parent, mapper, shortcut, obj=False):
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent : shortcut]:
                yield literal_column("'%s'" % const.n3())
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield literal_column("'%s'" % const.n3())
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        col = graph.value(tmap, rr.column)
                        func = cls._get_col(dbtable, tname, col)
                        if obj:
                            # for objects, the default term type is Literal
                            termtype = graph.value(tmap, rr.termType) or rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        func = cls._template_to_function(
                            dbtable, tname, template, irisafe=(termtype == rr.IRI)
                        )
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        ptable, pname = _get_table(graph, ref)
                        wheres = []
                        for join in graph[tmap : rr.joinCondition]:
                            ccol = f"{tname}.{graph.value(join, rr.child)}"
                            pcol = f"{pname}.{graph.value(join, rr.parent)}"
                            wheres.append(literal_column(ccol) == literal_column(pcol))
                        rs = cls._term_map(
                            graph, pname, ptable, ref, rr.subjectMap, rr.subject
                        )
                        for func in rs:
                            yield select(func).select_from(ptable).where(*wheres)
                        continue
                    else:
                        # TODO: replace with RDB-specific construct (postgresql?)
                        rowid = literal_column(f"{tname}.rowid").cast(sqltypes.VARCHAR)
                        yield ("_:" + tname.strip('"') + "#" + rowid)
                        continue

                    if termtype == rr.IRI:
                        yield "<" + func + ">"
                    elif termtype == rr.BlankNode:
                        yield "_:" + func
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            func = sqlfunc.cast(func, sqltypes.VARCHAR)
                            yield literal('"') + func + '"@' + str(lang)
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            func = sqlfunc.cast(func, sqltypes.VARCHAR)
                            yield literal('"') + func + '"^^' + dtype.n3()
                        else:
                            # keep original datatype
                            yield func
                    else:
                        yield literal_column("'_:'")

    def _triplesmap_select(self, metadata, tmap, pattern):
        mg = self.mapping.graph

        dbtable, tname = _get_table(mg, tmap)
        if metadata:
            dbtable = metadata.tables.get(tname.strip('"'), dbtable)

        qs, qp, qo = pattern
        sfilt = self.mapping.get_node_filter(qs, self.mapping.spat_tmaps)
        pfilt = self.mapping.get_node_filter(qp, self.mapping.ppat_pomaps)
        ofilt = self.mapping.get_node_filter(qo, self.mapping.opat_pomaps)

        swhere = []
        if not (None in sfilt):
            if not (tmap in sfilt):
                return
            else:
                swhere = sfilt[tmap]

        ss = self._term_map(mg, tname, dbtable, tmap, rr.subjectMap, rr.subject)
        s = next(ss).label("s")

        s_map = mg.value(tmap, rr.subjectMap)
        gs = list(self._term_map(mg, tname, dbtable, s_map, rr.graphMap, rr.graph))

        # Class Map
        if (not pfilt) or (None in pfilt) or (RDF.type == qp):
            for c in mg[s_map : rr["class"]]:
                p = literal_column("'%s'" % RDF.type.n3()).label("p")
                o = literal_column("'%s'" % c.n3()).label("o")
                # no unsafe IRI because it should be defined to be safe
                if (qo is not None) and (qo != c):
                    continue
                for g in list(gs) or [null()]:
                    yield (s, p, o, g.label("g")), dbtable, swhere

        # Select Predicate-Object Maps
        pomaps = set(mg[tmap : rr.predicateObjectMap :])
        if not (None in pfilt):
            pomaps &= set(pfilt)
        if not (None in ofilt):
            pomaps &= set(ofilt)

        for pomap in pomaps:
            ps = list(
                self._term_map(
                    mg, tname, dbtable, pomap, rr.predicateMap, rr.predicate
                )
            )
            os = list(
                self._term_map(
                    mg, tname, dbtable, pomap, rr.objectMap, rr.object, True
                )
            )
            gs = list(
                self._term_map(mg, tname, dbtable, pomap, rr.graphMap, rr.graph)
            )
            for p in ps:
                pwhere = pfilt.get(pomap) or []
                if (qp is not None) and p.is_literal and str(p)[1:-1] != qp.n3():
                    # Filter out non-identical property patterns
                    continue
                p = p.label("p")
                for o in os:
                    owhere = ofilt.get(pomap) or []
                    if isinstance(o, sqlalchemy.sql.selectable.Select):
                        # referencing object map condition
                        o = o.where(*owhere)
                        owhere = []
                    o = o.label("o")
                    for g in list(gs) or [null()]:
                        where = swhere + pwhere + owhere
                        yield (s, p, o, g.label("g")), dbtable, where

    def queryPattern(self, metadata, pattern):
        queries = []
        # Triple Maps
        for tmap in self.mapping.graph[: RDF.type : rr.TriplesMap]:
            selects = self._triplesmap_select(metadata, tmap, pattern)
            for spog, dbtable, where in selects:

                query = select(*spog).select_from(dbtable).where(*where)
                queries.append(query)
                
        return union_all(*queries)

    def queryBGP(self, conn, bgp):
        metadata = MetaData(conn)
        if 'duckdb' not in type(self.db.dialect).__module__:
            metadata.reflect(self.db)

        var_cols = {}
        for qs, qp, qo in bgp:
            nonvar = lambda n: n if not isinstance(n, Variable) else None
            pattern = nonvar(qs), nonvar(qp), nonvar(qo)
            subquery = self.queryPattern(metadata, pattern).subquery()
            for node, col in zip((qs, qp, qo), subquery.c):
                if isinstance(node, Variable):
                    var_cols.setdefault(node, []).append(col)
        sel = [cs[0].label(str(v)) for v, cs in var_cols.items()]
        where = [
            (c0 == c)
            for (c0, *cs) in var_cols.values()
            for c in cs
        ]
        return select(*sel).where(*where)

    def queryFilter(self, conn, part):
        expr = part.expr
        part_query = self.queryPart(conn, part.p)
        if hasattr(expr, 'name') and (expr.name == 'RelationalExpression'):
            var_col = {Variable(c.key):c for c in part_query.inner_columns}
            # TODO: eval group expr!
            a = var_col.get(expr.expr, expr.expr.n3())
            b = var_col.get(expr.other, expr.other.n3())
            # Assume one of two expressions is a column!
            c1, c2 = (a,b) if hasattr(a, 'bool_op') else (b, a)
            clause = c1.bool_op(expr.op)(c2)
            return part_query.where(clause)

        raise NotImplementedError
    
    def queryJoin(self, conn, part):
        query1 = self.queryPart(conn, part.p1)
        query2 = self.queryPart(conn, part.p2)
        var_cols = {}
        for c in list(query1.c) + list(query2.c):
            var_cols.setdefault(c.name, []).append(c)
        sel = [cs[0].label(str(v)) for v, cs in var_cols.items()]
        where = [
            (c0 == c)
            for (c0, *cs) in var_cols.values()
            for c in cs
        ]
        return select(*sel).where(*where)
    
    def queryAggregateJoin(self, conn, agg):
        funcs = {
            "Aggregate_Count": sqlfunc.count,
            "Aggregate_Sample": lambda x:x,
            "Aggregate_Sum": sqlfunc.sum,
            "Aggregate_Avg": sqlfunc.avg,
            "Aggregate_Min": sqlfunc.min,
            "Aggregate_Max": sqlfunc.max,
            "Aggregate_GroupConcat": sqlfunc.group_concat,
        }
        # Assume agg.p is always a Group
        group_expr, group_part = agg.p.expr, agg.p.p
        part_query = self.queryPart(conn, group_part)
        cols = list(part_query.inner_columns)
        var_col = {Variable(c.key): c for c in cols}
        # TODO: eval group expr!
        cols = [funcs.get(a.name)(var_col[a.vars]).label(str(a.res)) for a in agg.A]
        groups = [var_col[e] for e in group_expr]
        return part_query.group_by(*groups).with_only_columns(cols)
    
    def queryExtend(self, conn, part):
        part_query = self.queryPart(conn, part.p)
        cols = list(part_query.inner_columns)
        var_col = {Variable(c.key): c for c in cols}
        cols += [var_col[part.expr].label(str(part.var))]
        return part_query.with_only_columns(cols)

    def queryProject(self, conn, part):
        part_query = self.queryPart(conn, part.p)
        cols = list(part_query.inner_columns)
        var_col = {Variable(c.key): c for c in cols}
        cols = [var_col[c] for c in part.PV]
        return part_query.with_only_columns(cols)

    def queryPart(self, conn, part):
        if part.name == "BGP":
            return self.queryBGP(conn, part.triples)
        if part.name == "Filter":
            return self.queryFilter(conn, part)
        if part.name == "Extend":
            return self.queryExtend(conn, part)
        if part.name == "Project":
            return self.queryProject(conn, part)
        if part.name == "Join":
            return self.queryJoin(conn, part)
        if part.name == "AggregateJoin":
            return self.queryAggregateJoin(conn, part)
        if part.name == "ToMultiSet":
            # no idea what this should do
            return self.queryPart(conn, part.p)
        raise NotImplementedError

    def exec(self, query):
        with self.db.connect() as conn:
            qstr = str(query.compile(compile_kwargs={"literal_binds": True}))
            import sqlparse
            qstr = sqlparse.format(qstr, reindent=True, keyword_case='upper')
            logging.warn(qstr)

            results = conn.execute(query)
            rows = list(results)
            keys = [Variable(v) for v in results.keys()]
            logging.warn(f"Got {len(rows)} rows of {keys}")
            for vals in rows:
                yield dict(zip(keys, [self.make_node(v) for v in vals]))

    def evalPart(self, part):
        with self.db.connect() as conn:
            query = self.queryPart(conn, part)
        return self.exec(query)

    def make_node(self, val):
        isstr = isinstance(val, str)
        if val is None:
            return None
        elif (not isstr) or (val[0] not in '"<_'):
            if type(val) == bytes:
                return Literal(
                    base64.b16encode(o),
                    datatype=XSD.hexBinary,
                )
            else:
                return Literal(val)
        elif val.startswith("<"):
            return self._iri_encode(val)
        elif val == "_:":
            return BNode()
        elif val.startswith("_:"):
            return from_n3(val)
        else:
            return from_n3(val)

    def triples(self, pattern, context) -> Iterable[Triple]:
        """Search for a triple pattern in a DB mapping.

        Args:
          - pattern: The triple pattern (s, p, o) to search.
          - context: The query execution context.

        Returns: An iterator that produces RDF triples matching the input triple pattern.
        """
        nonvar = lambda n: n if not isinstance(n, Variable) else None
        pattern = tuple(nonvar(n) for n in pattern)

        result_count = 0
        with self.db.connect() as conn:
            metadata = MetaData(conn)
            if 'duckdb' not in type(self.db.dialect).__module__:
                metadata.reflect(self.db)

            query = self.queryPattern(metadata, pattern)
            rows = list(conn.execute(query))
            for s, p, o, g in rows:
                gnode = from_n3(g)
                snode = self.make_node(s)
                pnode = self.make_node(p)
                onode = self.make_node(o)
                if (snode is None) or (onode is None):
                    continue

                result = snode, pnode, onode
                result_count += 1
                # logging.warn(f"result: {result}")
                yield result, gnode
        
        ns = self.mapping.graph.namespace_manager
        patstr = ' '.join((n.n3(ns) if n else '_') for n in pattern)
        logging.warn(f"pattern: {patstr}, results: {result_count}")
    
    def _iri_encode(self, iri_n3):
        iri = iri_n3[1:-1]
        uri = re.sub("<ENCODE>(.+?)</ENCODE>", lambda x: iri_safe(x.group(1)), iri)
        return URIRef(uri, base=self.base)

    def create(self, configuration):
        raise TypeError("The DB mapping is read only!")

    def destroy(self, configuration):
        raise TypeError("The DB mapping is read only!")

    def commit(self):
        raise TypeError("The DB mapping is read only!")

    def rollback(self):
        raise TypeError("The DB mapping is read only!")

    def add(self, _, context=None, quoted=False):
        raise TypeError("The DB mapping is read only!")

    def addN(self, quads):
        raise TypeError("The DB mapping is read only!")

    def remove(self, _, context):
        raise TypeError("The DB mapping is read only!")
