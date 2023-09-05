# R2RMLTC0009b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0009b)
Generation of triples to multiple graphs

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<http://example.com/resource/student_' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/ontology/Student>' AS o,
          '<http://example.com/graph/students>' AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/resource/student_' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    "Student"."Name" AS o,
                    '<http://example.com/graph/students>' AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/resource/student_' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/ontology/practises>' AS p,
                    '<http://example.com/resource/sport_' || replace(replace(replace(replace(replace(replace(CAST("Sport_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    '<http://example.com/graph/practise>' AS g
   FROM "Sport" AS "Sport_ref",
        "Student"
   WHERE "Student"."Sport" = "Sport_ref"."ID"
   UNION ALL SELECT '<http://example.com/resource/sport_' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/ontology/Sport>' AS o,
                    '<http://example.com/graph/sports>' AS g
   FROM "Sport"
   UNION ALL SELECT '<http://example.com/resource/sport_' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    "Sport"."Name" AS o,
                    NULL AS g
   FROM "Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/resource/sport_100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Sport> .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> .
<http://example.com/resource/student_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> .
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/resource/student_20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
```

## Triple Diff
```diff
<http://example.com/resource/sport_100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Sport> .
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> .
<http://example.com/resource/student_10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> .
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/resource/student_20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/ontology/Student> .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
```

SUCCES