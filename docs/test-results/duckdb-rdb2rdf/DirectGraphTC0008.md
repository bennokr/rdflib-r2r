# DirectGraphTC0008
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0008)
Generation of direct graph from a table with composite primary key



```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1965, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 921, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 144, in execute
    self.__c.execute(statement, parameters)
duckdb.ParserException: Parser Error: zero-length delimited identifier at or near """"
LINE 2: ... ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(rep...
                                                  ^

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 154, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/compare.py", line 541, in to_isomorphic
    result += graph
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 722, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 2034, in addN
    self.store.addN(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/store.py", line 266, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 2034, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 722, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
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
sqlalchemy.exc.ProgrammingError: (duckdb.ParserException) Parser Error: zero-length delimited identifier at or near """"
LINE 2: ... ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(rep...
                                                  ^
[SQL: SELECT anon_1.s AS s, anon_1.p AS p, anon_1.o AS o, anon_1.g AS g 
FROM (SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Student".""Name"" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, '<http://example.com/base/Student>' AS o, NULL AS g 
FROM "Student" UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Student".""Name"" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://example.com/base/Student#Name>' AS p, "Student"."Name" AS o, NULL AS g 
FROM "Student" UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Student".""Name"" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://example.com/base/Student#ID>' AS p, ? || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || ? AS o, NULL AS g 
FROM "Student" UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? || replace(replace(replace(replace(replace(replace(CAST("Student".""Name"" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://example.com/base/Student#Sport>' AS p, "Student"."Sport" AS o, NULL AS g 
FROM "Student") AS anon_1]
[parameters: ('<Student/ID=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', ';%22Name%22=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<Student/ID=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', ';%22Name%22=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',' ... 10 parameters truncated ... '%28', ')', '%29', ',', '%2C', ':', '%3A', ';%22Name%22=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '"', '"^^<http://www.w3.org/2001/XMLSchema#integer>', '<Student/ID=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', ';%22Name%22=', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: https://sqlalche.me/e/20/f405)

```