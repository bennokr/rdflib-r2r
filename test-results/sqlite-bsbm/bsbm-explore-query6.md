# bsbm-explore-query6 
```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 205, in test_bsbm
    made = tuple(graph_rdb.query(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1131, in query
    return result(processor.query(query_object, initBindings, initNs, **kwargs))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/processor.py", line 80, in query
    return evalQuery(self.graph, query, initBindings, base)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/evaluate.py", line 532, in evalQuery
    return evalPart(ctx, main)
  File "/rdflib_r2r/sparql_op.py", line 40, in __evalPart__
    return rdflib_evalPart(ctx, part)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/evaluate.py", line 261, in evalPart
    return evalSelectQuery(ctx, part)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/evaluate.py", line 464, in evalSelectQuery
    res["bindings"] = evalPart(ctx, query.p)
  File "/rdflib_r2r/sparql_op.py", line 41, in __evalPart__
    return freeze_bindings(ctx, ctx.graph.store.evalPart(part))
  File "/rdflib_r2r/r2r_store.py", line 1037, in evalPart
  File "/rdflib_r2r/r2r_store.py", line 973, in queryPart
    if part.name == "AggregateJoin":
  File "/rdflib_r2r/r2r_store.py", line 885, in queryProject
    colforms = [ColForm.from_subform(cols, sf) for sf in var_subform.values()]
  File "/rdflib_r2r/r2r_store.py", line 969, in queryPart
    if part.name == "Project":
  File "/rdflib_r2r/r2r_store.py", line 813, in queryFilter
    if part.p.name == "AggregateJoin":
  File "/rdflib_r2r/r2r_store.py", line 790, in queryExpr
    part_query, var_subform = self.queryPart(conn, part.p)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_REGEX' Builtin_REGEX_Builtin_REGEX_{'text': rdflib.term.Variable('label'), 'pattern': rdflib.term.Literal('sot'), '_vars': {rdflib.term.Variable('label')}}

```