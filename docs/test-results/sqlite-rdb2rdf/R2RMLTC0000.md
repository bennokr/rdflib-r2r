# R2RMLTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0000)
one table, one column, zero rows

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST(anon_1."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
       anon_1."Name" AS o
FROM
  (SELECT "Student"."Name" AS "Name",
          "Student"."Name" AS "Name__1"
   FROM "Student") AS anon_1
```

## Raw ouput triples
```

```

## Triple Diff
```diff

```

SUCCES