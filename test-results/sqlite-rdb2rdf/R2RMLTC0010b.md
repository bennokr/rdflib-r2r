# R2RMLTC0010b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0010b)
Template with table columns with special chars

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.s AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.o AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       anon_1.p AS o,
       '<http://example.com/name>' AS p
FROM
  (SELECT "Country Info"."Country Code" AS s,
          "Country Info"."Name" AS o,
          "Country Info"."Name" AS p
   FROM "Country Info") AS anon_1
```

## Triple Diff
```diff
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/name> "Bolivia, Plurinational State of" .
<http://example.com/2/Ireland> <http://example.com/name> "Ireland" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/name> "Saint Martin (French part)" .
```

SUCCES