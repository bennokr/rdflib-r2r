# R2RMLTC0016b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016b)
Table with datatypes: real and float



```
Traceback (most recent call last):
  File "/tests/util.py", line 45, in create_database
    cursor.execute(sql_script, (), None)
duckdb.ParserException: Parser Error: Type BLOB does not support any modifiers!

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/util.py", line 49, in create_database
    cursor.executescript(sql_script)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 51, in __getattr__
    return getattr(self.c, name)
AttributeError: 'duckdb.DuckDBPyConnection' object has no attribute 'executescript'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 99, in test_rdb2rdf
    create_database(db, testcase.path, testcase.sql_fname)
  File "/tests/util.py", line 51, in create_database
    raise Exception(f"Problem with {path}: {e}")
Exception: Problem with /tests/rdb2rdf-ts/D016-1table1primarykey10columns3rowsSQLdatatypes: 'duckdb.DuckDBPyConnection' object has no attribute 'executescript'

```