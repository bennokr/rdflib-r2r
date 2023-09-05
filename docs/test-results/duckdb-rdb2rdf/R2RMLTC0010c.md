# R2RMLTC0010c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0010c)
Template with table columns with special chars and backslashes

## Created SQL query
```sql
SELECT '{{{ ' || CAST(anon_1."Country Info"."ISO 3166" AS VARCHAR) || ' }' || '}' || '}' AS o,
       '<http://example.com/code>' AS p,
       '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Country Info"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s
FROM
  (SELECT "Country Info"."ISO 3166",
          "Country Info"."Country Code",
          "Country Info"."Name"
   FROM "Country Info") AS anon_1
```

## Raw ouput triples
```
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/code> "{{{ BO }}}" .
<http://example.com/2/Ireland> <http://example.com/code> "{{{ IE }}}" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/code> "{{{ MF }}}" .
```

## Triple Diff
```diff
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/code> "{{{ BO }}}" .
<http://example.com/2/Ireland> <http://example.com/code> "{{{ IE }}}" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/code> "{{{ MF }}}" .
```

SUCCES