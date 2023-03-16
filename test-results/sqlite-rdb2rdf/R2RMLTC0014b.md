# R2RMLTC0014b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014b)
Triplesmaps with rr:inverseExpression and rr:joinCondition

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
          '<http://example.com/dept#location>' AS p,
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" AS o,
          NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#name>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#deptno>' AS p,
                    "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#COMPANY>' AS p,
                    '"EXAMPLE Corporation"' AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#c_ref_deptno>' AS p,
                    CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o,
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
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS",

     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"
   WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#jobtype>' AS p,
                    CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || CAST('>' AS VARCHAR) AS o,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#emptype>' AS p,
                    CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || CAST('>' AS VARCHAR) AS o,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || CAST('>' AS VARCHAR) AS o,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || CAST('>' AS VARCHAR) AS o,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST('>' AS VARCHAR) AS s,
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
      FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS") AS anon_1
```

## Raw ouput triples
```
<http://example.com/emp/7369> <http://example.com/emp#c_ref_deptno> _:Department10 .
<http://example.com/emp/7369> <http://example.com/emp#deptNum> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/emp/7369> <http://example.com/emp#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/emp/7369> <http://example.com/emp#emptype> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://example.com/emp#etype> "PART_TIME" .
<http://example.com/emp/7369> <http://example.com/emp#job> "CLERK" .
<http://example.com/emp/7369> <http://example.com/emp#jobtype> <http://example.com/emp/job/CLERK> .
<http://example.com/emp/7369> <http://example.com/emp#name> "SMITH" .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/job/CLERK> .
_:Department10 <http://example.com/dept#COMPANY> "EXAMPLE Corporation" .
_:Department10 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Department10 <http://example.com/dept#location> "NEW YORK" .
_:Department10 <http://example.com/dept#name> "APPSERVER" .
```

## Triple Diff
```diff
<http://example.com/emp/7369> <http://example.com/emp#c_ref_deptno> _:cb0 .
<http://example.com/emp/7369> <http://example.com/emp#deptNum> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/emp/7369> <http://example.com/emp#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/emp/7369> <http://example.com/emp#emptype> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://example.com/emp#etype> "PART_TIME" .
<http://example.com/emp/7369> <http://example.com/emp#job> "CLERK" .
<http://example.com/emp/7369> <http://example.com/emp#jobtype> <http://example.com/emp/job/CLERK> .
<http://example.com/emp/7369> <http://example.com/emp#name> "SMITH" .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/etype/PART_TIME> .
<http://example.com/emp/7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/emp/job/CLERK> .
_:cb0 <http://example.com/dept#COMPANY> "EXAMPLE Corporation" .
_:cb0 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb0 <http://example.com/dept#location> "NEW YORK" .
_:cb0 <http://example.com/dept#name> "APPSERVER" .
```

SUCCES

```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: ambiguous column name: deptno

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 198, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 530, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):  # type: ignore  [arg-type]
  File "/rdflib_r2r/r2r_store.py", line 652, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1583, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 323, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1452, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1814, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1995, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) ambiguous column name: deptno
[SQL: SELECT anon_1.s AS s, anon_1.p AS p, anon_1.o AS o, anon_1.g AS g 
FROM (SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#location>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" AS o, NULL AS g 
FROM (SELECT ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
       FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#name>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" AS o, NULL AS g 
FROM (SELECT ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
       FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#deptno>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS o, NULL AS g 
FROM (SELECT ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
       FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#c_ref_deptno>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o, NULL AS g 
FROM (SELECT ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
       FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref", (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "deptno" = substr(?,length('Department')+1) AND "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno" UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#jobtype>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."jobTypeURI" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#deptNum>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."deptno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#emptype>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."empTypeURI" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".jobTypeURI AS VARCHAR) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."jobTypeURI" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#etype>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."etype" AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."etype" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#empno>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."empno" AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."empno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empTypeURI AS VARCHAR) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."empTypeURI" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#job>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."job" AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."job" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS".empURI AS VARCHAR) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#name>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."ename" AS o, NULL AS g 
FROM (SELECT ('http://example.com/emp/' || "empno") AS empURI
            , "empno"
            , "ename"
            , ('http://example.com/emp/job/'|| "job") AS jobTypeURI
            , "job"
            , "deptno"
            , ('http://example.com/emp/etype/'|| "etype") AS empTypeURI
            , "etype"
            , ('http://example.com/graph/'|| "job" || '/' || "etype") AS graphURI
       FROM "EMP") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BS"."ename" = ?) AS anon_1]
[parameters: ('_:', 'http://example.com/emp/etype/PART_TIME', '_:', 'http://example.com/emp/etype/PART_TIME', '_:', 'http://example.com/emp/etype/PART_TIME', '<', '>', '_:', 'http://example.com/emp/etype/PART_TIME', '<', '>', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', 'http://example.com/emp/etype/PART_TIME', '<', '>', 'http://example.com/emp/etype/PART_TIME')]
(Background on this error at: https://sqlalche.me/e/14/e3q8)

```