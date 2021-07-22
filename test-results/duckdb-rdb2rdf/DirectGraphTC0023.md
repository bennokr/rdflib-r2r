# DirectGraphTC0023
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0023)
Generation of triples for two tables, two primary keys, two foreign keys, references to a key other than primary key



```
Traceback (most recent call last):
  File "/tests/util.py", line 45, in create_database
    cursor.execute(sql_script, (), None)
RuntimeError: Not implemented Error: Constraint type not handled yet!

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/util.py", line 49, in create_database
    cursor.executescript(sql_script)
TypeError: 'NoneType' object is not callable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 99, in test_rdb2rdf
    create_database(db, testcase.path, testcase.sql_fname)
  File "/tests/util.py", line 51, in create_database
    raise Exception(f"Problem with {path}: {e}")
Exception: Problem with /tests/rdb2rdf-ts/D023-2tables2primarykeys2foreignkeysReferencesToNon-primarykeys: 'NoneType' object is not callable

```