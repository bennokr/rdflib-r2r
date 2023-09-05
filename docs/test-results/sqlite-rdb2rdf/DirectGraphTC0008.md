# DirectGraphTC0008
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0008)
Generation of direct graph from a table with composite primary key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Name=' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Name=' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#Sport>' AS p,
                    "Student"."Sport" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Name=' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Name=' || replace(replace(replace(replace(replace(replace(CAST("Student"."Name" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Sport> "Tennis" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Sport> "Tennis" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES