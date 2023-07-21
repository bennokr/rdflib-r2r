# R2RMLTC0002e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002e)
Two columns mapping, an undefined rr:tableName



```
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 747, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such table: Students

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/rdflib/graph.py", line 594, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 672, in triples
    rows = list(conn.execute(query))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1414, in execute
    return meth(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 485, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1638, in _execute_clauseelement
    ret = self._execute_context(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1842, in _execute_context
    return self._exec_single_context(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1983, in _exec_single_context
    self._handle_dbapi_exception(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2325, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1964, in _exec_single_context
    self.dialect.do_execute(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 747, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: Students
[SQL: SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Students"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Students"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://example.com/id>' AS p, "Students"."ID" AS o, NULL AS g 
FROM "Students"]
[parameters: ('<http://example.com/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: https://sqlalche.me/e/20/e3q8)

```