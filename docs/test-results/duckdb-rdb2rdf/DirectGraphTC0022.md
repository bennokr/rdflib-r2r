# DirectGraphTC0022
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0022)
Generation of triples from two tables, a primary key, a foreign key, references no primary keys

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Source#' || CAST(CAST("Source".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Source>' AS o,
          NULL AS g
   FROM "Source"
   UNION ALL SELECT '_:Source#' || CAST(CAST("Source".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Source#ID>' AS p,
                    '"' || CAST(CAST("Source"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '_:Source#' || CAST(CAST("Source".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Source#attrB>' AS p,
                    "Source"."attrB" AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '_:Source#' || CAST(CAST("Source".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Source#attrA>' AS p,
                    "Source"."attrA" AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '_:Source#' || CAST(CAST("Source".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Source#ref-attrA;attrB>' AS p,
                    '_:Target#' || CAST(CAST("Target_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "Target" AS "Target_ref",
        "Source"
   WHERE "Source"."attrA" = "Target_ref"."key2attr2"
     AND "Source"."attrB" = "Target_ref"."key2attr1"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Target>' AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key2attr1>' AS p,
                    "Target"."key2attr1" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key1attr2>' AS p,
                    "Target"."key1attr2" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key1attr1>' AS p,
                    "Target"."key1attr1" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key2attr2>' AS p,
                    "Target"."key2attr2" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#litattr1>' AS p,
                    '"' || CAST(CAST("Target"."litattr1" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Target") AS anon_1
```

## Raw ouput triples
```
_:Source#0 <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Source#0 <http://example.com/base/Source#attrA> "K2A2" .
_:Source#0 <http://example.com/base/Source#attrB> "K2A1" .
_:Source#0 <http://example.com/base/Source#ref-attrA;attrB> _:Target#0 .
_:Source#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
_:Target#0 <http://example.com/base/Target#key1attr1> "K1A1" .
_:Target#0 <http://example.com/base/Target#key1attr2> "K1A2" .
_:Target#0 <http://example.com/base/Target#key2attr1> "K2A1" .
_:Target#0 <http://example.com/base/Target#key2attr2> "K2A2" .
_:Target#0 <http://example.com/base/Target#litattr1> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Target#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

## Triple Diff
```diff
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A2" .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A1" .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> _:cb0 .
- <http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
+ _:cb0 <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://example.com/base/Source#attrA> "K2A2" .
+ _:cb0 <http://example.com/base/Source#attrB> "K2A1" .
+ _:cb0 <http://example.com/base/Source#ref-attrA;attrB> _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 .
- _:cb0 <http://example.com/base/Target#key1attr1> "K1A1" .
- _:cb0 <http://example.com/base/Target#key1attr2> "K1A2" .
- _:cb0 <http://example.com/base/Target#key2attr1> "K2A1" .
- _:cb0 <http://example.com/base/Target#key2attr2> "K2A2" .
- _:cb0 <http://example.com/base/Target#litattr1> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
- _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://example.com/base/Target#key1attr1> "K1A1" .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://example.com/base/Target#key1attr2> "K1A2" .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://example.com/base/Target#key2attr1> "K2A1" .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://example.com/base/Target#key2attr2> "K2A2" .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://example.com/base/Target#litattr1> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cbab42e92afea1da9f573c2201b623357f4efda45bc4f6dee75de53a0237a1af50 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```