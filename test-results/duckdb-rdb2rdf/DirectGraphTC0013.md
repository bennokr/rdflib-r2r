# DirectGraphTC0013
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0013)
Generation of a direct graph from a table with NULL values


```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 139, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/compare.py", line 492, in to_isomorphic
    result += graph
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in addN
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/store.py", line 225, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 607, in triples
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
RuntimeError: Binder Error: No function matches the given name and argument types '||(BLOB, VARCHAR)'. You might need to add explicit type casts.
	Candidate functions:
	||(VARCHAR, VARCHAR) -> VARCHAR
	||(BLOB, BLOB) -> BLOB


```