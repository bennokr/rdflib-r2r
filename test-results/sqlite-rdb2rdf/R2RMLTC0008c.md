
# [R2RMLTC0008c](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0008c)
Generation of triples by using multiple predicateMaps within a rr:predicateObjectMap

```diff
<http://example.com/Student/10/Venus%20Williams> <http://example.com/name> "Venus Williams" .
<http://example.com/Student/10/Venus%20Williams> <http://xmlns.com/foaf/0.1/name> "Venus Williams" .
```

SUCCES

(also checking pattern queries afterwards: True)
