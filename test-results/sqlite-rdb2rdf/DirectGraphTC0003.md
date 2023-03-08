# DirectGraphTC0003
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0003)
Three columns mapping, generation of a BlankNode

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
                    '<http://example.com/base/Student#FirstName>' AS p,
                    "Student"."FirstName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('_:Student#' AS VARCHAR) || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#LastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('_:Student#' AS VARCHAR) || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
_:Student#1 <http://example.com/base/Student#FirstName> "Venus" .
_:Student#1 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#1 <http://example.com/base/Student#LastName> "Williams" .
_:Student#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
_:cb0 <http://example.com/base/Student#FirstName> "Venus" .
_:cb0 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb0 <http://example.com/base/Student#LastName> "Williams" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES