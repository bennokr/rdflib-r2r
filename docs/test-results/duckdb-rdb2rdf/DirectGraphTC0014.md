# DirectGraphTC0014
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0014)
Generation of direct graph from a database with primary key referencing candidate key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/LIKES>' AS o,
          NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#likeType>' AS p,
                    "LIKES"."likeType" AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#likedObj>' AS p,
                    "LIKES"."likedObj" AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#id>' AS p,
                    '"' || CAST(CAST("LIKES"."id" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/EMP>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#job>' AS p,
                    "EMP"."job" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#etype>' AS p,
                    "EMP"."etype" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#ename>' AS p,
                    "EMP"."ename" AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#ref-deptno>' AS p,
                    '_:DEPT#' || CAST(CAST("DEPT_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP",
        "DEPT" AS "DEPT_ref"
   WHERE "EMP"."deptno" = "DEPT_ref"."deptno"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#empno>' AS p,
                    '"' || CAST(CAST("EMP"."empno" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:EMP#' || CAST(CAST("EMP".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/EMP#deptno>' AS p,
                    '"' || CAST(CAST("EMP"."deptno" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/DEPT>' AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#loc>' AS p,
                    "DEPT"."loc" AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#deptno>' AS p,
                    '"' || CAST(CAST("DEPT"."deptno" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#dname>' AS p,
                    "DEPT"."dname" AS o,
                    NULL AS g
   FROM "DEPT") AS anon_1
```

## Raw ouput triples
```
_:DEPT#0 <http://example.com/base/DEPT#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:DEPT#0 <http://example.com/base/DEPT#dname> "APPSERVER" .
_:DEPT#0 <http://example.com/base/DEPT#loc> "NEW YORK" .
_:DEPT#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/DEPT> .
_:EMP#0 <http://example.com/base/EMP#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:EMP#0 <http://example.com/base/EMP#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:EMP#0 <http://example.com/base/EMP#ename> "SMITH" .
_:EMP#0 <http://example.com/base/EMP#etype> "PART_TIME" .
_:EMP#0 <http://example.com/base/EMP#job> "CLERK" .
_:EMP#0 <http://example.com/base/EMP#ref-deptno> _:DEPT#0 .
_:EMP#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/EMP> .
_:LIKES#0 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:LIKES#0 <http://example.com/base/LIKES#likeType> "Playing" .
_:LIKES#0 <http://example.com/base/LIKES#likedObj> "Soccer" .
_:LIKES#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
_:LIKES#1 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:LIKES#1 <http://example.com/base/LIKES#likeType> "Watching" .
_:LIKES#1 <http://example.com/base/LIKES#likedObj> "Basketball" .
_:LIKES#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
```

## Triple Diff
```diff
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ename> "SMITH" .
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#etype> "PART_TIME" .
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#job> "CLERK" .
- <http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ref-deptno> _:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa .
- <http://example.com/base/EMP/empno=7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/EMP> .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#dname> "APPSERVER" .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#loc> "NEW YORK" .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/DEPT> .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#ename> "SMITH" .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#etype> "PART_TIME" .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#job> "CLERK" .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://example.com/base/EMP#ref-deptno> _:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa .
+ _:cb17a5a68caaafa03fab7e2aaf509de2cee61ff3518fa66665853f4ac3f7a058295 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/EMP> .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#likeType> "Watching" .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#likedObj> "Basketball" .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#likeType> "Playing" .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#likedObj> "Soccer" .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```