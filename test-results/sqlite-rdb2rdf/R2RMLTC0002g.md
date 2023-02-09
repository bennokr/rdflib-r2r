# R2RMLTC0002g
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002g)
Two columns mapping, invalid SQL query



```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: near "IS": syntax error

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
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
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) near "IS": syntax error
[SQL: SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".StudentId AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/id>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."ID" AS o, NULL AS g 
FROM (THIS IS NOT A VALID SQL QUERY) AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"]
[parameters: ('<', '>')]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```