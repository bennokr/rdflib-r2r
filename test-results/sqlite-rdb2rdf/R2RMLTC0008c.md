# R2RMLTC0008c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0008c)
Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Student/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://xmlns.com/foaf/0.1/name>' AS p,
          "Student"."Name" AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Student/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams" .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

## Triple Diff
```diff
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams" .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES