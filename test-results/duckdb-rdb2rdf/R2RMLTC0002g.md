# R2RMLTC0002g
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002g)
Two columns mapping, invalid SQL query



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 448, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 619, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1262, in execute
    return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1998, in _handle_dbapi_exception
    util.raise_(exc_info[1], with_traceback=exc_info[2])
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/duckdb_engine/__init__.py", line 71, in do_execute
    cursor.execute(statement, parameters, context)
  File "/opt/miniconda3/lib/python3.8/site-packages/duckdb_engine/__init__.py", line 35, in execute
    self.c.execute(statement, parameters)
RuntimeError: Parser Error: syntax error at or near "IS"
LINE 2: FROM (THIS IS NOT A VALID SQL QUERY) AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"...
                   ^

```