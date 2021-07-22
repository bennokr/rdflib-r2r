# R2RMLTC0011b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0011b)
M to M relation, by using an additional Triples Map

```diff
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
<http://example.com/sport/110> <http://example.com/id> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/sport/111> <http://example.com/description> "Football" .
<http://example.com/sport/111> <http://example.com/id> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
<http://example.com/sport/112> <http://example.com/id> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://example.com/plays> <http://example.com/sport/110> .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/112> .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://example.com/plays> <http://example.com/sport/111> .
```

SUCCES

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 167, in test_rdb2rdf
    s_triples = sorted(g_made.triples([s, None, None]))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 566, in triples
    query, subforms = self.queryPattern(metadata, pattern)
  File "/rdflib_r2r/r2r_store.py", line 517, in queryPattern
    querysubforms += list(self._triplesmap_select(metadata, tmap, pattern))
  File "/rdflib_r2r/r2r_store.py", line 384, in _triplesmap_select
    s_tm_filter = self.mapping.get_filters(qs, dbtable, self.mapping.spat_tmaps)
  File "/rdflib_r2r/r2r_mapping.py", line 312, in get_filters
    key = dbtable.c[key.replace("__", " ")]
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/base.py", line 1158, in __getitem__
    return self._index[key]
KeyError: 'ID'

```