# R2RMLTC0016c
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016c)
Table with datatypes: date and timestamp

```diff
<http://example.com/Patient10> <http://example.com/birthdate> "1981-10-10"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/Patient10> <http://example.com/entrancedate> "2009-10-10T12:12:22"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient11> <http://example.com/birthdate> "1982-11-12"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/Patient11> <http://example.com/entrancedate> "2008-11-12T09:45:44"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient12> <http://example.com/birthdate> "1978-04-06"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.com/Patient12> <http://example.com/entrancedate> "2007-03-12T02:13:14"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
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