# R2RMLTC0012d
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012d)
TriplesMap with two subjectMap



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 107, in test_rdb2rdf
    db = setup_engine(engine_name, echo=dbecho)
  File "/tests/util.py", line 27, in setup_engine
    db = create_engine(
  File "<string>", line 2, in create_engine
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 601, in create_engine
    dbapi = dbapi_meth(**dbapi_args)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/dialects/postgresql/psycopg2.py", line 690, in import_dbapi
    import psycopg2
ModuleNotFoundError: No module named 'psycopg2'

```