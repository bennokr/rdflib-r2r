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

from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

from sqlalchemy import MetaData, select, text, null, literal_column, union_all
from sqlalchemy import schema as sqlschema, types as sqltypes, func as sqlfunc

from rdflib_r2r.types import Any, Optional, Engine, Triple, NamedTuple

rr = Namespace("http://www.w3.org/ns/r2rml#")


def iri_safe(v):
    return urllib.parse.quote(v, safe="/#;=")


def iri_unsafe(v):
    return urllib.parse.unquote(v)


class Mapping(NamedTuple):
    graph: Graph

    @classmethod
    def from_db(cls, db, baseuri="http://example.com/base/"):
        """Create RDB2RDF Direct Mapping

        See also: https://www.w3.org/TR/rdb-direct-mapping/

        Args:
            db (sqlalchemy.Engine): Database
            baseuri (str, optional): Base URI. Defaults to "http://example.com/base/".

        Returns:
            Mapping
        """
        base = Namespace(baseuri)
        mg = Graph()

        with db.connect() as conn:
            tmaps = {}
            for tablename in db.dialect.get_table_names(conn, schema='main'):
                tm = tmaps.setdefault(tablename, BNode())
                mg.add([tm, RDF.type, rr.TriplesMap])
                logtable = BNode()
                mg.add([tm, rr.logicalTable, logtable])
                mg.add([logtable, rr.tableName, Literal(f'"{tablename}"')])

                s_map = BNode()
                mg.add([tm, rr.subjectMap, s_map])
                mg.add([s_map, rr["class"], base[iri_safe(tablename)]])

                # TEMPORARY: duckdb hack
                pk = db.dialect.get_pk_constraint(conn, tablename, schema='main')
                if pk and any(pk.values()):
                    primary_keys = (
                        pk['constrained_columns'] 
                        or eval(pk['name'].partition('KEY')[-1])
                    )
                    if not (type(primary_keys) in [tuple, list]):
                        primary_keys = (primary_keys, )
                else:
                    primary_keys = []

                if primary_keys:
                    parts = ['%s={"%s"}' % (c, c) for c in primary_keys]
                    template = baseuri + tablename + "/" + ";".join(parts)
                    mg.add([s_map, rr.template, Literal(template)])
                else:
                    mg.add([s_map, rr.termType, rr.BlankNode])

                for column in db.dialect.get_columns(conn, tablename, schema='main'):
                    colname = column['name']
                    coltype = column['type']
                    # Add a predicate-object map per column
                    po_map = BNode()
                    mg.add([tm, rr.predicateObjectMap, po_map])
                    pname = f"{tablename}#{colname}"
                    mg.add([po_map, rr.predicate, base[iri_safe(pname)]])

                    o_map = BNode()
                    mg.add([po_map, rr.objectMap, o_map])
                    mg.add([o_map, rr.column, Literal(f'"{colname}"')])
                    if isinstance(coltype, sqltypes.Integer):
                        mg.add([o_map, rr.datatype, XSD.integer])

                    foreign_keys = db.dialect.get_foreign_keys(conn, tablename, schema='main')

                    for fk in foreign_keys:
                        # Add another predicate-object map for every foreign key
                        po_map = BNode()
                        mg.add([tm, rr.predicateObjectMap, po_map])
                        pname = f"{tablename}#ref-{colname}"
                        mg.add([po_map, rr.predicate, base[iri_safe(pname)]])

                        o_map = BNode()
                        mg.add([po_map, rr.objectMap, o_map])
                        reftable = fk['referred_table']
                        refmap = tmaps.setdefault(reftable, BNode())
                        mg.add([o_map, rr.parentTriplesMap, refmap])
                        
                        join = BNode()
                        mg.add([o_map, rr.joinCondition, join])
                        mg.add([join, rr.child, Literal(f'"{colname}"')])
                        for refcol in fk['referred_columns']:
                            mg.add([join, rr.parent, Literal(f'"{refcol}"')])

        logging.warn("direct:")
        for line in mg.serialize(format="turtle").decode().splitlines():
            logging.warn(line)
        return cls(mg)


