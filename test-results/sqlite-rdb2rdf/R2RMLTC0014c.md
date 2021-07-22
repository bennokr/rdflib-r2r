# R2RMLTC0014c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0014c)
Triplesmaps with rr:inverseExpression, rr:joinCondition, and referencing object maps

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
                    '<http://example.com/dept#COMPANY>' AS p,
                    '"EXAMPLE Corporation"' AS o,
                    NULL AS g
   FROM
     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s,
                    '<http://example.com/dept#deptno>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#positiveInteger>' AS VARCHAR) AS o,
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
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#etype>' AS p,
                    "EMP".etype AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#jobtype>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/emp/job/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".job AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#job>' AS p,
                    "EMP".job AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#deptNum>' AS p,
                    "EMP".deptno AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/emp/job/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".job AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#c_ref_deptno>' AS p,
                    CAST('_:' AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP",

     (SELECT ('Department' || "deptno") AS deptId ,
             "deptno" ,
             "dname" ,
             "loc"
      FROM "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"
   WHERE "EMP"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/emp/etype/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".etype AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#emptype>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/emp/etype/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".etype AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#name>' AS p,
                    "EMP".ename AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/emp/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/emp#empno>' AS p,
                    "EMP".empno AS o,
                    NULL AS g
   FROM "EMP") AS anon_1
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
_:cb0 <http://example.com/dept#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#positiveInteger> .
_:cb0 <http://example.com/dept#location> "NEW YORK" .
_:cb0 <http://example.com/dept#name> "APPSERVER" .
```

SUCCES

```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: ambiguous column name: deptno

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 185, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 606, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1994, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) ambiguous column name: deptno
[SQL: SELECT anon_1.s AS s, anon_1.p AS p, anon_1.o AS o, anon_1.g AS g 
FROM (SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#location>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" AS o, NULL AS g 
FROM (Select ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
         from "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."loc" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#deptno>' AS p, CAST(? AS VARCHAR) || CAST(CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" AS VARCHAR) AS VARCHAR) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM (Select ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
         from "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."deptno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".deptId AS VARCHAR) AS s, '<http://example.com/dept#name>' AS p, "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" AS o, NULL AS g 
FROM (Select ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
         from "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR" 
WHERE "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."dname" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#etype>' AS p, "EMP".etype AS o, NULL AS g 
FROM "EMP" 
WHERE "EMP"."etype" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#job>' AS p, "EMP".job AS o, NULL AS g 
FROM "EMP" 
WHERE "EMP"."job" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#deptNum>' AS p, "EMP".deptno AS o, NULL AS g 
FROM "EMP" 
WHERE "EMP"."deptno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#c_ref_deptno>' AS p, CAST(? AS VARCHAR) || CAST("View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref".deptId AS VARCHAR) AS o, NULL AS g 
FROM "EMP", (Select ('Department' || "deptno") AS deptId
            , "deptno"
            , "dname"
            , "loc"
         from "DEPT") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref" 
WHERE "deptno" = substr(?,length('Department')+1) AND "EMP"."deptno" = "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR_ref"."deptno" UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#empno>' AS p, "EMP".empno AS o, NULL AS g 
FROM "EMP" 
WHERE "EMP"."empno" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://example.com/emp#name>' AS p, "EMP".ename AS o, NULL AS g 
FROM "EMP" 
WHERE "EMP"."ename" = ?) AS anon_1]
[parameters: ('_:', 'Department10', '_:', '"', '"^^<http://www.w3.org/2001/XMLSchema#positiveInteger>', 'Department10', '_:', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '_:', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'Department10', '<', 'http://example.com/emp/', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'Department10')]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```