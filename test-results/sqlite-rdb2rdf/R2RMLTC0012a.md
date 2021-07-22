# R2RMLTC0012a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012a)
Duplicate tuples generate same blank node

```diff
_:cb0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://example.com/amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

SUCCES