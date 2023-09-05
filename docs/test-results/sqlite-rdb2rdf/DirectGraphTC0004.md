# DirectGraphTC0004
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0004)
Two column mapping, generation of a BlankNode subject

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:Student_Sport#' || CAST(CAST("Student_Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student_Sport>' AS o,
          NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '_:Student_Sport#' || CAST(CAST("Student_Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student_Sport#Student>' AS p,
                    "Student_Sport"."Student" AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '_:Student_Sport#' || CAST(CAST("Student_Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student_Sport#Sport>' AS p,
                    "Student_Sport"."Sport" AS o,
                    NULL AS g
   FROM "Student_Sport") AS anon_1
```

## Raw ouput triples
```
_:Student_Sport#1 <http://example.com/base/Student_Sport#Sport> "Tennis" .
_:Student_Sport#1 <http://example.com/base/Student_Sport#Student> "Venus" .
_:Student_Sport#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

## Triple Diff
```diff
_:cb0 <http://example.com/base/Student_Sport#Sport> "Tennis" .
_:cb0 <http://example.com/base/Student_Sport#Student> "Venus" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

SUCCES