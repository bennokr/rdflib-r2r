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

from sqlalchemy import MetaData, select, text, literal, literal_column, union_all
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
                mg.add([s_map, rr.termType, rr.BlankNode])
                mg.add([s_map, rr["class"], base[table.name]])
                for column in table.c:
                    po_map = BNode()
                    mg.add([tm, rr.predicateObjectMap, po_map])
                    pred = base[f"{table.name}#{column.name}"]
                    mg.add([po_map, rr.predicate, pred])
                    o_map = BNode()
                    mg.add([po_map, rr.objectMap, o_map])
                    mg.add([o_map, rr.column, Literal(f'"{column.name}"')])
                    logging.warn(('column.type', column.type))
                    if isinstance(column.type, sqltypes.Integer):
                        mg.add([o_map, rr.datatype, XSD.integer])

        logging.warn("direct: %s", mg.serialize(format="turtle"))
        return cls(mg)

    @staticmethod
    def cols_to_rownode(cols):
        # TODO: IRI-encode
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

    def triples(self, pattern, context) -> Iterable[Triple]:
        """Search for a triple pattern in a DB mapping.

        Args:
          - pattern: The triple pattern (s, p, o) to search.
          - context: The query execution context.

        Returns: An iterator that produces RDF triples matching the input triple pattern.
        """

        def get_col(dbtable, colname):
            try:
                return dbtable.c[colname[1:-1]]
            except KeyError:
                # rr.sqlQuery is set
                return literal_column(colname)


        def template_to_function(dbtable, template):
            # TODO: IRI-encode
            prefix, *rest = template.split("{")
            parts = [prefix] + [
                x
                for part in rest
                for colname, _, suffix in [part.partition("}")]
                for x in (get_col(dbtable, colname).cast(sqltypes.String), suffix)
                if x != ""
            ]
            logging.warn(("template_to_function", parts))
            return functools.reduce(operator.add, parts)

        def quad_query(dbtable, s_func, p_func, o_func, g_func):
            return select(
                s_func.label("s"),
                p_func.label("p"),
                o_func.label("o"),
                g_func.label("g"),
            ).select_from(dbtable)

        mg = self.mapping.graph
        with self.db.connect() as conn:
            qunion = []
            if pattern == (None, None, None):
                metadata = MetaData(conn)
                metadata.reflect(self.db)

                # Triple Maps
                for tm in mg[: RDF.type : rr.TriplesMap]:
                    logtable = mg.value(tm, rr.logicalTable)
                    if mg.value(logtable, rr.tableName):
                        tablename = mg.value(logtable, rr.tableName).toPython()[1:-1]
                        dbtable = metadata.tables[tablename]
                    else:
                        sqlquery = mg.value(logtable, rr.sqlQuery)
                        dbtable = select(text(f"* FROM ({sqlquery})")).subquery()

                    g_func = literal_column("'<graph>'")

                    # Subject Map
                    s_map = mg.value(tm, rr.subjectMap)
                    s_termtype: Optional[URIRef] = mg.value(s_map, rr.termType)
                    if mg.value(s_map, rr.constant):
                        s_const = mg.value(s_map, rr.constant).toPython()
                        s_func = literal_column("'<%s>'" % s_const)
                    elif mg.value(s_map, rr.template) or mg.value(s_map, rr.column):
                        s_template = mg.value(s_map, rr.template)
                        if s_template:
                            s_urifunc = template_to_function(dbtable, s_template)
                            s_termtype = s_termtype or rr.IRI
                        else:
                            s_column = mg.value(s_map, rr.column).toPython()
                            s_urifunc = literal_column(s_column)
                            s_termtype = s_termtype or rr.Literal
                        if s_termtype == rr.IRI:
                            s_func = "<" + s_urifunc + ">"
                        else:
                            s_func = "_:" + s_urifunc
                    elif s_termtype == rr.BlankNode:
                        s_func = "_:" + Mapping.cols_to_rownode(dbtable.c)

                    for s_class in mg[s_map : rr["class"]]:
                        type_func = literal_column("'%s'" % RDF.type.n3())
                        cls_func = literal_column("'%s'" % s_class.n3())
                        q = quad_query(dbtable, s_func, type_func, cls_func, g_func)
                        qunion.append(q)

                    # Predicate-Object Maps
                    for po_map in mg[tm : rr.predicateObjectMap :]:
                        if mg.value(po_map, rr.predicate):
                            p_const = mg.value(po_map, rr.predicate)
                        else:
                            p_map = mg.value(po_map, rr.predicateMap)
                            p_const = mg.value(p_map, rr.constant)
                        p_func = literal_column("'<%s>'" % p_const)

                        o_map = mg.value(po_map, rr.objectMap)
                        if mg.value(o_map, rr.constant):
                            o_const = mg.value(o_map, rr.constant).toPython()
                            o_func = literal_column("'<%s>'" % o_const)
                        else:
                            o_template = mg.value(o_map, rr.template)
                            o_termtype: Optional[URIRef] = mg.value(o_map, rr.termType)
                            if o_template:
                                o_urifunc = template_to_function(dbtable, o_template)
                                o_termtype = o_termtype or rr.IRI
                            else:
                                o_column = mg.value(o_map, rr.column).toPython()
                                o_urifunc = literal_column(o_column)
                                o_termtype = o_termtype or rr.Literal

                            if o_termtype == rr.IRI:
                                o_func = "<" + o_urifunc + ">"
                            else:
                                if mg.value(o_map, rr.language):
                                    o_func = '"' + o_urifunc + '"'
                                    o_func += "@" + str(mg.value(o_map, rr.language))
                                elif mg.value(o_map, rr.datatype):
                                    o_func = '"' + o_urifunc + '"'
                                    o_func += "^^" + mg.value(o_map, rr.datatype).n3()
                                else:
                                    o_func = o_urifunc

                        q = quad_query(dbtable, s_func, p_func, o_func, g_func)
                        qunion.append(q)

            if qunion:
                query = union_all(*qunion) if len(qunion) > 1 else qunion[0]
                for s, p, o, g in conn.execute(query):
                    logging.warn(("spog", (s, p, o, g)))
                    if s.startswith('<'):
                        snode = URIRef(self._iri_encode(s[1:-1]))
                    else:
                        snode = BNode(hex(hash(s) ** 2)[2:])
                    
                    pnode = URIRef(self._iri_encode(p[1:-1]))

                    if (not isinstance(o, str)) or (o[0] not in '"<_'):
                        onode = Literal(o)
                    elif o.startswith('<'):
                        onode = URIRef(self._iri_encode(o[1:-1]))
                    else:
                        onode = from_n3(o)
                    
                    yield (snode, pnode, onode), from_n3(g)

    @staticmethod
    def _iri_encode(iri):
        parts = iri.split('/', 3)
        logging.warn(('parts', parts))
        parts[-1] = quote(parts[-1], safe='/#;')
        return '/'.join(parts)

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
