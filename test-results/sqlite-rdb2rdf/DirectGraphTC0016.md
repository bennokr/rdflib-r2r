# DirectGraphTC0016
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0016)
Generation of direct graph from a database with sql datatypes

```diff
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#BirthDate> "1981-10-10"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#EntranceDate> "2009-10-10T12:12:22"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#FirstName> "Monica" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Height> "1.65"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#LastName> "Geller" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#PaidInAdvance> "false"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=10> <http://example.com/base/Patient#Weight> "80.25"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#BirthDate> "1982-11-12"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#EntranceDate> "2008-11-12T09:45:44"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#FirstName> "Rachel" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Height> "1.7"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#LastName> "Green" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9ffff3fc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Sex> "female" .
<http://example.com/base/Patient/ID=11> <http://example.com/base/Patient#Weight> "70.22"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#BirthDate> "1978-04-06"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#EntranceDate> "2007-03-12T02:13:14"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#FirstName> "Chandler" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Height> "1.76"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#LastName> "Bing" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#PaidInAdvance> "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Photo> "89504e470d0a1a0a0000000d49484452000000050000000508060000008d6f26e50000001c4944415408d763f9fffebfc37f062005c3201284d031f18258cd04000ef535cbd18e0e1f0000000049454e44ae426082"^^<http://www.w3.org/2001/XMLSchema#hexBinary> .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Sex> "male" .
<http://example.com/base/Patient/ID=12> <http://example.com/base/Patient#Weight> "90.31"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/base/Patient/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Patient> .
```

SUCCES

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 172, in test_rdb2rdf
    p_triples = sorted(g_made.triples([None, p, None]))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 578, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/result.py", line 382, in iterrows
    row = make_row(row) if make_row else row
ValueError: Couldn't parse date string 'datetime.date(1981, 10, 10)' - value is not a string.

```