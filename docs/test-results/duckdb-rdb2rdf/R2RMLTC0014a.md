# R2RMLTC0014a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014a)
Subjectmap with rr:inverseExpression

## Created SQL query
```sql
SELECT CAST('_:' AS VARCHAR) || CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptId" AS VARCHAR) AS s,
       anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" AS o,
       '<http://example.com/dept#location>' AS p
FROM
  (SELECT "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptId",
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc"
   FROM
     (SELECT ('Department' || "deptno") AS "deptId" ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Raw ouput triples
```
_:Department10 <http://example.com/dept#location> "NEW YORK" .
```

## Triple Diff
```diff
_:cb0 <http://example.com/dept#location> "NEW YORK" .
```

SUCCES