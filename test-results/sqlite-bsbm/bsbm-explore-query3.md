# bsbm-explore-query3 
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
    query, var_subform = self.queryPart(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 993, in queryPart
    return self.querySlice(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 934, in querySlice
    query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 973, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 885, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 989, in queryPart
    return self.queryOrderBy(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 894, in queryOrderBy
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 969, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 793, in queryFilter
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 995, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 943, in queryLeftJoin
    query2, var_subform2 = self.queryPart(conn, part.p2)
  File "/rdflib_r2r/r2r_store.py", line 967, in queryPart
    return self.queryBGP(conn, part.triples)
  File "/rdflib_r2r/r2r_store.py", line 674, in queryBGP
    pat_query, subforms = self.queryPattern(metadata, pat, restriction)
TypeError: cannot unpack non-iterable NoneType object

```