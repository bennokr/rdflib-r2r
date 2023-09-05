# R2RMLTC0001b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0001b)
One column mapping, generation of a BlankNode subject by using rr:termType

## Created SQL query
```sql
SELECT '_:' || CAST(anon_1."Student"."Name" AS VARCHAR) AS s,
       anon_1."Student"."Name" AS o,
       '<http://xmlns.com/foaf/0.1/name>' AS p
FROM
  (SELECT "Student"."Name",
          "Student"."Name"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
_:Venus <http://xmlns.com/foaf/0.1/name> "Venus" .
```

## Triple Diff
```diff
_:cb0 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES