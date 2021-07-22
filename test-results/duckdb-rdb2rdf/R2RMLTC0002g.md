# R2RMLTC0002g
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002g)
Two columns mapping, invalid SQL query


```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 107, in test_rdb2rdf
    mapping = R2RMapping(rdflib.Graph().parse(str(mapfile), format=fmt))
  File "/rdflib_r2r/r2r_mapping.py", line 218, in __init__
    t = _get_table(g, tmap)
  File "/rdflib_r2r/r2r_mapping.py", line 39, in _get_table
    view2obj(sqlquery)
  File "/rdflib_r2r/sql_view.py", line 103, in view2obj
    assert selecttok.normalized == 'SELECT'
AssertionError

```