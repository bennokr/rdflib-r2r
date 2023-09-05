# DirectGraphTC0013
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0013)
Generation of a direct graph from a table with NULL values

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Person#' || CAST(CAST("Person".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Person>' AS o,
          NULL AS g
   FROM "Person"
   UNION ALL SELECT '_:Person#' || CAST(CAST("Person".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Person#ID>' AS p,
                    '"' || CAST(CAST("Person"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT '_:Person#' || CAST(CAST("Person".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Person#DateOfBirth>' AS p,
                    "Person"."DateOfBirth" AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT '_:Person#' || CAST(CAST("Person".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Person#Name>' AS p,
                    "Person"."Name" AS o,
                    NULL AS g
   FROM "Person") AS anon_1
```

## Raw ouput triples
```
_:Person#0 <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Person#0 <http://example.com/base/Person#Name> "Alice" .
_:Person#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
_:Person#1 <http://example.com/base/Person#DateOfBirth> "September, 2010" .
_:Person#1 <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Person#1 <http://example.com/base/Person#Name> "Bob" .
_:Person#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

## Triple Diff
```diff
- <http://example.com/base/Person/ID=1> <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Person/ID=1> <http://example.com/base/Person#Name> "Alice" .
- <http://example.com/base/Person/ID=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
- <http://example.com/base/Person/ID=2> <http://example.com/base/Person#DateOfBirth> "September, 2010" .
- <http://example.com/base/Person/ID=2> <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Person/ID=2> <http://example.com/base/Person#Name> "Bob" .
- <http://example.com/base/Person/ID=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
+ _:cb0 <http://example.com/base/Person#DateOfBirth> "September, 2010" .
+ _:cb0 <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://example.com/base/Person#Name> "Bob" .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
+ _:cb6f5b880cb6d760d97934946989790004d8d6e619636889461addeef84614f33d <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb6f5b880cb6d760d97934946989790004d8d6e619636889461addeef84614f33d <http://example.com/base/Person#Name> "Alice" .
+ _:cb6f5b880cb6d760d97934946989790004d8d6e619636889461addeef84614f33d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```