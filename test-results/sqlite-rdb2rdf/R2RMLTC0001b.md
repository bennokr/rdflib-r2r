# R2RMLTC0001b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0001b)
One column mapping, generation of a BlankNode subject by using rr:termType

## Created SQL query
```sql
SELECT anon_1."Name" AS o,
       CAST('_:' AS VARCHAR) || CAST(anon_1."Name" AS VARCHAR) AS s,
       '<http://xmlns.com/foaf/0.1/name>' AS p
FROM
  (SELECT "Student"."Name" AS "Name",
          "Student"."Name" AS "Name__1"
   FROM "Student") AS anon_1
```

## Triple Diff
```diff
_:cb0 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES