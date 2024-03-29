# R2RMLTC0003b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0003b)
Three columns mapping, concatenation of columns, by using a rr:sqlQuery to produce literal

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       '<http://example.com/Student/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
       anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".Name AS o
FROM
  (SELECT "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."ID",
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".Name
   FROM
     (SELECT "ID",
             ("FirstName" || ' ' || "LastName") AS Name
      FROM "Student") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Student/10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

## Triple Diff
```diff
<http://example.com/Student/10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES