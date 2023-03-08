# R2RMLTC0009d
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0009d)
Named column in logical table

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/resource/student_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://example.com/numSport>' AS p,
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".SPORTCOUNT AS o,
          NULL AS g
   FROM
     (SELECT "Name",
             COUNT("Sport") AS SPORTCOUNT
      FROM "Student"
      GROUP BY "Name") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/resource/student_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name" AS o,
                    NULL AS g
   FROM
     (SELECT "Name",
             COUNT("Sport") AS SPORTCOUNT
      FROM "Student"
      GROUP BY "Name") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Raw ouput triples
```
<http://example.com/resource/student_Demi%20Moore> <http://example.com/numSport> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/resource/student_Demi%20Moore> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
<http://example.com/resource/student_Venus%20Williams> <http://example.com/numSport> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/resource/student_Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

## Triple Diff
```diff
<http://example.com/resource/student_Demi%20Moore> <http://example.com/numSport> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/resource/student_Demi%20Moore> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
<http://example.com/resource/student_Venus%20Williams> <http://example.com/numSport> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/resource/student_Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES