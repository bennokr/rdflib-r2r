# R2RMLTC0016d
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016d)
Table with datatypes, boolean conversions

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.anon_2 AS o
FROM
  (SELECT '<http://example.com/Patient' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://example.com/paid>' AS p,
          '"' || CASE "Patient"."PaidInAdvance"
                     WHEN 1 THEN 'true'
                     WHEN 0 THEN 'false'
                 END || '"^^<http://www.w3.org/2001/XMLSchema#boolean>' AS anon_2,
                        NULL AS g
   FROM "Patient"
   UNION ALL SELECT '<http://example.com/Patient' || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://xmlns.com/foaf/0.1/Person>' AS o,
                    NULL AS g
   FROM "Patient") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Patient10> <http://example.com/paid> "false"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient11> <http://example.com/paid> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient12> <http://example.com/paid> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

## Triple Diff
```diff
<http://example.com/Patient10> <http://example.com/paid> "false"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient11> <http://example.com/paid> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient12> <http://example.com/paid> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES