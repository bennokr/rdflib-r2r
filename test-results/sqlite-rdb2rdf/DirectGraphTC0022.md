# DirectGraphTC0022
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0022)
Generation of triples from two tables, a primary key, a foreign key, references no primary keys



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
  File "/rdflib_r2r/r2r_store.py", line 317, in _term_map_colforms
    colform = ColForm.from_expr(_get_col(dbtable, colname))
  File "/rdflib_r2r/r2r_mapping.py", line 67, in _get_col
    return sqlfunc.substr(dbcol + " " * l, 1, l)
NameError: name 'sqlfunc' is not defined

```