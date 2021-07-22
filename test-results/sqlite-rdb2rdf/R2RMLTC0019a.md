
# [R2RMLTC0019a](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0019a)
Generation of triples by using IRI value in columns

```diff
<http://example.com/base/Carlos> <http://xmlns.com/foaf/0.1/name> "Carlos" .
<http://example.com/ns#Jhon> <http://xmlns.com/foaf/0.1/name> "http://example.com/ns#Jhon" .
```

SUCCES

(also checking pattern queries afterwards: True)
