# R2RMLTC0009a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0009a)
Generation of triples from foreign key relations

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/resource/student_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://xmlns.com/foaf/0.1/name>' AS p,
          "Student"."Name" AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/resource/student_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/ontology/practises>' AS p,
                    CAST('<' AS VARCHAR) || CAST('http://example.com/resource/sport_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student",
        "Sport" AS "Sport_ref"
   WHERE "Student"."Sport" = "Sport_ref"."ID"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/resource/sport_' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    "Sport"."Name" AS o,
                    NULL AS g
   FROM "Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> .
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
```

## Triple Diff
```diff
<http://example.com/resource/sport_100> <http://www.w3.org/2000/01/rdf-schema#label> "Tennis" .
<http://example.com/resource/student_10> <http://example.com/ontology/practises> <http://example.com/resource/sport_100> .
<http://example.com/resource/student_10> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
<http://example.com/resource/student_20> <http://xmlns.com/foaf/0.1/name> "Demi Moore" .
```

SUCCES