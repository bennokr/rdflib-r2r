# R2RMLTC0011a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0011a)
M to M relation, by using a SQL query

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".ID AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".FirstName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".LastName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://example.com/firstName>' AS p,
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".FirstName AS o,
          NULL AS g
   FROM
     (SELECT "Student"."ID" AS ID,
             "Student"."FirstName" AS FirstName,
             "Student"."LastName" AS LastName,
             "Sport"."Description" AS Description,
             "Sport"."ID" AS Sport_ID
      FROM "Student",
           "Sport",
           "Student_Sport"
      WHERE "Student"."ID" = "Student_Sport"."ID_Student"
        AND "Sport"."ID" = "Student_Sport"."ID_Sport") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".ID AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".FirstName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".LastName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/id>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".ID AS o,
                    NULL AS g
   FROM
     (SELECT "Student"."ID" AS ID,
             "Student"."FirstName" AS FirstName,
             "Student"."LastName" AS LastName,
             "Sport"."Description" AS Description,
             "Sport"."ID" AS Sport_ID
      FROM "Student",
           "Sport",
           "Student_Sport"
      WHERE "Student"."ID" = "Student_Sport"."ID_Student"
        AND "Sport"."ID" = "Student_Sport"."ID_Sport") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".ID AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".FirstName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".LastName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/plays>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".Sport_ID AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".Description AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM
     (SELECT "Student"."ID" AS ID,
             "Student"."FirstName" AS FirstName,
             "Student"."LastName" AS LastName,
             "Sport"."Description" AS Description,
             "Sport"."ID" AS Sport_ID
      FROM "Student",
           "Sport",
           "Student_Sport"
      WHERE "Student"."ID" = "Student_Sport"."ID_Student"
        AND "Sport"."ID" = "Student_Sport"."ID_Sport") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".ID AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".FirstName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".LastName AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/lastName>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".LastName AS o,
                    NULL AS g
   FROM
     (SELECT "Student"."ID" AS ID,
             "Student"."FirstName" AS FirstName,
             "Student"."LastName" AS LastName,
             "Sport"."Description" AS Description,
             "Sport"."ID" AS Sport_ID
      FROM "Student",
           "Sport",
           "Student_Sport"
      WHERE "Student"."ID" = "Student_Sport"."ID_Student"
        AND "Sport"."ID" = "Student_Sport"."ID_Sport") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."Description" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/description>' AS p,
                    "Sport"."Description" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."Description" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/id>' AS p,
                    "Sport"."ID" AS o,
                    NULL AS g
   FROM "Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/10/Venus;Williams> <http://example.com/firstName> "Venus" .
<http://example.com/10/Venus;Williams> <http://example.com/id> "10" .
<http://example.com/10/Venus;Williams> <http://example.com/lastName> "Williams" .
<http://example.com/10/Venus;Williams> <http://example.com/plays> <http://example.com/110/Tennis> .
<http://example.com/11/Fernando;Alonso> <http://example.com/firstName> "Fernando" .
<http://example.com/11/Fernando;Alonso> <http://example.com/firstName> "Fernando" .
<http://example.com/11/Fernando;Alonso> <http://example.com/id> "11" .
<http://example.com/11/Fernando;Alonso> <http://example.com/id> "11" .
<http://example.com/11/Fernando;Alonso> <http://example.com/lastName> "Alonso" .
<http://example.com/11/Fernando;Alonso> <http://example.com/lastName> "Alonso" .
<http://example.com/11/Fernando;Alonso> <http://example.com/plays> <http://example.com/111/Football> .
<http://example.com/11/Fernando;Alonso> <http://example.com/plays> <http://example.com/112/Formula1> .
<http://example.com/110/Tennis> <http://example.com/description> "Tennis" .
<http://example.com/110/Tennis> <http://example.com/id> "110" .
<http://example.com/111/Football> <http://example.com/description> "Football" .
<http://example.com/111/Football> <http://example.com/id> "111" .
<http://example.com/112/Formula1> <http://example.com/description> "Formula1" .
<http://example.com/112/Formula1> <http://example.com/id> "112" .
<http://example.com/12/David;Villa> <http://example.com/firstName> "David" .
<http://example.com/12/David;Villa> <http://example.com/id> "12" .
<http://example.com/12/David;Villa> <http://example.com/lastName> "Villa" .
<http://example.com/12/David;Villa> <http://example.com/plays> <http://example.com/111/Football> .
```

## Triple Diff
```diff
<http://example.com/10/Venus;Williams> <http://example.com/firstName> "Venus" .
+ <http://example.com/10/Venus;Williams> <http://example.com/id> "10" .
- <http://example.com/10/Venus;Williams> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/10/Venus;Williams> <http://example.com/lastName> "Williams" .
<http://example.com/10/Venus;Williams> <http://example.com/plays> <http://example.com/110/Tennis> .
<http://example.com/11/Fernando;Alonso> <http://example.com/firstName> "Fernando" .
+ <http://example.com/11/Fernando;Alonso> <http://example.com/id> "11" .
- <http://example.com/11/Fernando;Alonso> <http://example.com/id> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/11/Fernando;Alonso> <http://example.com/lastName> "Alonso" .
<http://example.com/11/Fernando;Alonso> <http://example.com/plays> <http://example.com/111/Football> .
<http://example.com/11/Fernando;Alonso> <http://example.com/plays> <http://example.com/112/Formula1> .
<http://example.com/110/Tennis> <http://example.com/description> "Tennis" .
+ <http://example.com/110/Tennis> <http://example.com/id> "110" .
- <http://example.com/110/Tennis> <http://example.com/id> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/111/Football> <http://example.com/description> "Football" .
+ <http://example.com/111/Football> <http://example.com/id> "111" .
- <http://example.com/111/Football> <http://example.com/id> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/112/Formula1> <http://example.com/description> "Formula1" .
+ <http://example.com/112/Formula1> <http://example.com/id> "112" .
- <http://example.com/112/Formula1> <http://example.com/id> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/12/David;Villa> <http://example.com/firstName> "David" .
+ <http://example.com/12/David;Villa> <http://example.com/id> "12" .
- <http://example.com/12/David;Villa> <http://example.com/id> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/12/David;Villa> <http://example.com/lastName> "Villa" .
<http://example.com/12/David;Villa> <http://example.com/plays> <http://example.com/111/Football> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 174, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```