# R2RMLTC0010c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0010c)
Template with table columns with special chars and backslashes

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       CAST('{' AS VARCHAR) || CAST('{' AS VARCHAR) || CAST('{' AS VARCHAR) || CAST(' ' AS VARCHAR) || CAST(anon_1."ISO 3166" AS VARCHAR) || CAST(' }' AS VARCHAR) || CAST('}' AS VARCHAR) || CAST('}' AS VARCHAR) AS o,
       '<http://example.com/code>' AS p
FROM
  (SELECT "Country Info"."Country Code" AS "Country Code",
          "Country Info"."Name" AS "Name",
          "Country Info"."ISO 3166" AS "ISO 3166"
   FROM "Country Info") AS anon_1
```

## Triple Diff
```diff
<http://example.com/1/Bolivia%2C%20Plurinational%20State%20of> <http://example.com/code> "{{{ BO }}}" .
<http://example.com/2/Ireland> <http://example.com/code> "{{{ IE }}}" .
<http://example.com/3/Saint%20Martin%20%28French%20part%29> <http://example.com/code> "{{{ MF }}}" .
```

SUCCES