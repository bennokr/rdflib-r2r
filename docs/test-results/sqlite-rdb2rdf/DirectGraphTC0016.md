# DirectGraphTC0016
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0016)
Generation of direct graph from a database with sql datatypes

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Patient>' AS o,
          NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#EntranceDate>' AS p,
                    '"' || replace(CAST("Patient"."EntranceDate" AS VARCHAR), ' ', 'T') || '"^^<http://www.w3.org/2001/XMLSchema#dateTime>' AS anon_2,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#Sex>' AS p,
                    "Patient"."Sex" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#LastName>' AS p,
                    "Patient"."LastName" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#ID>' AS p,
                    '"' || CAST(CAST("Patient"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#Photo>' AS p,
                    "Patient"."Photo" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#Weight>' AS p,
                    "Patient"."Weight" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#PaidInAdvance>' AS p,
                    '"' || CASE "Patient"."PaidInAdvance"
                               WHEN 1 THEN 'true'
                               WHEN 0 THEN 'false'
                           END || '"^^<http://www.w3.org/2001/XMLSchema#boolean>' AS anon_3,
                                  NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#BirthDate>' AS p,
                    '"' || CAST("Patient"."BirthDate" AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#date>' AS anon_4,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#Height>' AS p,
                    "Patient"."Height" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<Patient/ID=' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Patient#FirstName>' AS p,
                    "Patient"."FirstName" AS o,
                    NULL AS g
   FROM "Patient") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#BirthDate> "1981-10-10"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#EntranceDate> "2009-10-10T12:12:22"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#FirstName> "Monica" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Height> "1.65"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#LastName> "Geller" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#PaidInAdvance> "false"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Weight> "80.25"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#BirthDate> "1982-11-12"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#EntranceDate> "2008-11-12T09:45:44"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#FirstName> "Rachel" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Height> "1.7"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#LastName> "Green" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9ffff3fc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Weight> "70.22"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#BirthDate> "1978-04-06"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#EntranceDate> "2007-03-12T02:13:14"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#FirstName> "Chandler" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Height> "1.76"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#LastName> "Bing" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Sex> "male" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Weight> "90.31"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
```

## Triple Diff
```diff
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#BirthDate> "1981-10-10"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#EntranceDate> "2009-10-10T12:12:22"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#FirstName> "Monica" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Height> "1.65"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#LastName> "Geller" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#PaidInAdvance> "false"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Weight> "80.25"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#BirthDate> "1982-11-12"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#EntranceDate> "2008-11-12T09:45:44"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#FirstName> "Rachel" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Height> "1.7"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#LastName> "Green" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9ffff3fc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Weight> "70.22"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#BirthDate> "1978-04-06"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#EntranceDate> "2007-03-12T02:13:14"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#FirstName> "Chandler" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Height> "1.76"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#LastName> "Bing" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Sex> "male" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Weight> "90.31"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
```

SUCCES