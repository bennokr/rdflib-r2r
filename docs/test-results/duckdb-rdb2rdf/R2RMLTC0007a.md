# R2RMLTC0007a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0007a)
Typing resources by relying on rdf:type predicate

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Student/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
       '<http://xmlns.com/foaf/0.1/Person>' AS o
FROM
  (SELECT "Student"."ID",
          "Student"."Name"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

## Triple Diff
```diff
<http://example.com/Student/10/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES