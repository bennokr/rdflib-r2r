# DirectGraphTC0018
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0018)
Generation of triples by using CHAR datatype column

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    substr("Student"."Name" || '               ', 1, 15) AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
_:Student#1 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#1 <http://example.com/base/Student#Name> "Venus          " .
_:Student#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:Student#2 <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#2 <http://example.com/base/Student#Name> "Fernando       " .
_:Student#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:Student#3 <http://example.com/base/Student#ID> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#3 <http://example.com/base/Student#Name> "David          " .
_:Student#3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
_:cb0 <http://example.com/base/Student#ID> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb0 <http://example.com/base/Student#Name> "David          " .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://example.com/base/Student#Name> "Venus          " .
_:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:cbf0dc47c4127ae186c1dd28ceaa0420e6215a04c104f252d088515d2185d037b9 <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cbf0dc47c4127ae186c1dd28ceaa0420e6215a04c104f252d088515d2185d037b9 <http://example.com/base/Student#Name> "Fernando       " .
_:cbf0dc47c4127ae186c1dd28ceaa0420e6215a04c104f252d088515d2185d037b9 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES