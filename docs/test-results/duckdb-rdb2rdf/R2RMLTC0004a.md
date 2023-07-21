# R2RMLTC0004a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0004a)
Two column mapping, from one row table to two different triples

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/Student>' AS o,
          NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "Student_Sport"."Student" AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/Sport>' AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "Student_Sport"."Sport" AS o,
                    NULL AS g
   FROM "Student_Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/Tennis> <http://xmlns.com/foaf/0.1/name> "Tennis" .
<http://example.com/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

## Triple Diff
```diff
<http://example.com/Tennis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Sport> .
<http://example.com/Tennis> <http://xmlns.com/foaf/0.1/name> "Tennis" .
<http://example.com/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/Student> .
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES