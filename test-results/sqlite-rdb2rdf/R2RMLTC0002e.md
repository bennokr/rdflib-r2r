# R2RMLTC0002e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002e)
Two columns mapping, an undefined rr:tableName



```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such table: Students

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 530, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):  # type: ignore  [arg-type]
  File "/rdflib_r2r/r2r_store.py", line 626, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1583, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 323, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1452, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1814, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1995, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: Students
[SQL: SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Students"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Students"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/id>' AS p, "Students"."ID" AS o, NULL AS g 
FROM "Students"]
[parameters: ('<', 'http://example.com/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: https://sqlalche.me/e/14/e3q8)

```