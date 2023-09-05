# DirectGraphTC0010
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0010)
Generation of direct graph for table names with spaces

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Country Info#' || CAST(CAST("Country Info".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Country%20Info>' AS o,
          NULL AS g
   FROM "Country Info"
   UNION ALL SELECT '_:Country Info#' || CAST(CAST("Country Info".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Country%20Code>' AS p,
                    '"' || CAST(CAST("Country Info"."Country Code" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT '_:Country Info#' || CAST(CAST("Country Info".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#ISO%203166>' AS p,
                    "Country Info"."ISO 3166" AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT '_:Country Info#' || CAST(CAST("Country Info".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Name>' AS p,
                    "Country Info"."Name" AS o,
                    NULL AS g
   FROM "Country Info") AS anon_1
```

## Raw ouput triples
```
_:Country Info#0 <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Country Info#0 <http://example.com/base/Country%20Info#ISO%203166> "BO" .
_:Country Info#0 <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
_:Country Info#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
_:Country Info#1 <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Country Info#1 <http://example.com/base/Country%20Info#ISO%203166> "IE" .
_:Country Info#1 <http://example.com/base/Country%20Info#Name> "Ireland" .
_:Country Info#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
_:Country Info#2 <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Country Info#2 <http://example.com/base/Country%20Info#ISO%203166> "MF" .
_:Country Info#2 <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
_:Country Info#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
```

## Triple Diff
```diff
- <http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#ISO%203166> "BO" .
- <http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
- <http://example.com/base/Country%20Info/Country%20Code=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
- <http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#ISO%203166> "IE" .
- <http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Name> "Ireland" .
- <http://example.com/base/Country%20Info/Country%20Code=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
- <http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#ISO%203166> "MF" .
- <http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
- <http://example.com/base/Country%20Info/Country%20Code=3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
+ _:cb0 <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://example.com/base/Country%20Info#ISO%203166> "MF" .
+ _:cb0 <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
+ _:cbab6c2c7798d8af874508dbdce5550932f82e00611ad50e54c899adb86732cfa2 <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cbab6c2c7798d8af874508dbdce5550932f82e00611ad50e54c899adb86732cfa2 <http://example.com/base/Country%20Info#ISO%203166> "IE" .
+ _:cbab6c2c7798d8af874508dbdce5550932f82e00611ad50e54c899adb86732cfa2 <http://example.com/base/Country%20Info#Name> "Ireland" .
+ _:cbab6c2c7798d8af874508dbdce5550932f82e00611ad50e54c899adb86732cfa2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
+ _:cbe540d7ec1ebef7d3a61803420287e23b5c9619364333cd3767b454013a35f6ab <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cbe540d7ec1ebef7d3a61803420287e23b5c9619364333cd3767b454013a35f6ab <http://example.com/base/Country%20Info#ISO%203166> "BO" .
+ _:cbe540d7ec1ebef7d3a61803420287e23b5c9619364333cd3767b454013a35f6ab <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
+ _:cbe540d7ec1ebef7d3a61803420287e23b5c9619364333cd3767b454013a35f6ab <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```