# R2RMLTC0020a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0020a)
Generation of triples by using IRI value in columns

```diff
<http://example.com/base/Bob%2FCharles> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/Bob> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/Emily%20Smith> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/http%3A%2F%2Fexample.com%2Fcompany%2FAlice> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/base/path%2F..%2FDanny> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES