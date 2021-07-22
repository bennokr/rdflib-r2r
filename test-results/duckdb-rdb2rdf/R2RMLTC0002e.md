# R2RMLTC0002e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002e)
Two columns mapping, an undefined rr:tableName


```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 114, in test_rdb2rdf
    outfile = testcase.path.joinpath(testcase.meta[rdb2rdftest.output])
KeyError: rdflib.term.URIRef('http://purl.org/NET/rdb2rdf-test#output')

```