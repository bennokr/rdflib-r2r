# R2RMLTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0000)
one table, one column, zero rows

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
       anon_1."Student"."Name" AS o,
       '<http://xmlns.com/foaf/0.1/name>' AS p
FROM
  (SELECT "Student"."Name",
          "Student"."Name"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```

```

## Triple Diff
```diff

```

SUCCES