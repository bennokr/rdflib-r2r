# R2RMLTC0018a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0018a)
Generation of triples by using CHAR datatype column

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://xmlns.com/foaf/0.1/Person>' AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/id>' AS p,
                    "Student"."ID" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://xmlns.com/foaf/0.1/name>' AS p,
                    substr("Student"."Name" || '               ', 1, 15) AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/10> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/10> <http://xmlns.com/foaf/0.1/name> "Venus          " .
<http://example.com/20> <http://example.com/id> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/20> <http://xmlns.com/foaf/0.1/name> "Fernando       " .
<http://example.com/30> <http://example.com/id> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/30> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/30> <http://xmlns.com/foaf/0.1/name> "David          " .
```

## Triple Diff
```diff
<http://example.com/10> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/10> <http://xmlns.com/foaf/0.1/name> "Venus          " .
<http://example.com/20> <http://example.com/id> "20"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/20> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/20> <http://xmlns.com/foaf/0.1/name> "Fernando       " .
<http://example.com/30> <http://example.com/id> "30"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/30> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/30> <http://xmlns.com/foaf/0.1/name> "David          " .
```

SUCCES