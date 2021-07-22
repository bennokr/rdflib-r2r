# R2RMLTC0002b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002b)
Two columns mapping, generation of a BlankNode subject by using rr:template and rr:termType

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       CAST('_:' AS VARCHAR) || CAST('students' AS VARCHAR) || CAST(anon_1.p AS VARCHAR) AS s,
       anon_1.s AS o
FROM
  (SELECT "Student"."ID" AS p,
          "Student"."Name" AS s
   FROM "Student") AS anon_1
```

## Triple Diff
```diff
_:cb0 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES