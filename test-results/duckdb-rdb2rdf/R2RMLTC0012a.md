# R2RMLTC0012a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012a)
Duplicate tuples generate same blank node

```diff
+ _:cb0 <http://example.com/amount> "30.0" .
- _:cb0 <http://example.com/amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
+ _:cb1e7a578a70e9521702adabc5bf6eb99b18a87eed7c5d4acee7b12e25c97068c5 <http://example.com/amount> "20.0" .
+ _:cb1e7a578a70e9521702adabc5bf6eb99b18a87eed7c5d4acee7b12e25c97068c5 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
- _:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://example.com/amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cb3aa145617de67873918c2ea44d39e730a9457f57aada0ab5afaadfd4384ad0c <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

FAIL
```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 160, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get the full diff

```