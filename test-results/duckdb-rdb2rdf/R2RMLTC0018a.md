# R2RMLTC0018a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0018a)
Generation of triples by using CHAR datatype column

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://xmlns.com/foaf/0.1/Person>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/id>' AS p,
                    "Student"."ID" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Triple Diff
```diff
+ <http://example.com/10> <http://example.com/id> "10" .
- <http://example.com/10> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
- <http://example.com/10> <http://xmlns.com/foaf/0.1/name> "Venus          " .
+ <http://example.com/10> <http://xmlns.com/foaf/0.1/name> "Venus" .
+ <http://example.com/20> <http://example.com/id> "20" .
- <http://example.com/20> <http://example.com/id> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
- <http://example.com/20> <http://xmlns.com/foaf/0.1/name> "Fernando       " .
+ <http://example.com/20> <http://xmlns.com/foaf/0.1/name> "Fernando" .
+ <http://example.com/30> <http://example.com/id> "30" .
- <http://example.com/30> <http://example.com/id> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/30> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
- <http://example.com/30> <http://xmlns.com/foaf/0.1/name> "David          " .
+ <http://example.com/30> <http://xmlns.com/foaf/0.1/name> "David" .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 168, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get the full diff

```