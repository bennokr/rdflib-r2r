# R2RMLTC0002h
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002h)
Two columns mapping, duplicate column name in SELECT



```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 107, in test_rdb2rdf
    mapping = R2RMapping(rdflib.Graph().parse(str(mapfile), format=fmt))
  File "/rdflib_r2r/r2r_mapping.py", line 249, in __init__
    t = _get_table(g, tmap)
  File "/rdflib_r2r/r2r_mapping.py", line 48, in _get_table
    return text(sqlquery).columns(*cols).subquery(tname.strip('"'))
  File "/rdflib_r2r/sql_view.py", line 106, in view2obj
    ex = parse_id(s, from_table)
  File "/rdflib_r2r/sql_view.py", line 83, in parse_id
    op = next(parse_node(l, from_table) for l in ls[0] if not l.ttype == Punct)
  File "/rdflib_r2r/sql_view.py", line 83, in <genexpr>
    op = next(parse_node(l, from_table) for l in ls[0] if not l.ttype == Punct)
  File "/rdflib_r2r/sql_view.py", line 29, in parse_node
    a, b = parse_node(ls[0], from_table), parse_node(ls[-1], from_table)
  File "/rdflib_r2r/sql_view.py", line 59, in parse_node
    return parse_id(ls, from_table)
  File "/rdflib_r2r/sql_view.py", line 96, in parse_id
    raise Exception(f"Problem with SQL Identifier {ls}")
Exception: Problem with SQL Identifier [<Name 'ID' at 0x7FE200AB28E0>]

```