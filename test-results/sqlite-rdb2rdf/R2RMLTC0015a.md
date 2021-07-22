# R2RMLTC0015a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0015a)
Generation of language tags from a table with language information

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          CAST('"' AS VARCHAR) || CAST(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."Name" AS VARCHAR) AS VARCHAR) || CAST('"@es' AS VARCHAR) AS o,
          NULL AS g
   FROM
     (SELECT "Code",
             "Name",
             "Lan"
      FROM "Country"
      WHERE "Lan" = 'ES') AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name" AS VARCHAR) AS VARCHAR) || CAST('"@en' AS VARCHAR) AS o,
                    NULL AS g
   FROM
     (SELECT "Code",
             "Name",
             "Lan"
      FROM "Country"
      WHERE "Lan" = 'EN') AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Triple Diff
```diff
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Bolivia, Plurinational State of"@en .
<http://example.com/BO> <http://www.w3.org/2000/01/rdf-schema#label> "Estado Plurinacional de Bolivia"@es .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Ireland"@en .
<http://example.com/IE> <http://www.w3.org/2000/01/rdf-schema#label> "Irlanda"@es .
```

SUCCES