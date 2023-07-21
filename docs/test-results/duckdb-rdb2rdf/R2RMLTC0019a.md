# R2RMLTC0019a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0019a)
Generation of triples by using IRI value in columns

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."FirstName" AS o,
       CAST('<' AS VARCHAR) || CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."FirstName" AS VARCHAR) || CAST('>' AS VARCHAR) AS s
FROM
  (SELECT "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."FirstName",
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."FirstName"
   FROM
     (SELECT "ID",
             "FirstName",
             "LastName"
      FROM "Employee"
      WHERE "ID" < 30) AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
```

## Triple Diff
```diff
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
```

SUCCES