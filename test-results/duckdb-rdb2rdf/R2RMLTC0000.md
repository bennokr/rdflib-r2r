# R2RMLTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0000)
one table, one column, zero rows

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       anon_1.p AS o,
       CAST('<' AS VARCHAR) || CAST('http://example.com/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.o AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s
FROM
  (SELECT "Student"."Name" AS p,
          "Student"."Name" AS o
   FROM "Student") AS anon_1
```

## Triple Diff
```diff

```

SUCCES