# R2RMLTC0010a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0010a)
Template with table column with special chars

## Created SQL query
```sql
SELECT anon_1."Country Info"."Name" AS o,
       '<http://example.com/name>' AS p,
       '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s
FROM
  (SELECT "Country Info"."Name",
          "Country Info"."Country Code"
   FROM "Country Info") AS anon_1
```

## Raw ouput triples
```
<http://example.com/1> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2> <http://example.com/name> "Ireland" .
<http://example.com/3> <http://example.com/name> "Saint Martin (French part)" .
```

## Triple Diff
```diff
<http://example.com/1> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2> <http://example.com/name> "Ireland" .
<http://example.com/3> <http://example.com/name> "Saint Martin (French part)" .
```

SUCCES