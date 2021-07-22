# R2RMLTC0010a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0010a)
Template with table column with special chars

## Created SQL query
```sql
SELECT anon_1.o AS o,
       CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.s AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       '<http://example.com/name>' AS p
FROM
  (SELECT "Country Info"."Name" AS o,
          "Country Info"."Country Code" AS s
   FROM "Country Info") AS anon_1
```

## Triple Diff
```diff
<http://example.com/1> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2> <http://example.com/name> "Ireland" .
<http://example.com/3> <http://example.com/name> "Saint Martin (French part)" .
```

SUCCES