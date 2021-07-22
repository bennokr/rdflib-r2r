"""
rdflib_r2r.r2r_store
=======================

TODO:
- delay the UNION creation longer, so that we can use colforms to filter them
    - This is SUPER complicated because you'd need to explode the BGPs 
        because each triple pattern becomes a set of selects, which you'd need to join

"""
from os import linesep
from typing import Iterable, List, Tuple, Union, Dict
import logging
import functools
import operator
import base64
import urllib.parse
import re
from string import Formatter
from collections import Counter

from rdflib import URIRef, Literal, BNode, Variable
from rdflib.namespace import RDF, XSD, Namespace
from rdflib.store import Store
from rdflib.util import from_n3

import sqlalchemy
from sqlalchemy import MetaData, select, text, null, literal_column, literal
from sqlalchemy import union_all, or_ as sql_or, and_ as sql_and
from sqlalchemy import types as sqltypes, func as sqlfunc
import sqlalchemy.sql as sql
from sqlalchemy.sql.expression import ColumnElement, GenerativeSelect, Select, TableClause
from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.selectable import ScalarSelect

FormStrings = Tuple[Union[str, bool]]  # booleans indicate SQL escaping of columns
SubForm = Tuple[Iterable[int], FormStrings]
SelectSubForm = Tuple[Select, List[SubForm]]
GenerativeSelectSubForm = Tuple[GenerativeSelect, List[SubForm]]


class ColForm:
    """A template object for creating SQL expressions that represent RDF nodes.

    Because the columns are separated from the template, this allows for efficient
    joins, filters, and aggregates.

    The `form` and `cols` list are combined by replacing non-strings in `form` by
    elements of `cols` sequentially.
    """

    form: FormStrings
    cols: Tuple[ColumnElement]

    def __init__(self, form, cols):
        self.form, self.cols = tuple(form), tuple(cols)

    def __hash__(self):
        return hash((self.form, self.cols))

    def __repr__(self):
        return f"ColForm({self.form}, {self.cols})"

    def expr(self):
        if self.cols == ():
            return literal_column("".join(self.form))
        if list(self.form) == [None]:
            return self.cols[0]
        cols = list(self.cols)
        parts = []
        for s in self.form:
            if s in [True, None, False]:
                col = sqlfunc.cast(cols.pop(0), sqltypes.VARCHAR)
                # non-string values indicate whether to escape URI terms
                part = sql_safe(col) if s else col
            else:
                part = literal(s)
            parts.append(part)
        return functools.reduce(operator.add, parts)

    @classmethod
    def from_template(cls, dbtable, template, irisafe=False) -> "ColForm":
        # make python format string: escape curly braces by doubling {{ }}
        template = re.sub("\\\\[{}]", lambda x: x.group(0)[1] * 2, template)

        form, cols = [], []
        for prefix, colname, _, _ in Formatter().parse(template):
            if prefix != "":
                form.append(prefix)
            if colname:
                col = _get_col(dbtable, colname, template=True)
                form.append(irisafe)  # sorry not sorry
                cols.append(col)

        return cls(form, cols)

    @classmethod
    def from_subform(cls, cols, subform):
        cols = list(cols)
        idxs, form = subform
        return cls(form, [cols[i] for i in idxs])

    @classmethod
    def from_expr(cls, expr):
        return cls([None], [expr])

    @classmethod
    def null(cls):
        return cls.from_expr(null())

    @staticmethod
    def to_subforms_columns(*colforms) -> Tuple[List[SubForm], List[ColumnElement]]:
        subforms, allcols = [], []
        i = 0
        for cf in colforms:
            cols = [c for c in cf.cols if type(c) != str]
            if cf.form:
                subforms.append((range(i, i + len(cols)), cf.form))
                i += len(cols)
                allcols += list(cols)
        return subforms, allcols

    @staticmethod
    def equal(*colforms, eq=True):
        if colforms:
            # Sort colforms by descending frequency of form (for efficient equalities)
            form_count = Counter(cf.form for cf in colforms)
            colforms = sorted(colforms, key=lambda cf: -form_count[cf.form])

            cf0, *cfs = colforms
            expr0 = cf0.expr()
            for cf in cfs:
                if tuple(cf0.form) == tuple(cf.form):
                    for c0, c in zip(cf0.cols, cf.cols):
                        yield (c0 == c) if eq else (c0 != c)
                else:
                    logging.warn(f"Cannot reduce {cf0} and {cf}")
                    # TODO: fancy prefix checking
                    yield (expr0 == cf.expr()) if eq else (expr0 != cf.expr())

    @classmethod
    def op(cls, opstr, cf1, cf2):
        if opstr in ["=", "=="]:
            return cls.from_expr(sql_and(*cls.equal(cf1, cf2)))
        elif opstr in ["!=", "<>"]:
            return cls.from_expr(sql_or(*cls.equal(cf1, cf2, eq=False)))
        elif opstr == "/":
            op = sql.operators.custom_op(opstr, is_comparison=True)
            a, b = cf1.expr(), cf2.expr()
            r = sqlfunc.cast(op(a, b), sqltypes.FLOAT)
            return cls.from_expr(r)
        else:
            op = sql.operators.custom_op(opstr, is_comparison=True)
            # TODO: fancy type casting
            return cls.from_expr(op(cf1.expr(), cf2.expr()))


