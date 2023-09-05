# R2RMLTC0008b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0008b)
Generation of triples referencing object map

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("Student"."Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/activity/Sport>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/Student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/id>' AS p,
                    "Student"."ID" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/Student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/Sport>' AS p,
                    '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("Student_ref"."Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Student",
        "Student" AS "Student_ref"
   UNION ALL SELECT '<http://example.com/Student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://xmlns.com/foaf/0.1/Person>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/Student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> <http://example.com/Tennis> .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10" .
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/activity/Sport> .
```

## Triple Diff
```diff
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> <http://example.com/Tennis> .
+ <http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10" .
- <http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/activity/Sport> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```