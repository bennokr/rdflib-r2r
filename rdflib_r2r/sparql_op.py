"""
rdflib_r2r.sparql_opt
=======================
Provides functions to overrides the RDFlib SPARQL evaluator for RDB stores.

Heavily inspired by rdflib-hdt.
"""
import logging
import functools

import rdflib.plugins.sparql.evaluate as sparql_evaluate
from rdflib import Variable
from rdflib.plugins.sparql.sparql import FrozenBindings, QueryContext

from rdflib_r2r.r2r_store import R2RStore, SparqlNotImplementedError

# copy the default RDFlib function for evaluating Basic Graph Patterns
rdflib_evalPart = sparql_evaluate.evalPart

def freeze_bindings(ctx, res):
    for bindings in res:
        yield FrozenBindings(ctx, bindings)

def optimize_sparql():
    """Overrides the RDFlib SPARQL engine to optimize SPARQL query execution over HDT documents.
    
    .. note::
      Calling this function triggers a global modification of the RDFlib SPARQL engine.
      However, executing SPARQL queries using other RDFlib stores will continue to work as before,
      so you can safely call this function at the beginning of your code.
    """

    def __evalPart__(ctx: QueryContext, part):
        # A SPARQL query executed over a non HDTStore is evaluated as usual
        if not isinstance(ctx.graph.store, R2RStore):
            return rdflib_evalPart(ctx, part)

        # logging.warn(("starting", part.name))
        # try:
        if part.name == "SelectQuery":
            return rdflib_evalPart(ctx, part)
        return freeze_bindings(ctx, ctx.graph.store.evalPart(part))
        # except SparqlNotImplementedError:
            # return rdflib_evalPart(ctx, part)
            

    sparql_evaluate.evalPart = __evalPart__


def reset_sparql():
    sparql_evaluate.evalPart = rdflib_evalPart

