# R2RMLTC0012a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012a)
Duplicate tuples generate same blank node

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:' || CAST("IOUs".fname AS VARCHAR) || '_' || CAST("IOUs".lname AS VARCHAR) || '_' || CAST("IOUs".amount AS VARCHAR) AS s,
          '<http://xmlns.com/foaf/0.1/name>' AS p,
          CAST("IOUs".fname AS VARCHAR) || ' ' || CAST("IOUs".lname AS VARCHAR) AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '_:' || CAST("IOUs".fname AS VARCHAR) || '_' || CAST("IOUs".lname AS VARCHAR) || '_' || CAST("IOUs".amount AS VARCHAR) AS s,
                    '<http://example.com/amount>' AS p,
                    "IOUs".amount AS o,
                    NULL AS g
   FROM "IOUs") AS anon_1
```

## Raw ouput triples
```
_:Bob_Smith_30.0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:Bob_Smith_30.0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:Bob_Smith_30.0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Bob_Smith_30.0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Sue_Jones_20.0 <http://example.com/amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:Sue_Jones_20.0 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

## Triple Diff
```diff
_:cb0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://example.com/amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

SUCCES