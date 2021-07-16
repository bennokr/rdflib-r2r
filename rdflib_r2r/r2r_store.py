"""
rdflib_r2r.r2r_store
=======================
"""
from os import linesep
from typing import Iterable, List, Tuple
import logging
import functools
import operator
import base64
import urllib.parse
import re
from string import Formatter

from rdflib import URIRef, Literal, BNode, Variable
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

import sqlalchemy
from sqlalchemy import MetaData, select, text, null, literal_column, literal
from sqlalchemy import union_all, or_ as sql_or, and_ as sql_and
from sqlalchemy import schema as sqlschema, types as sqltypes, func as sqlfunc
import sqlalchemy.sql as sql
from sqlalchemy.sql.expression import ColumnElement, GenerativeSelect, Select

ColMold = Tuple[List[str], List[ColumnElement]]
SelectSubMold = Tuple[Select, List[Tuple[Iterable[int], List[str]]] ]
GenerativeSelectSubMold = Tuple[GenerativeSelect, List[Tuple[Iterable[int], List[str]]] ]

class SparqlNotImplementedError(NotImplementedError):
    pass


from sqlalchemy.engine import Engine

from rdflib_r2r.types import Any, Optional, Triple
from rdflib_r2r.r2r_mapping import R2RMapping, _get_table, iri_safe, iri_unsafe

rr = Namespace("http://www.w3.org/ns/r2rml#")

# https://www.w3.org/2001/sw/rdb2rdf/wiki/Mapping_SQL_datatypes_to_XML_Schema_datatypes

XSDToSQL = {
    XSD.time: sqltypes.Time(),
    XSD.date: sqltypes.Date(),
    XSD.gYear: sqltypes.Integer(),
    XSD.gYearMonth: None,
    XSD.dateTime: None,
    XSD.duration: sqltypes.Interval(),
    XSD.dayTimeDuration: sqltypes.Interval(),
    XSD.yearMonthDuration: sqltypes.Interval(),
    XSD.hexBinary: None,
    XSD.string: sqltypes.String(),
    XSD.normalizedString: None,
    XSD.token: None,
    XSD.language: None,
    XSD.boolean: sqltypes.Boolean(),
    XSD.decimal: sqltypes.Numeric(),
    XSD.integer: sqltypes.Integer(),
    XSD.nonPositiveInteger: sqltypes.Integer(),
    XSD.long: sqltypes.Integer(),
    XSD.nonNegativeInteger: sqltypes.Integer(),
    XSD.negativeInteger: sqltypes.Integer(),
    XSD.int: sqltypes.Integer(),
    XSD.unsignedLong: sqltypes.Integer(),
    XSD.positiveInteger: sqltypes.Integer(),
    XSD.short: sqltypes.Integer(),
    XSD.unsignedInt: sqltypes.Integer(),
    XSD.byte: sqltypes.Integer(),
    XSD.unsignedShort: sqltypes.Integer(),
    XSD.unsignedByte: sqltypes.Integer(),
    XSD.float: sqltypes.Float(),
    XSD.double: sqltypes.Float(),
    XSD.base64Binary: None,
    XSD.anyURI: None,
}


def sql_safe(literal):
    # return "<ENCODE>" + sqlfunc.cast(literal, sqltypes.VARCHAR) + "</ENCODE>"
    # This is a terrible idea due to the large number of chars.
    # ... but the alternative messes up SPARQL query rewriting

    # TEMP: DISABLE FOR DEBUGGING
    literal = sqlfunc.replace(literal, " ", "%20")
    literal = sqlfunc.replace(literal, "/", "%2F")
    literal = sqlfunc.replace(literal, "(", "%28")
    literal = sqlfunc.replace(literal, ")", "%29")
    literal = sqlfunc.replace(literal, ",", "%2C")
    literal = sqlfunc.replace(literal, ":", "%3A")

    return literal


