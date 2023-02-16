# R2RMLTC0000
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0000)
one table, one column, zero rows



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 143, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/compare.py", line 540, in to_isomorphic
    result += graph
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 579, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1606, in addN
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/store.py", line 225, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1606, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 579, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 448, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 613, in triples
    col = ColForm.from_subform(cols, subform).expr()
  File "/rdflib_r2r/r2r_store.py", line 103, in from_subform
    return cls(form, [cols[i] for i in idxs])
  File "/rdflib_r2r/r2r_store.py", line 103, in <listcomp>
    return cls(form, [cols[i] for i in idxs])
IndexError: list index out of range

```