class R2RStore(Store):
    """

    It is heavily inspired by rdflib-hdt .

    Args:
      - db: SQLAlchemy engine.
    """

    def __init__(
        self,
        db: Engine,
        mapping: Optional[Mapping] = None,
        configuration=None,
        identifier=None,
    ):
        super(R2RStore, self).__init__(
            configuration=configuration, identifier=identifier
        )
        self.db = db
        self.mapping = mapping or Mapping.from_db(db)
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
    def _template_to_function(dbtable, tname, template):
        # make python format string: escape curly braces by doubling {{ }}
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)

        def get_col(col):
            if type(dbtable) is sqlschema.Table:
                dbcol = dbtable.c[col.strip('"')]
                logging.warn(("dbtable[col]", dbcol))
                if isinstance(dbcol.type, sqltypes.Numeric):
                    if dbcol.type.precision:
                        return sqlfunc.hex(dbcol)
                return dbcol.cast(sqltypes.VARCHAR)
            else:
                return literal_column(f"{tname}.{col}").cast(sqltypes.VARCHAR)

        parts = [
            x
            for prefix, col, _, _ in Formatter().parse(template)
            for x in (
                sqlfunc.cast(prefix, sqltypes.VARCHAR),
                get_col(col) if col else "",
            )
            if x != ""
        ]
        logging.warn(("template_to_function", parts))
        return functools.reduce(operator.add, parts)

    @classmethod
    def _term_map(cls, graph, tname, dbtable, parent, mapper, shortcut, obj=False):
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
                yield literal_column("'%s'" % iri_unsafe(const.n3()))
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield literal_column("'%s'" % iri_unsafe(const.n3()))
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        col = graph.value(tmap, rr.column)
                        urifunc = literal_column(f"{tname}.{col}")
                        if obj:
                            # for objects, the default term type is Literal
                            termtype = graph.value(tmap, rr.termType) or rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        urifunc = cls._template_to_function(dbtable, tname, template)
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        ptable, pname = cls._get_table(graph, ref)
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
                        # WARNING: Rowid is not supported in all RDBs!
                        # TODO: replace with RDB-specific construct (postgresql?)
                        rowid = literal_column(f"{tname}.rowid").cast(sqltypes.VARCHAR)
                        yield f"_:{tname}#" + rowid
                        continue

                    if termtype == rr.IRI:
                        yield "<" + urifunc + ">"
                    elif termtype == rr.BlankNode:
                        yield "_:" + urifunc
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            yield '"' + urifunc + '"@' + str(lang)
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            yield '"' + urifunc + '"^^' + dtype.n3()
                        else:
                            # keep original datatype
                            yield urifunc
                    else:
                        yield literal_column("'_:'")

    @classmethod
    def _get_table(cls, graph, tmap):
        logtable = graph.value(tmap, rr.logicalTable)
        if graph.value(logtable, rr.tableName):
            tname = graph.value(logtable, rr.tableName).toPython()
            return text(tname), tname
        else:
            tname = f'"View_{base64.b32encode(str(tmap).encode()).decode()}"'
            sqlquery = graph.value(logtable, rr.sqlQuery).strip().strip(";")
            return text(f"({sqlquery}) AS {tname}"), tname

    def _triplesmap_select(self, metadata, graph, tmap):
        dbtable, tname = self._get_table(graph, tmap)
        dbtable = metadata.tables.get(tname.strip('"'), dbtable)

        terms = {}
        for s in self._term_map(graph, tname, dbtable, tmap, rr.subjectMap, rr.subject):
            terms["s"] = s
        s_map = graph.value(tmap, rr.subjectMap)
        gs = self._term_map(graph, tname, dbtable, s_map, rr.graphMap, rr.graph)
        for gi, g in enumerate(gs):
            terms[f"g{gi}"] = g
        for ci, c in enumerate(graph[s_map : rr["class"]]):
            terms[f"c{ci}"] = literal_column("'%s'" % c.n3())

        # Predicate-Object Maps
        for po_i, po_map in enumerate(graph[tmap : rr.predicateObjectMap :]):
            ps = self._term_map(
                graph, tname, dbtable, po_map, rr.predicateMap, rr.predicate
            )
            for pi, p in enumerate(ps):
                terms[f"v{po_i}-p{pi}"] = p
            os = self._term_map(
                graph, tname, dbtable, po_map, rr.objectMap, rr.object, True
            )
            for oi, o in enumerate(os):
                terms[f"v{po_i}-o{oi}"] = o
            gs = self._term_map(graph, tname, dbtable, po_map, rr.graphMap, rr.graph)
            for gi, g in enumerate(gs):
                terms[f"v{po_i}-g{gi}"] = g

        return select(*[v.label(k) for k, v in terms.items()]).select_from(dbtable)

    def triples(self, pattern, context) -> Iterable[Triple]:
        """Search for a triple pattern in a DB mapping.

        Args:
          - pattern: The triple pattern (s, p, o) to search.
          - context: The query execution context.

        Returns: An iterator that produces RDF triples matching the input triple pattern.
        """

        mg = self.mapping.graph
        with self.db.connect() as conn:
            qunion = []
            if pattern == (None, None, None):
                metadata = MetaData(conn)
                metadata.reflect(self.db)

                # Triple Maps
                for tm in mg[: RDF.type : rr.TriplesMap]:

                    query = self._triplesmap_select(metadata, mg, tm)
                    logging.warn(('query', str(query)))
                    for row in conn.execute(query):
                        fields = {}
                        for k, v in row._mapping.items():
                            a, _, b = k.partition("-")
                            if not b:
                                fields.setdefault(a[0], []).append(v)
                            else:
                                (
                                    fields.setdefault(a[0], {})
                                    .setdefault(a[1:], {})
                                    .setdefault(b[0], [])
                                    .append(v)
                                )

                        for s in fields["s"]:
                            for g in fields.get("g", ["_:"]):
                                gnode = from_n3(g)
                                if s is None:
                                    continue
                                elif s.startswith("<"):
                                    snode = URIRef(self._iri_encode(s[1:-1]))
                                elif s == "_:":
                                    snode = BNode()
                                else:
                                    snode = BNode(hex(hash(s) ** 2)[2:])

                                for c in fields.get("c", []):
                                    cnode = from_n3(c)
                                    yield (snode, RDF.type, cnode), gnode

                                for v in fields["v"].values():
                                    for p in v["p"]:
                                        pnode = URIRef(self._iri_encode(p[1:-1]))

                                        for o in v["o"]:
                                            o_isstr = isinstance(o, str)
                                            if o is None:
                                                continue
                                            elif (not o_isstr) or (o[0] not in '"<_'):
                                                if type(o) == bytes:
                                                    onode = Literal(
                                                        base64.b16encode(o),
                                                        datatype=XSD.hexBinary,
                                                    )
                                                else:
                                                    onode = Literal(o)
                                            elif o.startswith("<"):
                                                o_uri = self._iri_encode(o[1:-1])
                                                onode = URIRef(o_uri)
                                            elif o.startswith("_:"):
                                                onode = BNode(hex(hash(o) ** 2)[2:])
                                            else:
                                                onode = from_n3(o)

                                            for g2 in v.get("g", ["_:"]):
                                                if g2 != g:
                                                    gnode = from_n3(g2)

                                                logging.warn(("spog", s, p, o, g))
                                                yield (snode, pnode, onode), gnode

    @staticmethod
    def _iri_encode(iri):
        if not iri.startswith('data'):
            parts = iri.split("/", 3)
            parts[-1] = iri_safe(parts[-1])
            return "/".join(parts)
        else:
            return iri

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
