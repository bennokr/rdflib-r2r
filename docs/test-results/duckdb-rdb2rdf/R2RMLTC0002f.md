# R2RMLTC0002f
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002f)
Two columns mapping, delimited identifiers referenced as regular identifiers



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 124, in test_rdb2rdf
    tuple(g_made)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/graph.py", line 592, in triples
    for (_s, _p, _o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 672, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1412, in execute
    return meth(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 515, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1635, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1844, in _execute_context
    return self._exec_single_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1984, in _exec_single_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2342, in _handle_dbapi_exception
    raise exc_info[1].with_traceback(exc_info[2])
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1965, in _exec_single_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 131, in do_execute
    cursor.execute(statement, parameters, context)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/duckdb_engine/__init__.py", line 93, in execute
    self.c.execute(statement, parameters)
duckdb.ParserException: Parser Error: syntax error at or near "%"
LINE 2: FROM (SELECT %(replace_1)s || replace(replace(replace(replace(replace(replace(CAST("Student".ID AS VARCHAR), %(replace_2)s, %(replace_3)s), %(replace_4)s, %(replace_5)s), %(replace_6)s, %(replace_7)s), %(replace_8)s, %(replace_9)s), %(replace_10)s, %(replace_11)s), %(replace_12)s, %(replace_13)s) || %(param_1)s || replace(replace(replace(replace(replace(replace(CAST("Student".Name AS VARCHAR), %(replace_14)s, %(replace_15)s), %(replace_16)s, %(replace_17)s), %(replace_18)s, %(replace_19)s), %(replace_20)s, %(replace_21)s), %(replace_22)s, %(replace_23)s), %(replace_24)s, %(replace_25)s) || %(param_2)s AS s, '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p, '<http://xmlns.com/foaf/0.1/Person>' AS o, NULL AS g 
FROM "Student" UNION ALL SELECT %(replace_26)s || replace(replace(replace(replace(replace(replace(CAST("Student".ID AS VARCHAR), %(replace_27)s, %(replace_28)s), %(replace_29)s, %(replace_30)s), %(replace_31)s, %(replace_32)s), %(replace_33)s, %(replace_34)s), %(replace_35)s, %(replace_36)s), %(replace_37)s, %(replace_38)s) || %(param_3)s || replace(replace(replace(replace(replace(replace(CAST("Student".Name AS VARCHAR), %(replace_39)s, %(replace_40)s), %(replace_41)s, %(replace_42)s), %(replace_43)s, %(replace_44)s), %(replace_45)s, %(replace_46)s), %(replace_47)s, %(replace_48)s), %(replace_49)s, %(replace_50)s) || %(param_4)s AS s, '<http://example.com/id>' AS p, "Student"."ID" AS o, NULL AS g 
FROM "Student" UNION ALL SELECT %(replace_51)s || replace(replace(replace(replace(replace(replace(CAST("Student".ID AS VARCHAR), %(replace_52)s, %(replace_53)s), %(replace_54)s, %(replace_55)s), %(replace_56)s, %(replace_57)s), %(replace_58)s, %(replace_59)s), %(replace_60)s, %(replace_61)s), %(replace_62)s, %(replace_63)s) || %(param_5)s || replace(replace(replace(replace(replace(replace(CAST("Student".Name AS VARCHAR), %(replace_64)s, %(replace_65)s), %(replace_66)s, %(replace_67)s), %(replace_68)s, %(replace_69)s), %(replace_70)s, %(replace_71)s), %(replace_72)s, %(replace_73)s), %(replace_74)s, %(replace_75)s) || %(param_6)s AS s, '<http://xmlns.com/foaf/0.1/name>' AS p, "Student"."Name" AS o, NULL AS g 
FROM "Student") AS anon_1...
                     ^

```