# R2RMLTC0008b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0008b)
Generation of triples referencing object map



```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: ambiguous column name: Student.ID

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
  File "/rdflib_r2r/r2r_store.py", line 620, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1994, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) ambiguous column name: Student.ID
[SQL: SELECT anon_1.s AS s, anon_1.p AS p, anon_1.o AS o, anon_1.g AS g 
FROM (SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Sport" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, '<http://example.com/activity/Sport>' AS o, NULL AS g 
FROM "Student" UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://xmlns.com/foaf/0.1/name>' AS p, "Student"."Name" AS o, NULL AS g 
FROM "Student" UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/id>' AS p, "Student"."ID" AS o, NULL AS g 
FROM "Student" UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, '<http://xmlns.com/foaf/0.1/Person>' AS o, NULL AS g 
FROM "Student" UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/Sport>' AS p, CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Sport" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM "Student", "Student" AS "Student") AS anon_1]
[parameters: ('<', 'http://example.com/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://example.com/Student/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://example.com/Student/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://example.com/Student/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://example.com/Student/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://example.com/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```