# DirectGraphTC0014
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0014)
Generation of direct graph from a database with primary key referencing candidate key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/DEPT>' AS o,
          NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#loc>' AS p,
                    "DEPT".loc AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#dname>' AS p,
                    "DEPT".dname AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '_:DEPT#' || CAST(CAST("DEPT".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/DEPT#deptno>' AS p,
                    '"' || CAST(CAST("DEPT".deptno AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "DEPT"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/EMP>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#empno>' AS p,
                    '"' || CAST(CAST("EMP".empno AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#job>' AS p,
                    "EMP".job AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#ename>' AS p,
                    "EMP".ename AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#etype>' AS p,
                    "EMP".etype AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#deptno>' AS p,
                    '"' || CAST(CAST("EMP".deptno AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "EMP"
   UNION ALL SELECT '<EMP/empno=' || replace(replace(replace(replace(replace(replace(CAST("EMP".empno AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/EMP#ref-deptno>' AS p,
                    '_:DEPT#' || CAST(CAST("DEPT_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "EMP",
        "DEPT" AS "DEPT_ref"
   WHERE "EMP"."deptno" = "DEPT_ref"."deptno"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/LIKES>' AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#likedObj>' AS p,
                    "LIKES"."likedObj" AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#id>' AS p,
                    '"' || CAST(CAST("LIKES".id AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "LIKES"
   UNION ALL SELECT '_:LIKES#' || CAST(CAST("LIKES".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/LIKES#likeType>' AS p,
                    "LIKES"."likeType" AS o,
                    NULL AS g
   FROM "LIKES") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ename> "SMITH" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#etype> "PART_TIME" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#job> "CLERK" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ref-deptno> _:DEPT#1 .
<http://example.com/base/EMP/empno=7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/EMP> .
_:DEPT#1 <http://example.com/base/DEPT#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:DEPT#1 <http://example.com/base/DEPT#dname> "APPSERVER" .
_:DEPT#1 <http://example.com/base/DEPT#loc> "NEW YORK" .
_:DEPT#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/DEPT> .
_:LIKES#1 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:LIKES#1 <http://example.com/base/LIKES#likeType> "Playing" .
_:LIKES#1 <http://example.com/base/LIKES#likedObj> "Soccer" .
_:LIKES#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
_:LIKES#2 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:LIKES#2 <http://example.com/base/LIKES#likeType> "Watching" .
_:LIKES#2 <http://example.com/base/LIKES#likedObj> "Basketball" .
_:LIKES#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
```

## Triple Diff
```diff
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#empno> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ename> "SMITH" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#etype> "PART_TIME" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#job> "CLERK" .
<http://example.com/base/EMP/empno=7369> <http://example.com/base/EMP#ref-deptno> _:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa .
<http://example.com/base/EMP/empno=7369> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/EMP> .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#deptno> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#dname> "APPSERVER" .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://example.com/base/DEPT#loc> "NEW YORK" .
_:cb100f97243f76953966c53e8f1ff7b07f9d46415a59de13032ecaa74d1044139fa <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/DEPT> .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#likeType> "Watching" .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://example.com/base/LIKES#likedObj> "Basketball" .
_:cb1b57edfbca0863fa06373259b7527a1bdcc5edccbd18690f987a4b0e4dc4bfa73 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#id> "7369"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#likeType> "Playing" .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://example.com/base/LIKES#likedObj> "Soccer" .
_:cbf819b16b453e71931b516f1cb24ba2ec539a68ac894882deacb0417ae741706d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/LIKES> .
```

SUCCES