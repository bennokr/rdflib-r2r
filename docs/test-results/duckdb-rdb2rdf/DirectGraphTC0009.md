# DirectGraphTC0009
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0009)
Two tables 1 primary key 1 foreign key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Sport>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student"."Sport" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Sport>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Sport"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#Name>' AS p,
                    "Sport"."Name" AS o,
                    NULL AS g
   FROM "Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#Name> "Tennis" .
<http://example.com/base/Sport/ID=100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#Name> "Demi Moore" .
<http://example.com/base/Student/ID=20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#Name> "Tennis" .
<http://example.com/base/Sport/ID=100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#ref-Sport> <http://example.com/base/Sport/ID=100> .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#Name> "Demi Moore" .
<http://example.com/base/Student/ID=20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 174, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```