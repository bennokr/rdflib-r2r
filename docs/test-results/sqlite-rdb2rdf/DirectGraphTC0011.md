# DirectGraphTC0011
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0011)
Many to Many relations

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
                    '<http://example.com/base/Sport#Description>' AS p,
                    "Sport"."Description" AS o,
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
                    '<http://example.com/base/Student#FirstName>' AS p,
                    "Student"."FirstName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student#LastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Student_Sport>' AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ID_Student>' AS p,
                    '"' || CAST(CAST("Student_Sport"."ID_Student" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ref-ID_Student>' AS p,
                    '<Student/ID=' || replace(replace(replace(replace(replace(replace(CAST("Student_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Student_Sport",
        "Student" AS "Student_ref"
   WHERE "Student_Sport"."ID_Student" = "Student_ref"."ID"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ref-ID_Sport>' AS p,
                    '<Sport/ID=' || replace(replace(replace(replace(replace(replace(CAST("Sport_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Student_Sport",
        "Sport" AS "Sport_ref"
   WHERE "Student_Sport"."ID_Sport" = "Sport_ref"."ID"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ID_Sport>' AS p,
                    '"' || CAST(CAST("Student_Sport"."ID_Sport" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student_Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#Description> "Tennis" .
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#Description> "Football" .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#Description> "Formula1" .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#FirstName> "Venus" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#LastName> "Williams" .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#LastName> "Alonso" .
<http://example.com/base/Student/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#FirstName> "David" .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#LastName> "Villa" .
<http://example.com/base/Student/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=110> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=10> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=112> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=12> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

## Triple Diff
```diff
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#Description> "Tennis" .
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#Description> "Football" .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#Description> "Formula1" .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#FirstName> "Venus" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#LastName> "Williams" .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#LastName> "Alonso" .
<http://example.com/base/Student/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#FirstName> "David" .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#LastName> "Villa" .
<http://example.com/base/Student/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=110> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=10> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=112> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=12> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

SUCCES