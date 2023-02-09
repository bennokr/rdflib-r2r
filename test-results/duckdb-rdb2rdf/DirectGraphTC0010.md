# DirectGraphTC0010
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0010)
Generation of direct graph for table names with spaces

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Country%20Info>' AS o,
          NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Name>' AS p,
                    "Country Info"."Name" AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Country%20Code>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Country Info"."Country Code" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#ISO%203166>' AS p,
                    "Country Info"."ISO 3166" AS o,
                    NULL AS g
   FROM "Country Info") AS anon_1
```

## Triple Diff
```diff
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#ISO%203166> "BO" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#ISO%203166> "IE" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Name> "Ireland" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#ISO%203166> "MF" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
```

SUCCES

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 185, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
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
RuntimeError: Binder Error: Type mismatch for binding parameter with index 49, expected type VARCHAR but got type INTEGER

```