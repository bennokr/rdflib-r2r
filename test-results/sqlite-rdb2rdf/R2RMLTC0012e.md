# R2RMLTC0012e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012e)
Default mapping

```diff
_:cb0 <http://example.com/base/IOUs#city> "Madrid" .
_:cb0 <http://example.com/base/IOUs#fname> "Sue" .
_:cb0 <http://example.com/base/IOUs#lname> "Jones" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#fname> "Sue" .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#lname> "Jones" .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#city> "London" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#fname> "Bob" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#lname> "Smith" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#fname> "Bob" .
_:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#lname> "Smith" .
_:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
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
KeyError: 'amount'

```