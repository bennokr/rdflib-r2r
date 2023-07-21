# DirectGraphTC0023
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0023)
Generation of triples for two tables, two primary keys, two foreign keys, references to a key other than primary key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Source/ID=' || replace(replace(replace(replace(replace(replace(CAST("Source"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Source>' AS o,
          NULL AS g
   FROM "Source"
   UNION ALL SELECT '<Source/ID=' || replace(replace(replace(replace(replace(replace(CAST("Source"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Source#attrA>' AS p,
                    substr("Source"."attrA" || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '<Source/ID=' || replace(replace(replace(replace(replace(replace(CAST("Source"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Source#attrB>' AS p,
                    substr("Source"."attrB" || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '<Source/ID=' || replace(replace(replace(replace(replace(replace(CAST("Source"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Source#ref-attrA;attrB>' AS p,
                    '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target_ref"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Target" AS "Target_ref",
        "Source"
   WHERE "Source"."attrA" = "Target_ref"."key2attr2"
     AND "Source"."attrB" = "Target_ref"."key2attr1"
   UNION ALL SELECT '<Source/ID=' || replace(replace(replace(replace(replace(replace(CAST("Source"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Source#ID>' AS p,
                    '"' || CAST(CAST("Source"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Source"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Target>' AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Target#key2attr2>' AS p,
                    substr("Target".key2attr2 || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Target#key1attr1>' AS p,
                    substr("Target".key1attr1 || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Target#key2attr1>' AS p,
                    substr("Target".key2attr1 || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Target#PK>' AS p,
                    '"' || CAST(CAST("Target"."PK" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Target"
   UNION ALL SELECT '<Target/PK=' || replace(replace(replace(replace(replace(replace(CAST("Target"."PK" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Target#key1attr2>' AS p,
                    substr("Target".key1attr2 || '    ', 1, 4) AS o,
                    NULL AS g
   FROM "Target") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A2" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A1" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> <http://example.com/base/Target/PK=1010> .
<http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr1> "K1A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr2> "K1A2" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr1> "K2A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr2> "K2A2" .
<http://example.com/base/Target/PK=1010> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

## Triple Diff
```diff
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A2" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A1" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> <http://example.com/base/Target/PK=1010> .
<http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr1> "K1A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr2> "K1A2" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr1> "K2A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr2> "K2A2" .
<http://example.com/base/Target/PK=1010> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```

SUCCES