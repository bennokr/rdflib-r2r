# DirectGraphTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0000)
Direct mapping of an empty table

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('_:Student#' AS VARCHAR) || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('_:Student#' AS VARCHAR) || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Triple Diff
```diff

```

SUCCES