SelectVarSubForm = Tuple[Select, Dict[Variable, SubForm]]


class SparqlNotImplementedError(NotImplementedError):
    pass


from sqlalchemy.engine import Engine

from rdflib_r2r.types import Any, Optional, Triple
from rdflib_r2r.r2r_mapping import R2RMapping, _get_table, iri_safe, _get_col

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

    @classmethod
    def _term_map_colforms(
        cls, graph, meta, dbtable, parent, wheres, mapper, shortcut, obj=False
    ) -> Iterable[ColForm]:
        """For each Triples Map, yield a expression template containing table columns.

        Args:
            graph (Graph): The RDF2RDB mapping graph
            dbtable (TableClause): The database table for this mapping
            parent (Identifier): The parent of this mapping
            wheres (Iterable[BooleanClause]): SQL clauses for restriction
            mapper (URIRef): Mapping predicate
            shortcut (URIRef): Mapping shortcut predicate
            obj (bool): Whether this term is in the object position. Defaults to False.

        Yields:
            ColForm: Expression Templates
        """
        if graph.value(parent, shortcut):
            # constant shortcut properties
            for const in graph[parent:shortcut]:
                yield ColForm([f"'{const.n3()}'"], [])
        elif graph.value(parent, mapper):
            for tmap in graph[parent:mapper]:
                if graph.value(tmap, rr.constant):
                    # constant value
                    for const in graph[tmap : rr.constant]:
                        yield ColForm([f"'{const.n3()}'"], [])
                else:
                    termtype = graph.value(tmap, rr.termType) or rr.IRI
                    if graph.value(tmap, rr.column):
                        colname = graph.value(tmap, rr.column)
                        colform = ColForm.from_expr(_get_col(dbtable, colname))
                        if obj:
                            # for objects, the default term type is Literal
                            termtype = graph.value(tmap, rr.termType) or rr.Literal
                    elif graph.value(tmap, rr.template):
                        template = graph.value(tmap, rr.template)
                        colform = ColForm.from_template(
                            dbtable, template, irisafe=(termtype == rr.IRI)
                        )
                    elif graph.value(tmap, rr.parentTriplesMap):
                        # referencing object map
                        ref = graph.value(tmap, rr.parentTriplesMap)
                        ptable = _get_table(graph, ref, meta=meta)
                        # push the where clauses into the subquery
                        #joins, wheres[:] = wheres[:], []
                        joins = wheres
                        for join in graph[tmap : rr.joinCondition]:
                            ccol = _get_col(dbtable, graph.value(join, rr.child))
                            pcol = _get_col(ptable, graph.value(join, rr.parent))
                            joins.append(literal_column(ccol) == literal_column(pcol))
                        yield from cls._term_map_colforms(
                            graph, meta, ptable, ref, [], rr.subjectMap, rr.subject
                        )
                        continue
                    else:
                        # TODO: replace with RDB-specific construct (postgresql?)
                        rowid = _get_col(dbtable, 'rowid').cast(
                            sqltypes.VARCHAR
                        )
                        t = getattr(dbtable, 'original', dbtable)
                        form = ["_:" + t.name + "#", None]
                        yield ColForm(form, [rowid])
                        continue

                    if termtype == rr.IRI:
                        form = ["<"] + list(colform.form) + [">"]
                        yield ColForm(form, colform.cols)
                    elif termtype == rr.BlankNode:
                        yield ColForm((["_:"] + list(colform.form)), colform.cols)
                    elif obj:
                        if graph.value(tmap, rr.language):
                            lang = graph.value(tmap, rr.language)
                            cols = [
                                sqlfunc.cast(c, sqltypes.VARCHAR) for c in colform.cols
                            ]
                            form = ['"'] + list(colform.form) + ['"@' + str(lang)]
                            yield ColForm(form, cols)
                        elif graph.value(tmap, rr.datatype):
                            dtype = graph.value(tmap, rr.datatype)
                            cols = [
                                sqlfunc.cast(c, sqltypes.VARCHAR) for c in colform.cols
                            ]
                            form = ['"'] + list(colform.form) + ['"^^' + dtype.n3()]
                            yield ColForm(form, cols)
                        else:
                            # keep original datatype
                            yield colform
                    else:
                        # not a real literal
                        yield ColForm.from_expr(literal_column("'_:'"))

    def _triplesmap_select(self, metadata, tmap, pattern) -> Iterable[SelectSubForm]:
        mg = self.mapping.graph

        dbtable = _get_table(mg, tmap, meta=metadata)

        qs, qp, qo = pattern
        s_tm_filter = self.mapping.get_filters(qs, dbtable, self.mapping.spat_tmaps)
        p_tm_filter = self.mapping.get_filters(qp, dbtable, self.mapping.ppat_pomaps)
        o_tm_filter = self.mapping.get_filters(qo, dbtable, self.mapping.opat_pomaps)

        swhere = []
        if not (None in s_tm_filter):
            if not (tmap in s_tm_filter):
                return
            else:
                swhere = s_tm_filter[tmap]

        ss = self._term_map_colforms(
            mg, metadata, dbtable, tmap, swhere, rr.subjectMap, rr.subject
        )
        scolform = next(ss)
        s_map = mg.value(tmap, rr.subjectMap)

        gcolforms = list(
            self._term_map_colforms(mg, metadata, dbtable, s_map, [], rr.graphMap, rr.graph)
        ) or [ColForm.null()]

        # Class Map
        if (not p_tm_filter) or (None in p_tm_filter) or (RDF.type == qp):
            for c in mg[s_map : rr["class"]]:
                pcolform = ColForm([f"'{RDF.type.n3()}'"], [])
                ocolform = ColForm([f"'{c.n3()}'"], [])
                # no unsafe IRI because it should be defined to be safe
                if (qo is not None) and (qo != c):
                    continue
                for gcolform in gcolforms:
                    subforms, cols = ColForm.to_subforms_columns(
                        scolform, pcolform, ocolform, gcolform
                    )
                    tables = [c.table for c in cols if isinstance(c, Column)]
                    query = select(*cols).select_from(*tables)
                    if swhere:
                        query = query.where(*swhere)
                    yield query, subforms

        # Predicate-Object Maps
        pomaps = set(mg[tmap : rr.predicateObjectMap :])
        if not (None in p_tm_filter):
            pomaps &= set(p_tm_filter)
        if not (None in o_tm_filter):
            pomaps &= set(o_tm_filter)

        for pomap in pomaps:
            pwhere = p_tm_filter.get(pomap) or []
            pcolforms = self._term_map_colforms(
                mg, metadata, dbtable, pomap, pwhere, rr.predicateMap, rr.predicate
            )
            owhere = o_tm_filter.get(pomap) or []
            ocolforms = list(
                self._term_map_colforms(
                    mg, metadata, dbtable, pomap, owhere, rr.objectMap, rr.object, True
                )
            )
            gcolforms = list(
                self._term_map_colforms(mg, metadata, dbtable, pomap, [], rr.graphMap, rr.graph)
            ) or [ColForm.null()]
            for pcolform in pcolforms:
                pstr = "".join(filter(bool, pcolform.form))
                if (qp is not None) and pstr[1:-1] != qp.n3():
                    # Filter out non-identical property patterns
                    continue
                for ocolform in ocolforms:
                    for gcolform in gcolforms:
                        where = swhere + pwhere + owhere
                        subforms, cols = ColForm.to_subforms_columns(
                            scolform, pcolform, ocolform, gcolform
                        )
                        tables = [c.table for c in cols if isinstance(c, Column)]
                        query = select(*cols).select_from(*tables)
                        if where:
                            query = query.where(*where)
                        yield query, subforms

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

    def union_spog_querysubforms(self, *queryforms) -> GenerativeSelectSubForm:
        queries = []
        # Make expressions from ColForms
        for query, q_subforms in queryforms:
            cols = list(query.inner_columns)
            onlycols = []
            assert len(q_subforms) == 4  # spog
            for subform, name in zip(q_subforms, "spog"):
                col = ColForm.from_subform(cols, subform).expr()
                onlycols.append(col.label(name))
            queries.append(query.with_only_columns(*onlycols))
        subforms = [([i], [None]) for i in range(4)]  # spog

        # If the object columns have different datatypes, cast them to n3 strings
        # WARNING: In most cases, this should be fine but it might mess up!
        _, _, o_cols, *_ = zip(*[q.inner_columns for q in queries])
        kwargs = lambda c: tuple((k, v) for k, v in vars(c).items() if k[0] != "_")
        o_types = set((c.type.__class__, kwargs(c.type)) for c in o_cols)
        if len(o_types) > 1:
            for qi, query in enumerate(queries):
                s, p, o, g = query.inner_columns
                queries[qi] = query.with_only_columns([s, p, self.col_n3(o), g])
        return union_all(*queries), subforms

    def queryPattern(
        self, metadata, pattern, restrict_tmaps=None
    ) -> GenerativeSelectSubForm:
        querysubforms: List[SelectSubForm] = []
        # Triple Maps produce select queries
        for tmap in self.mapping.graph[: RDF.type : rr.TriplesMap]:
            if restrict_tmaps and (tmap not in restrict_tmaps):
                continue
            querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))

        if len(querysubforms) > 1:
            return self.union_spog_querysubforms(*querysubforms)
        elif querysubforms:
            return querysubforms[0]
        else:
            raise Exception(f"Didn't get tmaps for {pattern} from {restrict_tmaps}!")
            

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

            query, subforms = self.queryPattern(metadata, pattern)
            cols = getattr(query, "inner_columns", query.c)
            onlycols = []
            for subform, colname in zip(subforms, "spog"):
                col = ColForm.from_subform(cols, subform).expr()
                onlycols.append(col.label(colname))
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
                if any(r is None for r in result):
                    logging.warn(f"none in result: {result}")
                result_count += 1
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
        if not metadata:
            logging.warn(f"Could not get metadata for {self.db}")

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
                    # Other triple maps that share this pred-obj map
                    for tmap in mg[: rr.predicateObjectMap : pomap]:
                        restriction.add(tmap)
                    # Referenced triple maps
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
        query_varsubforms = []
        table_varcolforms = {}
        for qs, qp, qo in bgp:
            restriction = restrict_tmaps.get(qs)
            pat = novar(qs), novar(qp), novar(qo)

            # Keep track of which columns belong to which query variable
            pat_query, subforms = self.queryPattern(metadata, pat, restriction)
            if isinstance(pat_query, Select):
                # Restrict selected terms from pattern query to query variables
                cols = list(pat_query.inner_columns)
                qvar_colform = [
                    (q, ColForm.from_subform(cols, subform))
                    for q, subform in zip((qs, qp, qo), subforms)
                    if isinstance(q, Variable)
                ]
                if len(pat_query._from_obj) == 1:
                    # Single table, so try to merge shared-subject terms
                    # Though keep the referenced triple maps around because they filter
                    refs = tuple(c for c in cols if isinstance(c, ScalarSelect))
                    table = pat_query._from_obj[0], refs, pat_query.whereclause
                    table_varcolforms.setdefault(table, set()).update(qvar_colform)
                    continue

                qvars, colforms = zip(*qvar_colform)
                subforms, allcols = ColForm.to_subforms_columns(*colforms)
                pat_query = pat_query.with_only_columns(allcols)
                qvar_subform = zip(qvars, subforms)
            else:
                qvar_subform = [
                    (q, subform)
                    for q, subform in zip((qs, qp, qo), subforms)
                    if isinstance(q, Variable)
                ]
            query_varsubforms.append((pat_query, qvar_subform))

        # Merge simple select statements on same table
        for (table, refs, where), var_colforms in table_varcolforms.items():
            qvars, colforms = zip(*dict(var_colforms).items())
            subform, allcols = ColForm.to_subforms_columns(*colforms)
            cols = [col.label(str(var)) for var, col in zip(qvars, allcols)]
            cols += [r for r in refs if r not in allcols]
            query = select(*cols).select_from(table)
            if where is not None:
                query = query.where(where)
            query_varsubforms.append((query, zip(qvars, subform)))

        # Collect colforms per variable
        var_colforms = {}
        for query, var_subform in query_varsubforms:
            subquery = query.subquery()
            incols = list(subquery.c)
            for var, (idx, form) in var_subform:
                cols = [incols[i] for i in idx]
                var_colforms.setdefault(var, []).append(ColForm(form, cols))

        # Simplify colform equalities
        colforms = [cfs[0] for cfs in var_colforms.values()]
        subforms, allcols = ColForm.to_subforms_columns(*colforms)
        where = [eq for cs in var_colforms.values() for eq in ColForm.equal(*cs)]
        return select(*allcols).where(*where), dict(zip(var_colforms, subforms))

    def queryExpr(self, conn, expr, var_cf) -> ColForm:
        # this all could get really complicated with expression types...
        agg_funcs = {
            "Aggregate_Sample": lambda x: x,
            "Aggregate_Count": sqlfunc.count,
            "Aggregate_Sum": sqlfunc.sum,
            "Aggregate_Avg": sqlfunc.avg,
            "Aggregate_Min": sqlfunc.min,
            "Aggregate_Max": sqlfunc.max,
            "Aggregate_GroupConcat": sqlfunc.group_concat_node,
        }
        if hasattr(expr, "name") and (expr.name in agg_funcs):
            sub = self.queryExpr(conn, expr.vars, var_cf)
            if expr.name == "Aggregate_Sample":
                return sub
            func = agg_funcs[expr.name]
            if (len(sub.cols) == 1) and (expr.name == "Aggregate_Count"):
                # Count queries don't need full node expression
                return ColForm.from_expr(func(sub.cols[0]))
            else:
                return ColForm.from_expr(func(sub.expr()))

        if hasattr(expr, "name") and (expr.name == "RelationalExpression"):
            a = self.queryExpr(conn, expr.expr, var_cf)
            b = self.queryExpr(conn, expr.other, var_cf)
            return ColForm.op(expr.op, a, b)

        math_expr_names = ["MultiplicativeExpression", "AdditiveExpression"]
        if hasattr(expr, "name") and (expr.name in math_expr_names):
            # TODO: ternary ops?
            a = self.queryExpr(conn, expr.expr, var_cf)
            for other in expr.other:
                b = self.queryExpr(conn, other, var_cf)
                return ColForm.op(expr.op[0], a, b)

        if hasattr(expr, "name") and (expr.name == "ConditionalAndExpression"):
            exprs = [self.queryExpr(conn, e, var_cf) for e in [expr.expr] + expr.other]
            return ColForm.from_expr(sql_and(*[e.expr() for e in exprs]))

        if hasattr(expr, "name") and (expr.name == "ConditionalOrExpression"):
            exprs = [self.queryExpr(conn, e, var_cf) for e in [expr.expr] + expr.other]
            return ColForm.from_expr(sql_or(*[e.expr() for e in exprs]))

        if hasattr(expr, "name") and (expr.name == "Function"):
            # TODO: it would be super cool to do UDFs here
            if expr.iri in XSDToSQL:
                for e in expr.expr:
                    cf = self.queryExpr(conn, e, var_cf)
                    val = sqlfunc.cast(cf.expr(), XSDToSQL[expr.iri])
                    return ColForm.from_expr(val)

        if isinstance(expr, str) and (expr in var_cf):
            return var_cf[expr]
        if isinstance(expr, URIRef):
            return ColForm.from_expr(expr.n3())
        if isinstance(expr, Literal):
            return ColForm.from_expr(expr.toPython())
        if isinstance(expr, str):
            return ColForm.from_expr(from_n3(expr).toPython())

        e = f'Expr not implemented: {getattr(expr, "name", None).__repr__()} {expr}'
        raise SparqlNotImplementedError(e)

    def queryFilter(self, conn, part) -> Select:
        part_query, var_subform = self.queryPart(conn, part.p)

        if getattr(part.expr, "name", None) == "Builtin_NOTEXISTS":
            # This is weird, but I guess that's how it is
            query2, var_subform2 = self.queryPart(conn, part.expr.graph)

            var_colforms = {}
            cols1 = list(part_query.inner_columns)
            for v, sf1 in var_subform.items():
                var_colforms.setdefault(v, []).append(ColForm.from_subform(cols1, sf1))
            cols2 = list(query2.inner_columns)
            for v, sf2 in var_subform2.items():
                var_colforms.setdefault(v, []).append(ColForm.from_subform(cols2, sf2))

            where = [eq for cs in var_colforms.values() for eq in ColForm.equal(*cs)]
            return part_query.filter(~query2.where(*where).exists()), var_subform

        cols = list(getattr(part_query, "inner_columns", part_query.c))
        var_cf = {v: ColForm.from_subform(cols, sf) for v, sf in var_subform.items()}
        clause = self.queryExpr(conn, part.expr, var_cf).expr()

        # Filter should be HAVING for aggregates
        if part.p.name == "AggregateJoin":
            return part_query.having(clause), var_subform
        else:
            return part_query.where(clause), var_subform

    def queryJoin(self, conn, part) -> Select:
        query1, var_subform1 = self.queryPart(conn, part.p1)
        query2, var_subform2 = self.queryPart(conn, part.p2)
        if not query1.c:
            return query2, var_subform2
        if not query2.c:
            return query1, var_subform1

        var_colforms = {}
        cols1 = list(query1.c)
        for v, sf1 in var_subform1.items():
            var_colforms.setdefault(v, []).append(ColForm.from_subform(cols1, sf1))
        cols2 = list(query2.c)
        for v, sf2 in var_subform2.items():
            var_colforms.setdefault(v, []).append(ColForm.from_subform(cols2, sf2))

        colforms = [cfs[0] for cfs in var_colforms.values()]
        subforms, allcols = ColForm.to_subforms_columns(*colforms)
        where = [eq for cs in var_colforms.values() for eq in ColForm.equal(*cs)]
        return select(*allcols).where(*where), dict(zip(var_colforms, subforms))

    def queryAggregateJoin(self, conn, agg) -> SelectVarSubForm:
        # Assume agg.p is always a Group
        group_expr, group_part = agg.p.expr, agg.p.p
        part_query, var_subform = self.queryPart(conn, group_part)
        cols = list(getattr(part_query, "inner_columns", part_query.c))
        var_cf = {v: ColForm.from_subform(cols, sf) for v, sf in var_subform.items()}

        # Get aggregate column expressions
        var_agg = {a.res: self.queryExpr(conn, a, var_cf) for a in agg.A}
        groups = [
            c
            for e in (group_expr or [])
            for c in self.queryExpr(conn, e, var_cf).cols
            if type(c) != str
        ]

        subforms, allcols = ColForm.to_subforms_columns(*var_agg.values())
        if isinstance(part_query, Select):
            query = part_query.group_by(*groups).with_only_columns(allcols)
        else:
            query = select(*allcols).group_by(*groups)
        return query, dict(zip(var_agg, subforms))

    def queryExtend(self, conn, part) -> SelectVarSubForm:
        part_query, var_subform = self.queryPart(conn, part.p)
        assert isinstance(part_query, Select)  # ?
        cols = list(part_query.inner_columns)
        var_cf = {v: ColForm.from_subform(cols, sf) for v, sf in var_subform.items()}

        cf = self.queryExpr(conn, part.expr, var_cf)
        idxs = []
        for c in cf.cols:
            if c in cols:
                idxs.append(cols.index(c))
            else:
                idxs.append(len(cols))
                cols.append(c)

        var_subform[part.var] = (idxs, cf.form)

        return part_query.with_only_columns(cols + list(cf.cols)), var_subform

    def queryProject(self, conn, part) -> SelectVarSubForm:
        part_query, var_subform = self.queryPart(conn, part.p)
        var_subform = {v: sf for v, sf in var_subform.items() if v in part.PV}
        cols = list(part_query.inner_columns)
        colforms = [ColForm.from_subform(cols, sf) for sf in var_subform.values()]
        subforms, allcols = ColForm.to_subforms_columns(*colforms)
        part_query = part_query.with_only_columns(allcols)
        return part_query, dict(zip(var_subform, subforms))

    def queryOrderBy(self, conn, part) -> SelectVarSubForm:
        part_query, var_subform = self.queryPart(conn, part.p)
        cols = list(part_query.inner_columns)
        var_cf = {v: ColForm.from_subform(cols, sf) for v, sf in var_subform.items()}

        ordering = []
        for e in part.expr:
            for col in self.queryExpr(conn, e.expr, var_cf).cols:
                if e.order == "DESC":
                    col = sqlalchemy.desc(col)
                ordering.append(col)

        return part_query.order_by(*ordering), var_subform

    def queryUnion(self, conn, part) -> SelectVarSubForm:
        query1, var_subform1 = self.queryPart(conn, part.p1)
        query2, var_subform2 = self.queryPart(conn, part.p2)

        all_vars = set(var_subform1) | set(var_subform2)

        cols1, cols2 = list(query1.c), list(query2.c)
        allcols1, allcols2 = [], []
        var_sf = {}
        for i, v in enumerate(all_vars):
            # TODO: if forms are identical, don't convert to expression
            var_sf[v] = [i], [None]
            if v in var_subform1:
                e1 = ColForm.from_subform(cols1, var_subform1[v]).expr()
            else:
                e1 = null()
            allcols1.append(e1.label(str(v)))
            if v in var_subform2:
                e2 = ColForm.from_subform(cols2, var_subform2[v]).expr()
            else:
                e2 = null()
            allcols2.append(e2.label(str(v)))
        query1 = select(*allcols1)
        query2 = select(*allcols2)
        return union_all(query1, query2), var_sf

    def querySlice(self, conn, part) -> SelectVarSubForm:
        query, var_subform = self.queryPart(conn, part.p)
        if part.start:
            query = query.offset(part.start)
        if part.length:
            query = query.limit(part.length)
        return query, var_subform

    def queryLeftJoin(self, conn, part) -> SelectVarSubForm:
        query1, var_subform1 = self.queryPart(conn, part.p1)
        query2, var_subform2 = self.queryPart(conn, part.p2)
        if not query1.c:
            return query2, var_subform2
        if not query2.c:
            return query1, var_subform1

        var_colforms = {}
        cols1 = list(query1.c)
        for v, sf1 in var_subform1.items():
            var_colforms.setdefault(v, []).append(ColForm.from_subform(cols1, sf1))
        cols2 = list(query2.c)
        for v, sf2 in var_subform2.items():
            var_colforms.setdefault(v, []).append(ColForm.from_subform(cols2, sf2))

        colforms = [cfs[0] for cfs in var_colforms.values()]
        subforms, allcols = ColForm.to_subforms_columns(*colforms)
        where = [eq for cs in var_colforms.values() for eq in ColForm.equal(*cs)]
        onclause = sql_and(*where)
        fromquery = query1.join(query2, onclause=onclause, isouter=True)
        query = select(*allcols).select_from(fromquery)
        return query, dict(zip(var_colforms, subforms))

    def queryPart(self, conn, part) -> SelectVarSubForm:
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
            q1, v1 = self.queryPart(conn, part.p1)
            q2, _ = self.queryPart(conn, part.p2)
            return q1.except_(q2), v1
        if part.name == "Distinct":
            query, var_subform = self.queryPart(conn, part.p)
            return query.distinct(), var_subform
        if part.name == "OrderBy":
            return self.queryOrderBy(conn, part)
        if part.name == "Union":
            return self.queryUnion(conn, part)
        if part.name == "Slice":
            return self.querySlice(conn, part)
        if part.name == "LeftJoin":
            return self.queryLeftJoin(conn, part)

        if part.name == "SelectQuery":
            return self.queryPart(conn, part.p)

        e = f"Sparql part not implemented:{part}"
        raise SparqlNotImplementedError(e)

    def exec(self, query):
        with self.db.connect() as conn:
            logging.warn(sql_pretty(query))

            # raise Exception

            results = conn.execute(query)
            rows = list(results)
            keys = [Variable(v) for v in results.keys()]
            logging.warn(f"Got {len(rows)} rows of {keys}")
            first = True
            for vals in rows:
                if first:
                    logging.warn(f"First row: {vals}")
                    first = False
                yield dict(zip(keys, [self.make_node(v) for v in vals]))

    @staticmethod
    def _apply_subforms(query, var_subform):
        if isinstance(query, Select):
            cols = [
                ColForm.from_subform(query.inner_columns, sf).expr().label(str(var))
                for var, sf in var_subform.items()
            ]
            return query.with_only_columns(cols)
        else:
            cols = [
                ColForm.from_subform(query.c, sf).expr().label(str(var))
                for var, sf in var_subform.items()
            ]
            return select(*cols)

    def evalPart(self, part):
        with self.db.connect() as conn:
            query, var_subform = self.queryPart(conn, part)
            query = self._apply_subforms(query, var_subform)
        return self.exec(query)

    def getSQL(self, sparqlQuery, base=None, initNs={}):
        from rdflib.plugins.sparql.parser import parseQuery
        from rdflib.plugins.sparql.algebra import translateQuery

        parsetree = parseQuery(sparqlQuery)
        queryobj = translateQuery(parsetree, base, initNs)
        with self.db.connect() as conn:
            query, var_subform = self.queryPart(conn, queryobj.algebra)
            sqlquery = self._apply_subforms(query, var_subform)
            return sql_pretty(sqlquery)

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
