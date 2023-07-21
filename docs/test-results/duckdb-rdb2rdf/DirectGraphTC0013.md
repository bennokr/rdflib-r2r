# DirectGraphTC0013
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0013)
Generation of a direct graph from a table with NULL values

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Person>' AS o,
          NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#DateOfBirth>' AS p,
                    "Person"."DateOfBirth" AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#Name>' AS p,
                    "Person"."Name" AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Person"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Person") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#Name> "Alice" .
<http://example.com/base/Person/ID=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#DateOfBirth> "September, 2010" .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#Name> "Bob" .
<http://example.com/base/Person/ID=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

## Triple Diff
```diff
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#Name> "Alice" .
<http://example.com/base/Person/ID=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#DateOfBirth> "September, 2010" .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#Name> "Bob" .
<http://example.com/base/Person/ID=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

SUCCES

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 198, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 530, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):  # type: ignore  [arg-type]
  File "/rdflib_r2r/r2r_store.py", line 652, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/result.py", line 381, in iterrows
    for row in self._fetchiter_impl():
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 1788, in _fetchiter_impl
    row = fetchone(self, self.cursor)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 960, in fetchone
    self.handle_exception(result, dbapi_cursor, e)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 941, in handle_exception
    result.connection._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1999, in _handle_dbapi_exception
    util.raise_(exc_info[1], with_traceback=exc_info[2])
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/cursor.py", line 955, in fetchone
    row = dbapi_cursor.fetchone()
duckdb.ConversionException: Conversion Error: Could not convert string 'September, 2010' to INT8

```