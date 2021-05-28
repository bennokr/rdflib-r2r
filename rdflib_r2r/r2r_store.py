"""
rdflib_r2r.r2r_store
=======================
"""
from typing import Iterable
import logging
import functools
import operator
import itertools

from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

from sqlalchemy import MetaData, select, text, null, literal_column, union_all
from sqlalchemy import types as sqltypes, func as sqlfunc

from urllib.parse import quote

from rdflib_r2r.types import Any, Optional, Engine, Triple, NamedTuple

rr = Namespace("http://www.w3.org/ns/r2rml#")


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
            metadata = MetaData(conn)
            metadata.reflect(db)
            for tablename, table in metadata.tables.items():
                tm = BNode()
                mg.add([tm, RDF.type, rr.TriplesMap])
                logtable = BNode()
                mg.add([tm, rr.logicalTable, logtable])
                mg.add([logtable, rr.tableName, Literal(f'"{table.name}"')])

                s_map = BNode()
                mg.add([tm, rr.subjectMap, s_map])
                mg.add([s_map, rr["class"], base[table.name]])
                
                if table.primary_key:
                    parts = ['%s={%s}' % (c.name,c.name) for c in table.primary_key]
                    template = baseuri + table.name + '/' + ';'.join(parts)
                    mg.add([s_map, rr.template, Literal(template)])
                else:
                    mg.add([s_map, rr.termType, rr.BlankNode])

                # if table.foreign_keys:


                for column in table.c:
                    po_map = BNode()
                    mg.add([tm, rr.predicateObjectMap, po_map])
                    pred = base[f"{table.name}#{column.name}"]
                    mg.add([po_map, rr.predicate, pred])

                    o_map = BNode()
                    mg.add([po_map, rr.objectMap, o_map])
                    mg.add([o_map, rr.column, Literal(f'"{column.name}"')])
                    if isinstance(column.type, sqltypes.Integer):
                        mg.add([o_map, rr.datatype, XSD.integer])

        logging.warn("direct: %s", mg.serialize(format="turtle"))
        return cls(mg)

    @staticmethod
    def cols_to_rownode(cols):
        vals = [
            x
            for c in cols
            for x in [c.name, "=", sqlfunc.cast(c, sqltypes.String), ";"]
        ]
        logging.warn(("cols_to_rownode", vals))
        return functools.reduce(operator.add, vals[:-1])


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
    def _template_to_function(template):
        prefix, *rest = template.split("{")
        parts = [prefix] + [
            x
            for part in rest
            for col, _, suffix in [part.partition("}")]
            for x in (literal_column(col).cast(sqltypes.String), suffix)
            if x != ""
        ]
        logging.warn(("template_to_function", parts))
        return functools.reduce(operator.add, parts)

    @classmethod
    def _term_map(cls, graph, parent, mapper, shortcut, obj=False):
        if graph.value(parent, shortcut):
            for column in graph[parent:shortcut]:
                yield literal_column("'<%s>'" % column)
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    yield literal_column("'%s'" % graph.value(tmap, rr.constant).n3())
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        urifunc = literal_column(graph.value(tmap, rr.column))
                        if obj:
                            termtype = rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        urifunc = cls._template_to_function(template)
                    elif graph.value(tmap, rr.parentTriplesMap):
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        if graph.value(tmap, rr.joinCondition):
                            continue
                        else:
                            rs = cls._term_map(graph, ref, rr.subjectMap, rr.subject)
                            yield from rs
                            continue
                    else:
                        yield literal_column("'_:'")
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
                            yield urifunc # keep original datatype
                    else:
                        yield literal_column("'_:'")
    
    @classmethod
    def _triplesmap_select(cls, mg, tmap):
        logtable = mg.value(tmap, rr.logicalTable)
        if mg.value(logtable, rr.tableName):
            dbtable = text(mg.value(logtable, rr.tableName).toPython())
        else:
            sqlquery = mg.value(logtable, rr.sqlQuery)
            dbtable = text(f"({sqlquery})")

        terms = {}
        for s in cls._term_map(mg, tmap, rr.subjectMap, rr.subject):
            terms['s'] = s
        s_map = mg.value(tmap, rr.subjectMap)
        gs = cls._term_map(mg, s_map, rr.graphMap, rr.graph)
        for gi, g in enumerate(gs):
            terms[f'g{gi}'] = g
        for ci, c in enumerate(mg[s_map : rr["class"]]):
            terms[f'c{ci}'] = literal_column("'%s'" % c.n3())

        # Predicate-Object Maps
        for po_i, po_map in enumerate(mg[tmap : rr.predicateObjectMap :]):
            ps = cls._term_map(mg, po_map, rr.predicateMap, rr.predicate)
            for pi, p in enumerate(ps):
                terms[f'v{po_i}-p{pi}'] = p
            os = cls._term_map(mg, po_map, rr.objectMap, rr.object, True)
            for oi, o in enumerate(os):
                terms[f'v{po_i}-o{oi}'] = o
            gs = cls._term_map(mg, po_map, rr.graphMap, rr.graph)
            for gi, g in enumerate(gs):
                terms[f'v{po_i}-g{gi}'] = g
        
        return select(*[v.label(k) for k,v in terms.items()]).select_from(dbtable)

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
                    
                    query = self._triplesmap_select(mg, tm)

                    for row in conn.execute(query):
                        fields = {}
                        for k, v in row._mapping.items():
                            a, _, b = k.partition('-')
                            if not b:
                                fields.setdefault(a[0], []).append(v)
                            else:
                                field = fields.setdefault(a[0], {}) \
                                    .setdefault(a[1:], {}) \
                                    .setdefault(b[0], []).append(v)
                        
                        for s in fields['s']:
                            for g in fields.get('g', ['_:']):
                                gnode = from_n3(g)
                                if s.startswith("<"):
                                    snode = URIRef(self._iri_encode(s[1:-1]))
                                elif s == '_:':
                                    snode = BNode()
                                else:
                                    snode = BNode(hex(hash(s) ** 2)[2:])
                                
                                for c in fields.get('c', []):
                                    cnode = from_n3(c)
                                    yield (snode, RDF.type, cnode), gnode
                                
                                for v in fields['v'].values():
                                    for p in v['p']:
                                        pnode = URIRef(self._iri_encode(p[1:-1]))

                                        for o in v['o']:
                                            o_isstr = isinstance(o, str)
                                            if (not o_isstr) or (o[0] not in '"<_'):
                                                onode = Literal(o)
                                            elif o.startswith("<"):
                                                o_uri = self._iri_encode(o[1:-1])
                                                onode = URIRef(o_uri)
                                            else:
                                                onode = from_n3(o)

                                            for g2 in v.get('g', ['_:']):
                                                if g2 != g:
                                                    gnode = from_n3(g2)
                                                
                                                logging.warn(('spog', s, p, o, g))
                                                yield (snode, pnode, onode), gnode

    @staticmethod
    def _iri_encode(iri):
        parts = iri.split("/", 3)
        parts[-1] = quote(parts[-1], safe="/#;=")
        return "/".join(parts)

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