def sql_pretty(query):
    import sqlparse

    qstr = str(query.compile(compile_kwargs={"literal_binds": True}))
    return sqlparse.format(qstr, reindent=True, keyword_case="upper")


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


    def _iri_encode(self, iri_n3):
        iri = iri_n3[1:-1]
        uri = re.sub("<ENCODE>(.+?)</ENCODE>", lambda x: iri_safe(x.group(1)), iri)
        return URIRef(uri, base=self.base)

    @staticmethod
    def _get_col(dbtable, colname, template=False):
        if type(dbtable) is sqlschema.Table:
            dbcol = dbtable.c[colname.strip('"')]

            if isinstance(dbcol.type, sqltypes.Numeric):
                if dbcol.type.precision:
                    if template:
                        # Binary data
                        return sqlfunc.hex(dbcol)
                    else:
                        return literal_column(f'"{dbtable.name}".{colname}')

            if (not template) and isinstance(dbcol.type, sqltypes.CHAR):
                if dbcol.type.length:
                    l = dbcol.type.length
                    return sqlfunc.substr(dbcol + " " * l, 1, l)

            return dbcol
        else:
            return literal_column(f'"{dbtable.name}".{colname}')

    @staticmethod
    def _concat_colmold(strings: List[str], cols: List[ColumnElement]):
        if cols == []:
            return literal_column(''.join(strings))
        cols = list(cols)
        parts = [(literal(s) if s != None else cols.pop(0)) for s in strings]
        return functools.reduce(operator.add, parts)

    @classmethod
    def _template_to_colmolds(cls, dbtable, template, irisafe=False) -> ColMold:
        # make python format string: escape curly braces by doubling {{ }}
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)

        strings, cols = [], []
        for prefix, colname, _, _ in Formatter().parse(template):
            if prefix != "":
                strings.append(prefix)
            if colname:
                col = cls._get_col(dbtable, colname, template=True)
                col = sqlfunc.cast(col, sqltypes.VARCHAR)
                if irisafe:
                    col = sql_safe(col)
                strings.append(None)
                cols.append(col)

        return strings, cols

    @classmethod
    def _term_map_colmolds(
        cls, graph, dbtable, parent, wheres, mapper, shortcut, obj=False
    ) -> Iterable[ColMold]:
        # TODO: make this yield (strings, cols) tuples
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
                yield [f"'{const.n3()}'"], []
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield [f"'{const.n3()}'"], []
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        colname = graph.value(tmap, rr.column)
                        strings, cols = [None], [cls._get_col(dbtable, colname)]
                        if obj:
                            # for objects, the default term type is Literal
                            termtype = graph.value(tmap, rr.termType) or rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        strings, cols = cls._template_to_colmolds(
                            dbtable, template, irisafe=(termtype == rr.IRI)
                        )
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        ptable = _get_table(graph, ref)
                        # push the where clauses into the subquery
                        joins, wheres[:] = wheres[:], []
                        for join in graph[tmap : rr.joinCondition]:
                            ccol = f'"{dbtable.name}".{graph.value(join, rr.child)}'
                            pcol = f'"{ptable.name}".{graph.value(join, rr.parent)}'
                            joins.append(literal_column(ccol) == literal_column(pcol))
                        referenced_colmolds = cls._term_map_colmolds(
                            graph, ptable, ref, [], rr.subjectMap, rr.subject
                        )
                        for strings, cols in referenced_colmolds:
                            # is this the best way..?
                            cols = [
                                select(c).select_from(ptable).where(*joins).as_scalar()
                                for c in cols
                            ]
                            yield strings, cols
                        continue
                    else:
                        # TODO: replace with RDB-specific construct (postgresql?)
                        rowid = literal_column(f'"{dbtable.name}".rowid').cast(
                            sqltypes.VARCHAR
                        )
                        strings = ["_:" + dbtable.name + "#", None]
                        yield strings, [rowid]
                        continue

                    if termtype == rr.IRI:
                        yield (["<"] + strings + [">"]), cols
                    elif termtype == rr.BlankNode:
                        yield (["_:"] + strings), cols
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            cols = [sqlfunc.cast(c, sqltypes.VARCHAR) for c in cols]
                            yield (['"'] + strings + ['"@' + str(lang)]), cols
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            cols = [sqlfunc.cast(c, sqltypes.VARCHAR) for c in cols]
                            yield (['"'] + strings + ['"^^' + dtype.n3()]), cols
                        else:
                            # keep original datatype
                            yield strings, cols
                    else:
                        yield [None], [literal_column("'_:'")]  # not a real literal

    @staticmethod
    def _combine_colmolds(*colmolds):
        allcols = []
        submold = []
        i = 0
        for strings, cols in colmolds:
            submold.append((range(i, i + len(cols)), strings))
            i += len(cols)
            allcols += cols
        return submold, allcols

    def _triplesmap_select(self, metadata, tmap, pattern) -> Iterable[SelectSubMold]:
        mg = self.mapping.graph

        dbtable = _get_table(mg, tmap)
        if metadata:
            dbtable = metadata.tables.get(dbtable.name, dbtable)

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

        ss = self._term_map_colmolds(
            mg, dbtable, tmap, swhere, rr.subjectMap, rr.subject
        )
        scolmold = next(ss)
        s_map = mg.value(tmap, rr.subjectMap)

        gcolmolds = list(
            self._term_map_colmolds(
                mg, dbtable, s_map, [], rr.graphMap, rr.graph
            )
        ) or [([None],[null()])]

        # Class Map
        if (not pfilt) or (None in pfilt) or (RDF.type == qp):
            for c in mg[s_map : rr["class"]]:
                pcolmold = [f"'{RDF.type.n3()}'"], []
                ocolmold = [f"'{c.n3()}'"], []
                # no unsafe IRI because it should be defined to be safe
                if (qo is not None) and (qo != c):
                    continue
                for gcolmold in gcolmolds:
                    submold, cols = self._combine_colmolds(
                        scolmold, pcolmold, ocolmold, gcolmold
                    )
                    query = select(*cols).select_from(dbtable)
                    if swhere:
                        query = query.where(*swhere)
                    yield query, submold

        # Predicate-Object Maps
        pomaps = set(mg[tmap : rr.predicateObjectMap :])
        if not (None in pfilt):
            pomaps &= set(pfilt)
        if not (None in ofilt):
            pomaps &= set(ofilt)

        for pomap in pomaps:
            pwhere = pfilt.get(pomap) or []
            pcolmolds = self._term_map_colmolds(
                mg, dbtable, pomap, pwhere, rr.predicateMap, rr.predicate
            )
            owhere = ofilt.get(pomap) or []
            ocolmolds = list(
                self._term_map_colmolds(
                    mg, dbtable, pomap, owhere, rr.objectMap, rr.object, True
                )
            )
            gcolmolds = list(
                self._term_map_colmolds(mg, dbtable, pomap, [], rr.graphMap, rr.graph)
            ) or [([None],[null()])]
            for pcolmold in pcolmolds:
                pstrings, pcols = pcolmold
                pstr = "".join(filter(bool, pstrings))
                if (qp is not None) and pstr[1:-1] != qp.n3():
                    # Filter out non-identical property patterns
                    continue
                for ocolmold in ocolmolds:
                    for gcolmold in gcolmolds:
                        where = swhere + pwhere + owhere
                        submold, cols = self._combine_colmolds(
                            scolmold, pcolmold, ocolmold, gcolmold
                        )
                        query = select(*cols).select_from(dbtable)
                        if where:
                            query = query.where(*where)
                        yield query, submold

    @staticmethod
    def col_n3(dbcol):
        """Cast column to n3"""
        if isinstance(dbcol.type, sqltypes.DATE):
            dt = XSD.date.n3()
            n3col = '"' + sqlfunc.cast(dbcol, sqltypes.VARCHAR) + ('"^^' + dt)
            n3col.original = dbcol
            return n3col
        if isinstance(dbcol.type, sqltypes.DATETIME) or isinstance(
            dbcol.type, sqltypes.TIMESTAMP
        ):
            dt = XSD.dateTime.n3()
            value = sqlfunc.replace(sqlfunc.cast(dbcol, sqltypes.VARCHAR), " ", "T")
            n3col = '"' + value + ('"^^' + dt)
            n3col.original = dbcol
            return n3col
        if isinstance(dbcol.type, sqltypes.BOOLEAN):
            dt = XSD.boolean.n3()
            value = sql.expression.case({1: "true", 0: "false"}, value=dbcol)
            n3col = '"' + value + ('"^^' + dt)
            n3col.original = dbcol
            return n3col
        return dbcol

    def queryPattern(self, metadata, pattern, restrict_tmaps=None) -> GenerativeSelectSubMold:
        query_idxstrs: List[SelectSubMold] = []
        # Triple Maps produce select queries
        for tmap in self.mapping.graph[: RDF.type : rr.TriplesMap]:
            if restrict_tmaps and (tmap not in restrict_tmaps):
                continue
            query_idxstrs += list(self._triplesmap_select(metadata, tmap, pattern))

        if len(query_idxstrs) > 1:
            queries = []
            for query, q_submold in query_idxstrs:
                cols = list(query.inner_columns)
                onlycols = []
                assert len(q_submold) == 4 # spog
                for (idxs, strings), name in zip(q_submold, "spog"):
                    col = self._concat_colmold(strings, [cols[i] for i in idxs])
                    onlycols.append( col.label(name) )
                queries.append( query.with_only_columns(*onlycols) )
            submold = [([i], [None]) for i in range(4)] # spog

            # If the object columns have different datatypes, cast them to n3 strings
            # WARNING: In most cases, this should be fine but it might mess up!
            _, _, o_cols, *_ = zip(*[q.inner_columns for q in queries])
            kwargs = lambda c: tuple((k, v) for k, v in vars(c).items() if k[0] != "_")
            o_types = set((c.type.__class__, kwargs(c.type)) for c in o_cols)
            if len(o_types) > 1:
                for qi, query in enumerate(queries):
                    s, p, o, g = query.inner_columns
                    queries[qi] = query.with_only_columns([s, p, self.col_n3(o), g])
            return union_all(*queries), submold
        elif query_idxstrs:
            return query_idxstrs[0]
        else:
            logging.warn(f"Didn't get any tmaps for {pattern} from {restrict_tmaps}!")

    def make_node(self, val):
        isstr = isinstance(val, str)
        if val is None:
            return None
        elif (not isstr) or (val[0] not in '"<_'):
            if type(val) == bytes:
                return Literal(
                    base64.b16encode(val),
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
            if "duckdb" not in type(self.db.dialect).__module__:
                metadata.reflect(self.db)

            query, submold = self.queryPattern(metadata, pattern)
            cols = getattr(query, 'inner_columns', query.c)
            onlycols = []
            for (idxs, mold), colname in zip(submold, "spog"):
                col = self._concat_colmold(mold, [cols[i] for i in idxs])
                onlycols.append( col.label(colname) )
            if isinstance(query, Select):
                query = query.with_only_columns(onlycols)
            else:
                query = select(*onlycols)

            # logging.warn(sql_pretty(query))
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
        patstr = " ".join((n.n3(ns) if n else "_") for n in pattern)
        logging.warn(f"pattern: {patstr}, results: {result_count}")


    ###### SPARQL #######

    def queryBGP(self, conn, bgp) -> GenerativeSelect:
        bgp = set(bgp)

        metadata = MetaData(conn)
        if "duckdb" not in type(self.db.dialect).__module__:
            metadata.reflect(self.db)

        # Optimize DB table restrictions in queries
        mg = self.mapping.graph
        restrict_tmaps = {}
        for qs, qp, qo in bgp:
            if isinstance(qs, Variable):
                restriction = set()
                # Find triple map restrictions based on types
                if (not isinstance(qo, Variable)) and (qp == RDF.type):
                    for tmap in mg[: RDF.type : rr.TriplesMap]:
                        if qo in mg[mg.value(tmap, rr.subjectMap) : rr["class"]]:
                            restriction.add(tmap)
                # Find triple map restrictions based on predicates
                for pomap in mg[: rr.predicate : qp]:
                    for tmap in mg[: rr.predicateObjectMap : pomap]:
                        restriction.add(tmap)
                    for omap in mg[pomap : rr.objectMap]:
                        for tmap in mg[omap : rr.parentTriplesMap]:
                            # recursive ??
                            restriction.add(tmap)
                if restriction:
                    if qs in restrict_tmaps:
                        restrict_tmaps[qs] &= restriction  # intersect per pattern
                    else:
                        restrict_tmaps[qs] = restriction

        # Collect queries and associated query variables; collect simple table selects
        novar = lambda n: n if not isinstance(n, Variable) else None
        query_varsubmold = []
        table_varcolmolds = {}
        for qs, qp, qo in bgp:
            restriction = restrict_tmaps.get(qs)
            pat = novar(qs), novar(qp), novar(qo)
            
            # TODO: node mold stuff here!
            pat_query, submold = self.queryPattern(metadata, pat, restriction)
            logging.warn(sql_pretty(pat_query))
            logging.warn(submold)
            if isinstance(pat_query, Select):
                cols = list(pat_query.inner_columns)
                qvar_colmold = [
                    (q, (tuple(s), tuple(cols[i] for i in ixs) ) )
                    for (ixs,s),q in zip(submold, (qs, qp, qo)) 
                    if isinstance(q, Variable)
                ]
                if len(pat_query._from_obj) == 1:
                    table = pat_query._from_obj[0]
                    table_varcolmolds.setdefault(table, set()).update(qvar_colmold)
                    continue
                
                qvars, colmolds = zip(*qvar_colmold)
                submold, allcols = self._combine_colmolds(*colmolds)
                pat_query = pat_query.with_only_columns(allcols)
                qvar_submold = zip(qvars, submold)
            else:
                qvar_submold = [(q,i) for q,i in zip(pat, submold) if q != None]
            query_varsubmold.append( (pat_query, qvar_submold) )

        # Merge simple select statements on same table
        for table, var_colmolds in table_varcolmolds.items():
            qvars, colmolds = zip(*dict(var_colmolds).items())
            submold, allcols = self._combine_colmolds(*colmolds)
            query = select(*[col.label(str(var)) for var, col in zip(qvars, allcols)])
            query_varsubmold.append( (query, zip(qvars, submold)) )

        # Collect colmolds per variable
        var_colmolds = {}
        for query, varsubmold in query_varsubmold:
            subquery = query.subquery()
            incols = list(subquery.c)
            for var, (idx, mold) in varsubmold:
                cols = [incols[i] for i in idx]
                var_colmolds.setdefault(var, []).append( (mold, cols) )

        # Simplify colmold equalities
        submold, allcols = self._combine_colmolds(*colmolds)
        sel = [self._concat_colmold(*cs[0]).label(str(v)) for v, cs in var_colmolds.items()]
        where = [eq for cs in var_colmolds.values() for eq in self.colmold_equal(*cs)]
        return select(*sel).where(*where)

    def colmold_equal(self, *colmolds):
        if colmolds:
            (mold_0, cols_0), *cs = colmolds
            result_0 = self._concat_colmold(mold_0, cols_0)
            for mold, cols in cs:
                if tuple(mold_0) == tuple(mold):
                    for c0, c in zip(cols_0, cols):
                        yield c0 == c
                else:
                    result = self._concat_colmold(mold, cols)
                    yield result_0 == result

    def queryExpr(self, conn, expr, var_col) -> ColumnElement:
        if hasattr(expr, "name") and (expr.name == "RelationalExpression"):
            a = self.queryExpr(conn, expr.expr, var_col)
            b = self.queryExpr(conn, expr.other, var_col)
            op = sql.operators.custom_op(expr.op, is_comparison=True)
            return op(a, b)
        if hasattr(expr, "name") and (expr.name == "MultiplicativeExpression"):
            # TODO: ternary ops?
            a = self.queryExpr(conn, expr.expr, var_col)
            for other in expr.other:
                b = self.queryExpr(conn, other, var_col)
                op = sql.operators.custom_op(*expr.op, is_comparison=True)
                return op(a, b)
        if hasattr(expr, "name") and (expr.name == "ConditionalAndExpression"):
            exprs = [self.queryExpr(conn, e, var_col) for e in [expr.expr] + expr.other]
            return sql_and(*exprs)
        if hasattr(expr, "name") and (expr.name == "ConditionalOrExpression"):
            exprs = [self.queryExpr(conn, e, var_col) for e in [expr.expr] + expr.other]
            return sql_or(*exprs)
        if hasattr(expr, "name") and (expr.name == "Function"):
            # TODO: it would be super cool to do UDFs here
            if expr.iri in XSDToSQL:
                for e in expr.expr:
                    val = self.queryExpr(conn, e, var_col)
                    return sqlfunc.cast(val, XSDToSQL[expr.iri])

        if isinstance(expr, str) and (expr in var_col):
            return var_col[expr]
        if isinstance(expr, URIRef):
            return expr.n3()
        if isinstance(expr, Literal):
            return expr.toPython()
        if isinstance(expr, str):
            return from_n3(expr).toPython()

        # logging.warn(("Expr not implemented:", getattr(expr, "name", None), expr))
        raise SparqlNotImplementedError

    def queryFilter(self, conn, part) -> GenerativeSelect:
        part_query = self.queryPart(conn, part.p)

        if getattr(part.expr, "name", None) == "Builtin_NOTEXISTS":
            # This is weird, but I guess that's how it is
            query2 = self.queryPart(conn, part.expr.graph)
            var_cols = {}
            for c in list(query2.inner_columns) + list(part_query.inner_columns):
                var_cols.setdefault(c.name, []).append(c)
            where = [
                c0 == c
                for (c0, *cs) in var_cols.values() 
                for c in cs
            ]
            return part_query.filter(~query2.where(*where).exists())

        var_col = {Variable(c.key): c for c in part_query.inner_columns}
        clause = self.queryExpr(conn, part.expr, var_col)

        # Filter should be HAVING for aggregates
        if part.p.name == "AggregateJoin":
            return part_query.having(clause)
        else:
            return part_query.where(clause)

    def queryJoin(self, conn, part) -> GenerativeSelect:
        query1 = self.queryPart(conn, part.p1)
        query2 = self.queryPart(conn, part.p2)
        if not query1.c:
            return query2
        if not query2.c:
            return query1
        var_cols = {}
        for c in list(query1.c) + list(query2.c):
            var_cols.setdefault(c.name, []).append(c)
        sel = [cs[0].label(str(v)) for v, cs in var_cols.items()]
        where = [(c0 == c) for (c0, *cs) in var_cols.values() for c in cs]
        return select(*sel).where(*where)

    def queryAggregateJoin(self, conn, agg) -> Select:
        funcs = {
            "Aggregate_Count": sqlfunc.count,
            "Aggregate_Sample": lambda x: x,
            "Aggregate_Sum": sqlfunc.sum,
            "Aggregate_Avg": sqlfunc.avg,
            "Aggregate_Min": sqlfunc.min,
            "Aggregate_Max": sqlfunc.max,
            "Aggregate_GroupConcat": sqlfunc.group_concat_node,
        }
        # Assume agg.p is always a Group
        group_expr, group_part = agg.p.expr, agg.p.p
        part_query = self.queryPart(conn, group_part)

        # CompoundSelect objects are different
        cols = list(getattr(part_query, "inner_columns", part_query.c))
        var_col = {Variable(c.key): c for c in cols}

        # Get aggregate column expressions
        cols = []
        for a in agg.A:
            func = funcs.get(a.name)
            expr = self.queryExpr(conn, a.vars, var_col)
            col = func(expr).label(str(a.res))
            cols.append(col)
        groups = [self.queryExpr(conn, e, var_col) for e in group_expr]

        # CompoundSelect objects are different
        if isinstance(part_query, Select):
            return part_query.group_by(*groups).with_only_columns(cols)
        else:
            return select(*cols).group_by(*groups)

    def queryExtend(self, conn, part) -> Select:
        part_query = self.queryPart(conn, part.p)
        cols = list(part_query.inner_columns)
        var_col = {Variable(c.key): c for c in cols}
        cols += [self.queryExpr(conn, part.expr, var_col).label(str(part.var))]
        return part_query.with_only_columns(cols)

    def queryProject(self, conn, part) -> Select:
        part_query = self.queryPart(conn, part.p)
        cols = list(part_query.inner_columns)
        var_col = {Variable(c.key): c for c in cols}
        cols = [self.queryExpr(conn, c, var_col) for c in part.PV]
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
        if part.name == "Minus":
            q1 = self.queryPart(conn, part.p1)
            q2 = self.queryPart(conn, part.p2)
            return q1.except_(q2)
        if part.name == "Distinct":
            return self.queryPart(conn, part.p).distinct()

        # logging.warn(("Part not implemented:", part))
        raise SparqlNotImplementedError

    def exec(self, query):
        with self.db.connect() as conn:
            logging.warn(sql_pretty(query))

            raise Exception

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
