
# DirectGraphTC0014
Generation of direct graph from a database with primary key referencing candidate key

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
