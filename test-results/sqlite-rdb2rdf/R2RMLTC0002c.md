# R2RMLTC0002c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002c)
Two columns mapping, an undefined SQL identifier



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 115, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 448, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 607, in triples
    query, subforms = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 554, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
  File "/rdflib_r2r/r2r_store.py", line 465, in _triplesmap_select
    ocolforms = list(
  File "/rdflib_r2r/r2r_store.py", line 341, in _term_map_colforms
    colform = ColForm.from_expr(cls._get_col(dbtable, colname))
  File "/rdflib_r2r/r2r_store.py", line 290, in _get_col
    dbcol = dbtable.c[colname.strip('"')]
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/base.py", line 1158, in __getitem__
    return self._index[key]
KeyError: 'IDs'

```