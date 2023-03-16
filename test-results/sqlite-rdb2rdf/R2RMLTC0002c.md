# R2RMLTC0002c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002c)
Two columns mapping, an undefined SQL identifier



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 530, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):  # type: ignore  [arg-type]
  File "/rdflib_r2r/r2r_store.py", line 634, in triples
    query, (s,p,o,g) = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 580, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
  File "/rdflib_r2r/r2r_store.py", line 482, in _triplesmap_select
    ocolforms = list(
  File "/rdflib_r2r/r2r_store.py", line 357, in _term_map_colforms
    colform = ColForm.from_expr(cls._get_col(dbtable, colname))
  File "/rdflib_r2r/r2r_store.py", line 306, in _get_col
    dbcol = dbtable.c[colname.strip('"')]
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/base.py", line 1192, in __getitem__
    return self._index[key]
KeyError: 'IDs'

```