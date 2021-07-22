# DirectGraphTC0012
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0012)
Generation of direct graph from a database without primary keys

```diff
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#city> "London" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#fname> "Bob" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#lname> "Smith" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#fname> "Bob" .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#lname> "Smith" .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#fname> "Sue" .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#lname> "Jones" .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#city> "London" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#fname> "Bob" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#lname> "Smith" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#city> "Madrid" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#fname> "Sue" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#lname> "Jones" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#fname> "Bob" .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#lname> "Smith" .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
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
KeyError: 'amount'

```