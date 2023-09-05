# R2RMLTC0014b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014b)
Triplesmaps with rr:inverseExpression and rr:joinCondition

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
                    '<http://example.com/dept#deptno>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#deptNum>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#emptype>' AS p,
                    '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || '>' AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || '>' AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#empno>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."empno" AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#jobtype>' AS p,
                    '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || '>' AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#c_ref_deptno>' AS p,
                    '_:' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref",

     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#job>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."job" AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#name>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."ename" AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://example.com/emp#etype>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."etype" AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"
   UNION ALL SELECT '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<' || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || '>' AS o,
                    NULL AS g
   FROM
     (SELECT ('http://example.com/emp/' || "empno") AS empURI ,
             "empno" ,
             "ename" ,
             ('http://example.com/emp/job/'|| "job") AS jobTypeURI ,
             "job" ,
             "deptno" ,
             ('http://example.com/emp/etype/'|| "etype") AS empTypeURI ,
             "etype" ,
             ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS") AS anon_1
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
_:Department10 <http://example.com/dept#deptno> "10" .
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
+ _:cb0 <http://example.com/dept#deptno> "10" .
- _:cb0 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
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