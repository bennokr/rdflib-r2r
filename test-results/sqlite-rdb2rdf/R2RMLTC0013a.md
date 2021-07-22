# R2RMLTC0013a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0013a)
Generation of empty triples from referenced columns that have null values



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 155, in test_rdb2rdf
    sql_query = g_made.store.getSQL("SELECT * WHERE {?s ?p ?o}")
  File "/rdflib_r2r/r2r_store.py", line 1038, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 963, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 875, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 957, in queryPart
    return self.queryBGP(conn, part.triples)
  File "/rdflib_r2r/r2r_store.py", line 713, in queryBGP
    cols = [incols[i] for i in idx]
  File "/rdflib_r2r/r2r_store.py", line 713, in <listcomp>
    cols = [incols[i] for i in idx]
IndexError: list index out of range

```