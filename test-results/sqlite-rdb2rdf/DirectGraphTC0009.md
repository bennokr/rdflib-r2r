# DirectGraphTC0009
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0009)
Two tables 1 primary key 1 foreign key



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 139, in test_rdb2rdf
    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/compare.py", line 492, in to_isomorphic
    result += graph
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in __iadd__
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in addN
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/store.py", line 225, in addN
    for s, p, o, c in quads:
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 1409, in <genexpr>
    self.store.addN(
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 551, in <genexpr>
    self.addN((s, p, o, self) for s, p, o in other)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/graph.py", line 421, in triples
    for (s, p, o), cg in self.__store.triples((s, p, o), context=self):
  File "/rdflib_r2r/r2r_store.py", line 578, in triples
    rows = list(conn.execute(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1443, in _execute_clauseelement
    compiled_sql, extracted_params, cache_hit = elem._compile_w_cache(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 546, in _compile_w_cache
    compiled_sql = self._compiler(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 581, in _compiler
    return dialect.statement_compiler(dialect, self, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 766, in __init__
    Compiled.__init__(self, dialect, statement, **kwargs)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 455, in __init__
    self.string = self.process(self.statement, **compile_kwargs)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 490, in process
    return obj._compiler_dispatch(self, **kwargs)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/visitors.py", line 81, in _compiler_dispatch
    return meth(self, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 3131, in visit_select
    text = self._compose_select_body(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 3270, in _compose_select_body
    [
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 3271, in <listcomp>
    f._compiler_dispatch(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/visitors.py", line 81, in _compiler_dispatch
    return meth(self, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 2736, in visit_subquery
    return self.visit_alias(subquery, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 2695, in visit_alias
    inner = alias.element._compiler_dispatch(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/visitors.py", line 81, in _compiler_dispatch
    return meth(self, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 1810, in visit_compound_select
    text = (" " + keyword + " ").join(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 1812, in <genexpr>
    c._compiler_dispatch(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/visitors.py", line 81, in _compiler_dispatch
    return meth(self, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 3131, in visit_select
    text = self._compose_select_body(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/compiler.py", line 3287, in _compose_select_body
    if t:
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 3714, in __bool__
    raise TypeError("Boolean value of this clause is not defined")
TypeError: Boolean value of this clause is not defined

```