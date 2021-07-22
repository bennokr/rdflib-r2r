# R2RMLTC0012b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012b)
Duplicate tuples generate same blank node

```diff
_:cb0 <http://example.com/city> "Madrid" .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
_:cb73b70e4b2d26b1f7c8474f47e210a488b7d883818a502afd8c76cc8b1facee20 <http://example.com/city> "London" .
_:cb73b70e4b2d26b1f7c8474f47e210a488b7d883818a502afd8c76cc8b1facee20 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
```

SUCCES

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 177, in test_rdb2rdf
    o_triples = sorted(g_made.triples([None, None, o]))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 566, in triples
    query, subforms = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 517, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
  File "/rdflib_r2r/r2r_store.py", line 386, in _triplesmap_select
    o_tm_filter = self.mapping.get_filters(qo, dbtable, self.mapping.opat_pomaps)
  File "/rdflib_r2r/r2r_mapping.py", line 294, in get_filters
    key = dbtable.c[pat.field]
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/base.py", line 1158, in __getitem__
    return self._index[key]
KeyError: 'city'

```