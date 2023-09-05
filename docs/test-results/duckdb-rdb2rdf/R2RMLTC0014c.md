# R2RMLTC0014c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014c)
Triplesmaps with rr:inverseExpression, rr:joinCondition, and referencing object maps

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
          '<http://example.com/dept#COMPANY>' AS p,
          '"EXAMPLE Corporation"' AS o,
          NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#name>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#location>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#deptno>' AS p,
                    '"' || CAST(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#positiveInteger>' AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#jobtype>' AS p,
                    '<http://example.com/emp/job/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."job" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#job>' AS p,
                    "EMP"."job" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#etype>' AS p,
                    "EMP"."etype" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#emptype>' AS p,
                    '<http://example.com/emp/etype/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."etype" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#deptNum>' AS p,
                    "EMP"."deptno" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#c_ref_deptno>' AS p,
                    '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref",
        "EMP"
   WHERE "EMP"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#name>' AS p,
                    "EMP"."ename" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/emp/job/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."job" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/emp#empno>' AS p,
                    "EMP"."empno" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<http://example.com/emp/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."empno" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/emp/etype/' || replace(replace(replace(replace(replace(replace(CAST("EMP"."etype" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "EMP") AS anon_1
```

## Raw ouput triples
```
<http://example.com/emp/7369> <http://example.com/emp#c_ref_deptno> _:Department10 .
<http://example.com/emp/7369> <http://example.com/emp#deptNum> "10" .
<http://example.com/emp/7369> <http://example.com/emp#empno> "7369" .
<http://example.com/emp/7369> <http://example.com/emp#emptype> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://example.com/emp#etype> "PART_TIME" .
<http://example.com/emp/7369> <http://example.com/emp#job> "CLERK" .
<http://example.com/emp/7369> <http://example.com/emp#jobtype> <http://example.com/emp/job/CLERK> .
<http://example.com/emp/7369> <http://example.com/emp#name> "SMITH" .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/job/CLERK> .
_:Department10 <http://example.com/dept#COMPANY> "EXAMPLE Corporation" .
_:Department10 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#positiveInteger> .
_:Department10 <http://example.com/dept#location> "NEW YORK" .
_:Department10 <http://example.com/dept#name> "APPSERVER" .
```

## Triple Diff
```diff
<http://example.com/emp/7369> <http://example.com/emp#c_ref_deptno> _:cb0 .
+ <http://example.com/emp/7369> <http://example.com/emp#deptNum> "10" .
- <http://example.com/emp/7369> <http://example.com/emp#deptNum> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/emp/7369> <http://example.com/emp#empno> "7369" .
- <http://example.com/emp/7369> <http://example.com/emp#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/emp/7369> <http://example.com/emp#emptype> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://example.com/emp#etype> "PART_TIME" .
<http://example.com/emp/7369> <http://example.com/emp#job> "CLERK" .
<http://example.com/emp/7369> <http://example.com/emp#jobtype> <http://example.com/emp/job/CLERK> .
<http://example.com/emp/7369> <http://example.com/emp#name> "SMITH" .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/job/CLERK> .
_:cb0 <http://example.com/dept#COMPANY> "EXAMPLE Corporation" .
_:cb0 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#positiveInteger> .
_:cb0 <http://example.com/dept#location> "NEW YORK" .
_:cb0 <http://example.com/dept#name> "APPSERVER" .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```