# R2RMLTC0011a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0011a)
M to M relation, by using a SQL query



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 139, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/compare.py", line 492, in to_isomorphic
    result += graph
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in addN
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/store.py", line 225, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 566, in triples
    query, subforms = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 517, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
  File "/rdflib_r2r/r2r_store.py", line 436, in _triplesmap_select
    ocolforms = list(
  File "/rdflib_r2r/r2r_store.py", line 323, in _term_map_colforms
    colform = ColForm.from_template(
  File "/rdflib_r2r/r2r_store.py", line 91, in from_template
    col = _get_col(dbtable, colname, template=True)
  File "/rdflib_r2r/r2r_mapping.py", line 71, in _get_col
    tname = getattr(dbtable, 'original', dbtable).name
AttributeError: 'TextualSelect' object has no attribute 'name'

```