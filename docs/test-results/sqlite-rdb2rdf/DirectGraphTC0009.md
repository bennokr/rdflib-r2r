# DirectGraphTC0009
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0009)
Two tables 1 primary key 1 foreign key

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Sport/ID=' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Sport>' AS o,
          NULL AS g
   FROM "Sport"
   UNION ALL SELECT '<Sport/ID=' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Sport#Name>' AS p,
                    "Sport"."Name" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '<Sport/ID=' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Sport#ID>' AS p,
                    '"' || CAST(CAST("Sport"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Student>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#Name>' AS p,
                    "Student"."Name" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#ref-Sport>' AS p,
                    '<Sport/ID=' || replace(replace(replace(replace(replace(replace(CAST("Sport_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Sport" AS "Sport_ref",
        "Student"
   WHERE "Student"."Sport" = "Sport_ref"."ID"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#Sport>' AS p,
                    '"' || CAST(CAST("Student"."Sport" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#Name> "Tennis" .
<http://example.com/base/Sport/ID=100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ref-Sport> <http://example.com/base/Sport/ID=100> .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#Name> "Demi Moore" .
<http://example.com/base/Student/ID=20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#ID> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=100> <http://example.com/base/Sport#Name> "Tennis" .
<http://example.com/base/Sport/ID=100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#Sport> "100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ref-Sport> <http://example.com/base/Sport/ID=100> .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#ID> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=20> <http://example.com/base/Student#Name> "Demi Moore" .
<http://example.com/base/Student/ID=20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES