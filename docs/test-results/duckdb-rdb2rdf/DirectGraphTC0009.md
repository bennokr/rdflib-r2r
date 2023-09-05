# DirectGraphTC0009
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0009)
Two tables 1 primary key 1 foreign key

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
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ref-Sport>' AS p,
                    '_:Sport#' || CAST(CAST("Sport_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student",
        "Sport" AS "Sport_ref"
   WHERE "Student"."Sport" = "Sport_ref"."ID"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Sport>' AS p,
                    '"' || CAST(CAST("Student"."Sport" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Sport>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#ID>' AS p,
                    '"' || CAST(CAST("Sport"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#Name>' AS p,
                    "Sport"."Name" AS o,
                    NULL AS g
   FROM "Sport") AS anon_1
```

## Raw ouput triples
```
_:Sport#0 <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Sport#0 <http://example.com/base/Sport#Name> "Tennis" .
_:Sport#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
_:Student#0 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#0 <http://example.com/base/Student#Name> "Venus Williams" .
_:Student#0 <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#0 <http://example.com/base/Student#ref-Sport> _:Sport#0 .
_:Student#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:Student#1 <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#1 <http://example.com/base/Student#Name> "Demi Moore" .
_:Student#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
- <http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#Name> "Tennis" .
- <http://example.com/base/Sport/ID=100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#Name> "Venus Williams" .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#ref-Sport> <http://example.com/base/Sport/ID=100> .
- <http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=20> <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=20> <http://example.com/base/Student#Name> "Demi Moore" .
- <http://example.com/base/Student/ID=20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb0 <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://example.com/base/Student#Name> "Demi Moore" .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb5eaaef78fd9a13a7af2e02e92319ae391e64c3d93952302bfcf6996b4cf9d293 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb5eaaef78fd9a13a7af2e02e92319ae391e64c3d93952302bfcf6996b4cf9d293 <http://example.com/base/Student#Name> "Venus Williams" .
+ _:cb5eaaef78fd9a13a7af2e02e92319ae391e64c3d93952302bfcf6996b4cf9d293 <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb5eaaef78fd9a13a7af2e02e92319ae391e64c3d93952302bfcf6996b4cf9d293 <http://example.com/base/Student#ref-Sport> _:cb72850346c5671e61a3b58f39fd59be466916e635b9fdb84c90a0296e729fb7a4 .
+ _:cb5eaaef78fd9a13a7af2e02e92319ae391e64c3d93952302bfcf6996b4cf9d293 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb72850346c5671e61a3b58f39fd59be466916e635b9fdb84c90a0296e729fb7a4 <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb72850346c5671e61a3b58f39fd59be466916e635b9fdb84c90a0296e729fb7a4 <http://example.com/base/Sport#Name> "Tennis" .
+ _:cb72850346c5671e61a3b58f39fd59be466916e635b9fdb84c90a0296e729fb7a4 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```