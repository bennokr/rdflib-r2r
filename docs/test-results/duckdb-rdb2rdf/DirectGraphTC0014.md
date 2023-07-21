# DirectGraphTC0014
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0014)
Generation of direct graph from a database with primary key referencing candidate key



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 110, in test_rdb2rdf
    mapping = R2RMapping.from_db(db)
  File "/rdflib_r2r/r2r_mapping.py", line 91, in from_db
    primary_keys = pk["constrained_columns"] or eval(
  File "<string>", line 1, in <module>
NameError: name 'empno' is not defined

```