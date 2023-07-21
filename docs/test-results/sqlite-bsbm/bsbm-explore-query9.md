# bsbm-explore-query9
[bsbm-explore-query9](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ9)


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 210, in test_bsbm
    goal = set(graph.query(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1321, in query
    return result(processor.query(query_object, initBindings, initNs, **kwargs))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/processor.py", line 75, in query
    return evalQuery(self.graph, query, initBindings, base)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/evaluate.py", line 586, in evalQuery
    return evalPart(ctx, main)
  File "/rdflib_r2r/sparql_op.py", line 35, in __evalPart__
    return rdflib_evalPart(ctx, part)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/plugins/sparql/evaluate.py", line 296, in evalPart
    raise Exception("DESCRIBE not implemented")
Exception: DESCRIBE not implemented

```