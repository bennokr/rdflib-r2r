# DirectGraphTC0021
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0021)
Generation of triples for two tables, two primary keys, a foreign key, references all nulls

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
                    '<http://example.com/base/Source#ID>' AS p,
                    '"' || CAST(CAST("Source"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
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
                    '<http://example.com/base/Target#key1attr2>' AS p,
                    "Target"."key1attr2" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key2attr2>' AS p,
                    "Target"."key2attr2" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key2attr1>' AS p,
                    "Target"."key2attr1" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#key1attr1>' AS p,
                    "Target"."key1attr1" AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '_:Target#' || CAST(CAST("Target".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Target#PK>' AS p,
                    '"' || CAST(CAST("Target"."PK" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Target") AS anon_1
```

## Raw ouput triples
```
_:Source#0 <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Source#0 <http://example.com/base/Source#attrA> "K2A21" .
_:Source#0 <http://example.com/base/Source#attrB> "K2A11" .
_:Source#0 <http://example.com/base/Source#ref-attrA;attrB> _:Target#0 .
_:Source#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
_:Source#1 <http://example.com/base/Source#ID> "1101"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Source#1 <http://example.com/base/Source#attrA> "K2A22" .
_:Source#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
_:Source#2 <http://example.com/base/Source#ID> "1102"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Source#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
_:Target#0 <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Target#0 <http://example.com/base/Target#key1attr1> "K1A11" .
_:Target#0 <http://example.com/base/Target#key1attr2> "K1A21" .
_:Target#0 <http://example.com/base/Target#key2attr1> "K2A11" .
_:Target#0 <http://example.com/base/Target#key2attr2> "K2A21" .
_:Target#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
_:Target#1 <http://example.com/base/Target#PK> "1011"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Target#1 <http://example.com/base/Target#key1attr1> "K1A12" .
_:Target#1 <http://example.com/base/Target#key1attr2> "K1A22" .
_:Target#1 <http://example.com/base/Target#key2attr2> "K2A22" .
_:Target#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
_:Target#2 <http://example.com/base/Target#PK> "1012"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Target#2 <http://example.com/base/Target#key1attr1> "K1A13" .
_:Target#2 <http://example.com/base/Target#key1attr2> "K1A23" .
_:Target#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

## Triple Diff
```diff
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A21" .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A11" .
- <http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> <http://example.com/base/Target/PK=1010> .
- <http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
- <http://example.com/base/Source/ID=1101> <http://example.com/base/Source#ID> "1101"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Source/ID=1101> <http://example.com/base/Source#attrA> "K2A22" .
- <http://example.com/base/Source/ID=1101> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
- <http://example.com/base/Source/ID=1102> <http://example.com/base/Source#ID> "1102"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Source/ID=1102> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
- <http://example.com/base/Target/PK=1010> <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr1> "K1A11" .
- <http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr2> "K1A21" .
- <http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr1> "K2A11" .
- <http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr2> "K2A21" .
- <http://example.com/base/Target/PK=1010> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
- <http://example.com/base/Target/PK=1011> <http://example.com/base/Target#PK> "1011"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Target/PK=1011> <http://example.com/base/Target#key1attr1> "K1A12" .
- <http://example.com/base/Target/PK=1011> <http://example.com/base/Target#key1attr2> "K1A22" .
- <http://example.com/base/Target/PK=1011> <http://example.com/base/Target#key2attr2> "K2A22" .
- <http://example.com/base/Target/PK=1011> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
- <http://example.com/base/Target/PK=1012> <http://example.com/base/Target#PK> "1012"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Target/PK=1012> <http://example.com/base/Target#key1attr1> "K1A13" .
- <http://example.com/base/Target/PK=1012> <http://example.com/base/Target#key1attr2> "K1A23" .
- <http://example.com/base/Target/PK=1012> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
+ _:cb0 <http://example.com/base/Source#ID> "1102"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
+ _:cb35c25286a276a3d5a81f2a4af5f9de76408d41c3b71ae95f4078bbdb6026a19c <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb35c25286a276a3d5a81f2a4af5f9de76408d41c3b71ae95f4078bbdb6026a19c <http://example.com/base/Source#attrA> "K2A21" .
+ _:cb35c25286a276a3d5a81f2a4af5f9de76408d41c3b71ae95f4078bbdb6026a19c <http://example.com/base/Source#attrB> "K2A11" .
+ _:cb35c25286a276a3d5a81f2a4af5f9de76408d41c3b71ae95f4078bbdb6026a19c <http://example.com/base/Source#ref-attrA;attrB> _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb .
+ _:cb35c25286a276a3d5a81f2a4af5f9de76408d41c3b71ae95f4078bbdb6026a19c <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
+ _:cb474a9fc2e1dbe19c5f1d5728ebbc0513a052092cce00fc51532e493531061b87 <http://example.com/base/Source#ID> "1101"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb474a9fc2e1dbe19c5f1d5728ebbc0513a052092cce00fc51532e493531061b87 <http://example.com/base/Source#attrA> "K2A22" .
+ _:cb474a9fc2e1dbe19c5f1d5728ebbc0513a052092cce00fc51532e493531061b87 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://example.com/base/Target#key1attr1> "K1A11" .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://example.com/base/Target#key1attr2> "K1A21" .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://example.com/base/Target#key2attr1> "K2A11" .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://example.com/base/Target#key2attr2> "K2A21" .
+ _:cba5864a014692387c3032a8bc02333f5a9a85442e5438c33f14392bcd3f8b64bb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
+ _:cbaf341034c0c5c9c03da196b717f4564d1814811546caafa935c41086ad70c1e5 <http://example.com/base/Target#PK> "1011"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cbaf341034c0c5c9c03da196b717f4564d1814811546caafa935c41086ad70c1e5 <http://example.com/base/Target#key1attr1> "K1A12" .
+ _:cbaf341034c0c5c9c03da196b717f4564d1814811546caafa935c41086ad70c1e5 <http://example.com/base/Target#key1attr2> "K1A22" .
+ _:cbaf341034c0c5c9c03da196b717f4564d1814811546caafa935c41086ad70c1e5 <http://example.com/base/Target#key2attr2> "K2A22" .
+ _:cbaf341034c0c5c9c03da196b717f4564d1814811546caafa935c41086ad70c1e5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
+ _:cbf921d185a44af823d9eecd08085eb0f17c0c6fe22557e5ac9f9be633f769be6f <http://example.com/base/Target#PK> "1012"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cbf921d185a44af823d9eecd08085eb0f17c0c6fe22557e5ac9f9be633f769be6f <http://example.com/base/Target#key1attr1> "K1A13" .
+ _:cbf921d185a44af823d9eecd08085eb0f17c0c6fe22557e5ac9f9be633f769be6f <http://example.com/base/Target#key1attr2> "K1A23" .
+ _:cbf921d185a44af823d9eecd08085eb0f17c0c6fe22557e5ac9f9be633f769be6f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```