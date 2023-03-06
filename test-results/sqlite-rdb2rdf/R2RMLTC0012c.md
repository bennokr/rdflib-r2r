# R2RMLTC0012c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012c)
TriplesMap without subjectMap



```
Traceback (most recent call last):
  File "/rdflib_r2r/r2r_store.py", line 428, in _triplesmap_select
    scolform, stable = next(ss)
StopIteration

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 448, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 608, in triples
    query, subforms = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 555, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
RuntimeError: generator raised StopIteration

```