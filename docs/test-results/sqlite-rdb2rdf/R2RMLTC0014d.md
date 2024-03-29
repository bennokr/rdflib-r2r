# R2RMLTC0014d
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014d)
three tables, one primary key, one foreign key

## Created SQL query
```sql
SELECT '<http://data.example.com/employee/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BU"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
       '<http://data.example.com/roles/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BU".ROLE AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
       '<http://example.com/ns#role>' AS p
FROM
  (SELECT "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BU"."empno",
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BU".ROLE
   FROM
     (SELECT "EMP".*,
             (CASE "job"
                  WHEN 'CLERK' THEN 'general-office'
                  WHEN 'NIGHTGUARD' THEN 'security'
                  WHEN 'ENGINEER' THEN 'engineering'
              END) AS ROLE
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BU") AS anon_1
```

## Raw ouput triples
```
<http://data.example.com/employee/7369> <http://example.com/ns#role> <http://data.example.com/roles/general-office> .
```

## Triple Diff
```diff
<http://data.example.com/employee/7369> <http://example.com/ns#role> <http://data.example.com/roles/general-office> .
```

SUCCES