# R2RMLTC0012a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012a)
Duplicate tuples generate same blank node

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('_:' AS VARCHAR) || CAST("IOUs"."fname" AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs"."lname" AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs"."amount" AS VARCHAR) AS s,
          '<http://xmlns.com/foaf/0.1/name>' AS p,
          CAST("IOUs"."fname" AS VARCHAR) || CAST(' ' AS VARCHAR) || CAST("IOUs"."lname" AS VARCHAR) AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("IOUs"."fname" AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs"."lname" AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs"."amount" AS VARCHAR) AS s,
                    '<http://example.com/amount>' AS p,
                    "IOUs"."amount" AS o,
                    NULL AS g
   FROM "IOUs") AS anon_1
```

## Raw ouput triples
```
_:Bob_Smith_30.0 <http://example.com/amount> "30.0" .
_:Bob_Smith_30.0 <http://example.com/amount> "30.0" .
_:Bob_Smith_30.0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Bob_Smith_30.0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Sue_Jones_20.0 <http://example.com/amount> "20.0" .
_:Sue_Jones_20.0 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

## Triple Diff
```diff
+ _:cb0 <http://example.com/amount> "30.0" .
- _:cb0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
+ _:cb1e7a578a70e9521702adabc5bf6eb99b18a87eed7c5d4acee7b12e25c97068c5 <http://example.com/amount> "20.0" .
+ _:cb1e7a578a70e9521702adabc5bf6eb99b18a87eed7c5d4acee7b12e25c97068c5 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
- _:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://example.com/amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 174, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```