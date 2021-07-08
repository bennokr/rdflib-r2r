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

from rdflib_r2r.r2r_store import R2RStore
from rdflib_r2r.types import BGP

# copy the default RDFlib function for evaluating Basic Graph Patterns
rdflib_evalBGP = sparql_evaluate.evalBGP

@functools.lru_cache(maxsize=500, typed=False)
def cachedBGP(ctx, bgp):
    yield from rdflib_evalBGP(ctx, bgp)
    bs = list(rdflib_evalBGP(ctx, bgp))
    if bgp:
        ns = ctx.graph.namespace_manager
        logging.warn('bgp:\n' + '\n'.join(' '.join(n.n3(ns) for n in t) for t in bgp))
        logging.warn(f"Got {len(bs)} results")
        if len(bgp) == 1:
            nonvar = lambda n: n if not isinstance(n, Variable) else None
            pat = tuple(nonvar(n) for n in bgp[0])
            logging.warn(('pat', pat))
            for t in ctx.graph.triples(pat):
                bind = {p:n for p,n in zip(pat,t) if isinstance(n, Variable)}
                yield FrozenBindings(ctx, bind)

def optimize_sparql():
    """Overrides the RDFlib SPARQL engine to optimize SPARQL query execution over HDT documents.
    .. note::
      Calling this function triggers a global modification of the RDFlib SPARQL engine.
      However, executing SPARQL queries using other RDFlib stores will continue to work as before,
      so you can safely call this function at the beginning of your code.
    """
    
    
    def __evalBGP__(ctx: QueryContext, bgp: BGP):
        bgp = tuple(set(bgp))

        # A SPARQL query executed over a non HDTStore is evaluated as usual
        if not isinstance(ctx.graph.store, R2RStore):
            return cachedBGP(ctx, bgp)

        # delegate the join evaluation to the DB
        store: R2RStore = ctx.graph.store
        for bindings in list(store.evalBGP(bgp)):
            yield FrozenBindings(ctx, bindings)
        

    # overrides RDFlib evalBGP function
    sparql_evaluate.evalBGP = __evalBGP__

def reset_sparql():
    sparql_evaluate.evalBGP = rdflib_evalBGP