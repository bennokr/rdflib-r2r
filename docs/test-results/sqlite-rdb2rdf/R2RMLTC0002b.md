# R2RMLTC0002b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002b)
Two columns mapping, generation of a BlankNode subject by using rr:template and rr:termType

## Created SQL query
```sql
SELECT '_:students' || CAST(anon_1."ID" AS VARCHAR) AS s,
       '<http://xmlns.com/foaf/0.1/name>' AS p,
       anon_1."Name" AS o
FROM
  (SELECT "Student"."ID" AS "ID",
          "Student"."Name" AS "Name"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
_:students10 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

## Triple Diff
```diff
_:cb0 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES