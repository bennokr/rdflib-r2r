# R2RMLTC0001a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0001a)
One column mapping, subject URI generation by using rr:template

## Created SQL query
```sql
SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
       '<http://xmlns.com/foaf/0.1/name>' AS p,
       anon_1."Student"."Name" AS o
FROM
  (SELECT "Student"."Name",
          "Student"."Name"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

## Triple Diff
```diff
<http://example.com/Venus> <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES