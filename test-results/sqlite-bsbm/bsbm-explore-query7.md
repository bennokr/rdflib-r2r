# bsbm-explore-query7 
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
  File "/rdflib_r2r/r2r_store.py", line 995, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 942, in queryLeftJoin
    return query2, var_subform2
  File "/rdflib_r2r/r2r_store.py", line 995, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 961, in queryLeftJoin
  File "<string>", line 2, in join
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/base.py", line 104, in _generative
    x = fn(self, *args, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/selectable.py", line 5127, in join
    target = coercions.expect(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 211, in expect
    return impl._implicit_coercions(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 915, in _implicit_coercions
    self._raise_for_expected(original_element, argname, resolved)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 282, in _raise_for_expected
    util.raise_(exc.ArgumentError(msg, code=code), replace_context=err)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
sqlalchemy.exc.ArgumentError: Join target, typically a FROM expression, or ORM relationship attribute expected, got <sqlalchemy.sql.selectable.Select object at 0x7fb847238250>.

```