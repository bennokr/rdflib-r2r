# R2RMLTC0003c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0003c)
Three columns mapping, by using a rr:template to produce literal

## Created SQL query
```sql
SELECT CAST(anon_1."FirstName" AS VARCHAR) || CAST(' ' AS VARCHAR) || CAST(anon_1."LastName" AS VARCHAR) AS o,
       '<http://xmlns.com/foaf/0.1/name>' AS p,
       CAST('<' AS VARCHAR) || CAST('http://example.com/Student' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s
FROM
  (SELECT "Student"."FirstName" AS "FirstName",
          "Student"."LastName" AS "LastName",
          "Student"."ID" AS "ID"
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