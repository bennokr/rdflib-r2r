
# [R2RMLTC0005a](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0005a)
Typing of resources

```diff
<http://example.com/Bob;Smith> <http://example.com/owes> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Bob;Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Sue;Jones> <http://example.com/owes> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Sue;Jones> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES

(also checking pattern queries afterwards: True)
