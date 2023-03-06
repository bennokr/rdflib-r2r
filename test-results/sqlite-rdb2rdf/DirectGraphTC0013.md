# DirectGraphTC0013
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0013)
Generation of a direct graph from a table with NULL values

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Person>' AS o,
          NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#DateOfBirth>' AS p,
                    "Person"."DateOfBirth" AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Person"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Person"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Person/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Person#Name>' AS p,
                    "Person"."Name" AS o,
                    NULL AS g
   FROM "Person") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#Name> "Alice" .
<http://example.com/base/Person/ID=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#DateOfBirth> "September, 2010" .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#Name> "Bob" .
<http://example.com/base/Person/ID=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

## Triple Diff
```diff
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#ID> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=1> <http://example.com/base/Person#Name> "Alice" .
<http://example.com/base/Person/ID=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#DateOfBirth> "September, 2010" .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#ID> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Person/ID=2> <http://example.com/base/Person#Name> "Bob" .
<http://example.com/base/Person/ID=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Person> .
```

SUCCES