# R2RMLTC0005a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0005a)
Typing of resources

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("IOUs".fname AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';' || replace(replace(replace(replace(replace(replace(CAST("IOUs".lname AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://xmlns.com/foaf/0.1/Person>' AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '<http://example.com/' || replace(replace(replace(replace(replace(replace(CAST("IOUs".fname AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';' || replace(replace(replace(replace(replace(replace(CAST("IOUs".lname AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/owes>' AS p,
                    "IOUs".amount AS o,
                    NULL AS g
   FROM "IOUs") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

## Triple Diff
```diff
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES