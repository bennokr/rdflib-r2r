# DirectGraphTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0000)
Direct mapping of an empty table



```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 747, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such column: Student.rowid

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 143, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/compare.py", line 540, in to_isomorphic
    result += graph
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 579, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1606, in addN
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/store.py", line 225, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1606, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 579, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 448, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 622, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1414, in execute
    return meth(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 485, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1638, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
    return self._exec_single_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1983, in _exec_single_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 2325, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 747, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such column: Student.rowid
[SQL: SELECT CAST(? AS VARCHAR) || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, '<http://example.com/base/Student>' AS o, NULL AS g]
[parameters: ('_:Student#',)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```