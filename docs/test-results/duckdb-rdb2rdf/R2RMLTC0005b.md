# R2RMLTC0005b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0005b)
Default mapping

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:' || CAST("IOUs"."fname" AS VARCHAR) || '_' || CAST("IOUs"."lname" AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/IOUs>' AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '_:' || CAST("IOUs"."fname" AS VARCHAR) || '_' || CAST("IOUs"."lname" AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#amount>' AS p,
                    "IOUs"."amount" AS o,
                    NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '_:' || CAST("IOUs"."fname" AS VARCHAR) || '_' || CAST("IOUs"."lname" AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#lname>' AS p,
                    "IOUs"."lname" AS o,
                    NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '_:' || CAST("IOUs"."fname" AS VARCHAR) || '_' || CAST("IOUs"."lname" AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#fname>' AS p,
                    "IOUs"."fname" AS o,
                    NULL AS g
   FROM "IOUs") AS anon_1
```

## Raw ouput triples
```
_:Bob_Smith <http://example.com/base/IOUs#amount> "30.0" .
_:Bob_Smith <http://example.com/base/IOUs#amount> "30.0" .
_:Bob_Smith <http://example.com/base/IOUs#fname> "Bob" .
_:Bob_Smith <http://example.com/base/IOUs#fname> "Bob" .
_:Bob_Smith <http://example.com/base/IOUs#lname> "Smith" .
_:Bob_Smith <http://example.com/base/IOUs#lname> "Smith" .
_:Bob_Smith <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:Bob_Smith <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:Sue_Jones <http://example.com/base/IOUs#amount> "20.0" .
_:Sue_Jones <http://example.com/base/IOUs#fname> "Sue" .
_:Sue_Jones <http://example.com/base/IOUs#lname> "Jones" .
_:Sue_Jones <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```

## Triple Diff
```diff
+ _:cb0 <http://example.com/base/IOUs#amount> "30.0" .
- _:cb0 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://example.com/base/IOUs#fname> "Bob" .
_:cb0 <http://example.com/base/IOUs#lname> "Smith" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#amount> "20.0" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#fname> "Sue" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#lname> "Jones" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#fname> "Sue" .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#lname> "Jones" .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```