# R2RMLTC0016a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016a)
Table with datatypes: string and integer

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://example.com/gender>' AS p,
          "Patient"."Sex" AS o,
          NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/id>' AS p,
                    "Patient"."ID" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/lastName>' AS p,
                    "Patient"."LastName" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/firstName>' AS p,
                    "Patient"."FirstName" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient/' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://xmlns.com/foaf/0.1/Person>' AS o,
                    NULL AS g
   FROM "Patient") AS anon_1
```

## Triple Diff
```diff
<http://example.com/Patient/10> <http://example.com/firstName> "Monica" .
<http://example.com/Patient/10> <http://example.com/gender> "female" .
<http://example.com/Patient/10> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/Patient/10> <http://example.com/lastName> "Geller" .
<http://example.com/Patient/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient/11> <http://example.com/firstName> "Rachel" .
<http://example.com/Patient/11> <http://example.com/gender> "female" .
<http://example.com/Patient/11> <http://example.com/id> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/Patient/11> <http://example.com/lastName> "Green" .
<http://example.com/Patient/11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient/12> <http://example.com/firstName> "Chandler" .
<http://example.com/Patient/12> <http://example.com/gender> "male" .
<http://example.com/Patient/12> <http://example.com/id> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/Patient/12> <http://example.com/lastName> "Bing" .
<http://example.com/Patient/12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES