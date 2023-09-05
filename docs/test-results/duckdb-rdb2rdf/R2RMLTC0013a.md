# R2RMLTC0013a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0013a)
Generation of empty triples from referenced columns that have null values

## Created SQL query
```sql
SELECT anon_1."Person"."DateOfBirth" AS o,
       '<http://example.com/BirthDay>' AS p,
       '<http://example.com/Person/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Person"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Person"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Person"."DateOfBirth" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s
FROM
  (SELECT "Person"."DateOfBirth",
          "Person"."ID",
          "Person"."Name",
          "Person"."DateOfBirth"
   FROM "Person") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Person/2/Bob/September%2C%202010> <http://example.com/BirthDay> "September, 2010" .
```

## Triple Diff
```diff
<http://example.com/Person/2/Bob/September%2C%202010> <http://example.com/BirthDay> "September, 2010" .
```

SUCCES