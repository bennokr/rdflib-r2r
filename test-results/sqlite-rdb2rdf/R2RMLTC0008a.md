
# [R2RMLTC0008a](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0008a)
Generation of triples to a target graph by using rr:graphMap and rr:template

```diff
<http://example.com/Student/10/Venus%20Williams> <http://example.com/Sport> "Tennis" .
<http://example.com/Student/10/Venus%20Williams> <http://example.com/id> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/Student/10/Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES

(also checking pattern queries afterwards: True)
