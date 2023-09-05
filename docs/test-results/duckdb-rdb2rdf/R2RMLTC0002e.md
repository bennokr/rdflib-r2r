# R2RMLTC0002e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002e)
Two columns mapping, an undefined rr:tableName



```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1965, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 921, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 144, in execute
    self.__c.execute(statement, parameters)
duckdb.CatalogException: Catalog Error: Table with name Students does not exist!
Did you mean "Student"?
LINE 2: FROM "Students"
             ^

The above exception was the direct cause of the following exception:

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
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2339, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1965, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 921, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 144, in execute
    self.__c.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (duckdb.CatalogException) Catalog Error: Table with name Students does not exist!
Did you mean "Student"?
LINE 2: FROM "Students"
             ^
[SQL: SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Students"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Students"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://example.com/id>' AS p, "Students"."ID" AS o, NULL AS g 
FROM "Students"]
[parameters: ('<http://example.com/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: https://sqlalche.me/e/20/f405)

```