# R2RMLTC0003c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0003c)
Three columns mapping, by using a rr:template to produce literal

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       CAST('<' AS VARCHAR) || CAST('http://example.com/Student' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       CAST(anon_1."Student"."FirstName" AS VARCHAR) || CAST(' ' AS VARCHAR) || CAST(anon_1."Student"."LastName" AS VARCHAR) AS o
FROM
  (SELECT "Student"."ID",
          "Student"."FirstName",
          "Student"."LastName"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Student10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

## Triple Diff
```diff
<http://example.com/Student10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES