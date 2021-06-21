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

import parse
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

from sqlalchemy import MetaData, select, text, null, literal_column
from sqlalchemy import union_all, or_ as sql_or, and_ as sql_and
from sqlalchemy import schema as sqlschema, types as sqltypes, func as sqlfunc
from sqlalchemy.engine import Engine

from rdflib_r2r.types import Any, Optional, Triple, NamedTuple

rr = Namespace("http://www.w3.org/ns/r2rml#")


def iri_safe(v):
    return urllib.parse.quote(v, safe="")


def iri_unsafe(v):
    return urllib.parse.unquote(v)


class Mapping:
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
                    pname = f"{tablename}#{colname}"
                    mg.add([pomap, rr.predicate, base[iri_safe(pname)]])

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
                    pname = f"{tablename}#ref-{';'.join(fk['constrained_columns'])}"
                    mg.add([pomap, rr.predicate, base[iri_safe(pname)]])

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

        logging.warn("direct:")
        for line in mg.serialize(format="turtle").decode().splitlines():
            logging.warn(line)
        return cls(mg)

    @classmethod
    def _template_to_parser(cls, template, irisafe=None):
        # TODO: iri safe?
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)
        template = re.sub('{"', "{", template)
        template = re.sub('"}', "}", template)
        return template

    @classmethod
    def _term_pat(cls, graph, parent, shortcut, mapper, obj=False):
        """Get pattern matchers based on term mappings

        Args:
            graph: Mapping graph
            parent: Parent mapping
            shortcut: Shortcut property
            mapper: Mapper property
            obj (bool, optional): Whether this is an object mapping. Defaults to False.

        Yields:
            Union[str, parse.Pattern]: Node n3 pattern
        """
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
                yield const.n3()
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield const.n3()
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        col = graph.value(tmap, rr.column)
                        col = re.sub('(^"|"$)', "", col)
                        func = "{%s}" % col
                        if obj:
                            # for objects, the default term type is Literal
                            termtype = graph.value(tmap, rr.termType) or rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        func = cls._template_to_parser(
                            template, irisafe=(termtype == rr.IRI)
                        )
                    else:
                        continue

                    if termtype == rr.IRI:
                        yield parse.compile("<" + func + ">")
                    elif termtype == rr.BlankNode:
                        yield parse.compile("_:" + func)
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            func = '"' + func + '"@' + str(lang)
                            yield parse.compile(func)
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            func = '"' + func + '"^^' + dtype.n3()
                            yield parse.compile(func)
                        else:
                            func = '"' + func + '"'
                            yield parse.compile(func)

    def __init__(self, g):
        self.graph = g

        self.spat_tmaps, self.ppat_pomaps, self.opat_pomaps = {}, {}, {}
        for tmap in g[: RDF.type : rr.TriplesMap]:
            for s_pat in self._term_pat(g, tmap, rr.subject, rr.subjectMap):
                self.spat_tmaps.setdefault(s_pat, []).append(tmap)
            for po_i, pomap in enumerate(g[tmap : rr.predicateObjectMap :]):
                for p_pat in self._term_pat(g, pomap, rr.predicate, rr.predicateMap):
                    self.ppat_pomaps.setdefault(p_pat, []).append(pomap)
                for o_pat in self._term_pat(g, pomap, rr.object, rr.objectMap, True):
                    self.opat_pomaps.setdefault(o_pat, []).append(pomap)

        logging.warn(("spat_tmaps", self.spat_tmaps))
        logging.warn(("ppat_pomaps", self.ppat_pomaps))
        logging.warn(("opat_pomaps", self.opat_pomaps))

    @staticmethod
    def get_node_filter(node, pat_maps):
        map_conditions = {}
        if node is not None:
            for pat, maps in pat_maps.items():
                # Ignore conditions on BNodes and non-string Literals
                if isinstance(node, BNode) or (getattr(node, 'datatype', None) != None):
                    for m in maps:
                        # No condition, select all
                        map_conditions.setdefault(m, []).append(True)
                elif isinstance(pat, str):
                    if node.n3() == pat:
                        for m in maps:
                            # No condition, select all
                            map_conditions.setdefault(m, []).append(True)
                else:
                    logging.warn(("parse", str(pat), node, pat.parse(node.n3())))
                    if pat.parse(node.n3()):
                        where = sql_and(
                            *[
                                literal_column(k) == v
                                for k, v in pat.parse(node.n3()).named.items()
                            ]
                        )
                        for m in maps:
                            map_conditions.setdefault(m, []).append(where)
            return {
                m: ([] if (True in wheres) else [sql_or(*wheres)])
                for m, wheres in map_conditions.items()
            }
        else:
            return {None: []}

    def try_map(self, pattern):
        sfilt = self.get_node_filter(pattern[0], self.spat_tmaps)
        pfilt = self.get_node_filter(pattern[1], self.ppat_pomaps)
        ofilt = self.get_node_filter(pattern[2], self.opat_pomaps)
        return sfilt, pfilt, ofilt


class R2RStore(Store):
    """
    Args:
      - db: SQLAlchemy engine.
    """

    def __init__(
        self,
        db: Engine,
        mapping: Optional[Mapping] = None,
        base: str = "http://example.com/base/",
        configuration=None,
        identifier=None,
    ):
        super(R2RStore, self).__init__(
            configuration=configuration, identifier=identifier
        )
        self.db = db
        self.mapping = mapping or Mapping.from_db(db)
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

    @staticmethod
    def _sql_safe(literal):
        return "<ENCODE>" + literal + "</ENCODE>"

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
                    c = cls._sql_safe(c)
                parts.append(c)
        parts = [sqlfunc.cast(x, sqltypes.VARCHAR) for x in parts if x != ""]
        return functools.reduce(operator.add, parts)

    @classmethod
    def _term_map(cls, graph, tname, dbtable, parent, mapper, shortcut, obj=False):
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
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
                        yield "<" + func + ">"
                    elif termtype == rr.BlankNode:
                        yield "_:" + func
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            yield '"' + func + '"@' + str(lang)
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            yield '"' + func + '"^^' + dtype.n3()
                        else:
                            # keep original datatype
                            yield func
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

    def _triplesmap_select(self, metadata, graph, tmap, pfilt, ofilt):
        dbtable, tname = self._get_table(graph, tmap)
        dbtable = metadata.tables.get(tname.strip('"'), dbtable)

        ss = self._term_map(graph, tname, dbtable, tmap, rr.subjectMap, rr.subject)
        s = next(ss).label("s")

        s_map = graph.value(tmap, rr.subjectMap)
        gs = list(self._term_map(graph, tname, dbtable, s_map, rr.graphMap, rr.graph))

        # Class Map
        if (not pfilt) or (None in pfilt):
            for c in graph[s_map : rr["class"]]:
                p = literal_column("'%s'" % RDF.type.n3()).label("p")
                o = literal_column("'%s'" % c.n3()).label("o")
                for g in list(gs) or [null()]:
                    yield (s, p, o, g.label("g")), dbtable, []

        # Select Predicate-Object Maps
        pomaps = set(graph[tmap : rr.predicateObjectMap :])
        if not (None in pfilt):
            pomaps &= set(pfilt)
        if not (None in ofilt):
            pomaps &= set(ofilt)
        pomap_conditions = {
            pomap: (pfilt.get(pomap) or []) + (ofilt.get(pomap) or [])
            for pomap in pomaps
        }

        for pomap, wheres in pomap_conditions.items():
            ps = list(
                self._term_map(
                    graph, tname, dbtable, pomap, rr.predicateMap, rr.predicate
                )
            )
            os = list(
                self._term_map(
                    graph, tname, dbtable, pomap, rr.objectMap, rr.object, True
                )
            )
            gs = list(
                self._term_map(graph, tname, dbtable, pomap, rr.graphMap, rr.graph)
            )
            for p in ps:
                p = p.label("p")
                for o in os:
                    o = o.label("o")
                    for g in list(gs) or [null()]:
                        yield (s, p, o, g.label("g")), dbtable, wheres

    def triples(self, pattern, context) -> Iterable[Triple]:
        """Search for a triple pattern in a DB mapping.

        Args:
          - pattern: The triple pattern (s, p, o) to search.
          - context: The query execution context.

        Returns: An iterator that produces RDF triples matching the input triple pattern.
        """

        sfilt, pfilt, ofilt = self.mapping.try_map(pattern)
        logging.warn(("pattern", pattern, "filters", sfilt, pfilt, ofilt))

        mg = self.mapping.graph
        with self.db.connect() as conn:
            metadata = MetaData(conn)
            metadata.reflect(self.db)

            # Triple Maps
            tmaps = {tmap: [] for tmap in mg[: RDF.type : rr.TriplesMap]}
            if not (None in sfilt):
                tmaps = {tmap: sfilt[tmap] for tmap in set(tmaps) & set(sfilt)}
            for tmap, swhere in tmaps.items():
                selects = self._triplesmap_select(metadata, mg, tmap, pfilt, ofilt)
                for spog, dbtable, powhere in selects:

                    query = select(*spog).select_from(dbtable).where(*swhere, *powhere)

                    rows = list(conn.execute(query))
                    logging.warn(("query", str(query), len(rows), "results"))
                    for s, p, o, g in rows:
                        logging.warn(("spog", s, p, o, g))
                        gnode = from_n3(g)

                        if s is None:
                            continue
                        elif s.startswith("<"):
                            suri = self._iri_encode(s[1:-1])
                            snode = URIRef(suri, base=self.base)
                        elif s == "_:":
                            snode = BNode()
                        else:
                            snode = BNode(hex(hash(s) ** 2)[2:])

                        puri = self._iri_encode(p[1:-1])
                        pnode = URIRef(puri, base=self.base)

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
                            onode = URIRef(o_uri, base=self.base)
                        elif o.startswith("_:"):
                            onode = BNode(hex(hash(o) ** 2)[2:])
                        else:
                            onode = from_n3(o)
                        
                        result = snode, pnode, onode
                        qs, qp, qo = pattern
                        if (
                            ((qs is not None) and (snode != qs))
                            or ((qp is not None) and (pnode != qp))
                            or ((qo is not None) and (onode != qo))
                        ):
                            logging.warn(f"Manually discarded {result}")
                            continue
                        yield result, gnode

    @staticmethod
    def _iri_encode(iri):
        return re.sub("<ENCODE>(.+?)</ENCODE>", lambda x: iri_safe(x.group(1)), iri)

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
