# DirectGraphTC0003
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0003)
Three columns mapping, generation of a BlankNode

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#FirstName>' AS p,
                    "Student"."FirstName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#LastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
_:Student#0 <http://example.com/base/Student#FirstName> "Venus" .
_:Student#0 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#0 <http://example.com/base/Student#LastName> "Williams" .
_:Student#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
_:cb0 <http://example.com/base/Student#FirstName> "Venus" .
_:cb0 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb0 <http://example.com/base/Student#LastName> "Williams" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES

```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 1104, in fetchone
    row = dbapi_cursor.fetchone()
duckdb.ConversionException: Conversion Error: Could not convert string 'Venus' to INT8

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 207, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 592, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 672, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/result.py", line 533, in iterrows
    for raw_row in self._fetchiter_impl():
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 2093, in _fetchiter_impl
    row = fetchone(self, self.cursor)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 1109, in fetchone
    self.handle_exception(result, dbapi_cursor, e)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 1080, in handle_exception
    result.connection._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2339, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 1104, in fetchone
    row = dbapi_cursor.fetchone()
sqlalchemy.exc.DataError: (duckdb.ConversionException) Conversion Error: Could not convert string 'Venus' to INT8
(Background on this error at: https://sqlalche.me/e/20/9h9h)

```