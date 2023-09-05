# R2RMLTC0004b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0004b)
Two column mapping, presence of rr:termType rr:Literal on rr:subjectMap



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 124, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 592, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 672, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1412, in execute
    return meth(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 515, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1635, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1844, in _execute_context
    return self._exec_single_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1984, in _exec_single_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2342, in _handle_dbapi_exception
    raise exc_info[1].with_traceback(exc_info[2])
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1965, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 131, in do_execute
    cursor.execute(statement, parameters, context)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 93, in execute
    self.c.execute(statement, parameters)
duckdb.InvalidInputException: Invalid Input Error: Param is of type 'dict', but no named parameters were found in the query

```