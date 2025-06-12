# rdb2rdf Test Fixes

This document summarizes the current failing tests (see `docs/test-results/rdb2rdf.md`) and outlines the root causes and proposed fixes to make the RDB2RDF and R2RML W3C test suites pass on both SQLite and DuckDB.

## 1. Primary Key Detection and Subject Mapping

**Affected tests:**
- DirectGraphTC0005 (D005)
- DirectGraphTC0012 (D012)
- R2RMLTC0005b (R005b), R2RMLTC0012e (R012e)

**Issue:** The code in `R2RMapping.from_db` relies on `db.dialect.get_pk_constraint` (with a hack to parse the `name` field for DuckDB) to detect primary key columns. This approach is brittle:
- DuckDB reflection often returns incorrect or empty PK info.
- SQLite’s implicit `rowid` can be misinterpreted as a primary key.

**Fix:** Replace the dialect‐based constraint logic with direct inspection of the reflected table’s `primary_key` attribute. For example:
```diff
--- a/rdflib_r2r/r2r_mapping.py
+++ b/rdflib_r2r/r2r_mapping.py
@@     @classmethod
      def from_db(cls, db, baseuri="http://example.com/base/"):
          with db.connect() as conn:
              metadata = MetaData()
              metadata.reflect(conn)
              for tablename, table in metadata.tables.items():
-                # brittle dialect hack:
-                pk = db.dialect.get_pk_constraint(conn, tablename, schema="main")
-                if pk and any(pk.values()):
-                    # duckdb & sqlite special cases...
-                    primary_keys = [...]
-                else:
-                    primary_keys = []
+                # robust PK detection:
+                primary_keys = [c.name for c in table.primary_key.columns]
```
This ensures composite and single-column PKs are detected consistently across SQLite and DuckDB, and removes the need for the ad‐hoc parsing hack.

## 2. Default SQL‐to‐XSD Datatype Mapping

**Affected tests:**
- DirectGraphTC0016 (D016)
- R2RMLTC0016b (R016b), R2RMLTC0016c (R016c)

**Issue:** When no `rr:datatype` or `rr:language` is specified in an object map, SQL values for `REAL`, `FLOAT`, `DATE`, and `TIMESTAMP` columns are emitted as plain literals (or Python‐typed literals), not as typed N3 literals, causing mismatches against the test‐case N3 outputs.

**Fix:** Leverage the existing `XSDToSQL` mapping and `R2RStore.col_n3()` helper to wrap object columns in N3‐typed expressions by default:
```diff
--- a/rdflib_r2r/r2r_store.py
+++ b/rdflib_r2r/r2r_store.py
@@     def _term_map_colforms(...):
                          elif obj:
-                            # default: keep original column expression → plain literal
-                            yield colform, dbtable
+                            # default SQL→XSD mapping when no rr:datatype/language:
+                            dbcol = cls._get_col(dbtable, colname)
+                            # wrap as N3 literal with correct XSD type
+                            yield ColForm.from_expr(cls.col_n3(dbcol)), dbtable
```
This change will produce SQL results like `"2021-01-01"^^<http://www.w3.org/2001/XMLSchema#date>` so that `make_node` parses them into correctly typed `Literal` nodes.

## 3. Null‐Value Filtering for Join Conditions

**Affected tests:**
- R2RMLTC0013a (R013a)

**Issue:** Object maps referencing parent triples via `rr:joinCondition` still emit a triple (often with empty or `None` object) when the child column value is `NULL`.

**Fix:** Augment the WHERE clauses generated for `joinCondition` to filter out `NULL` child‐column values. For example:
```diff
--- a/rdflib_r2r/r2r_store.py
+++ b/rdflib_r2r/r2r_store.py
@@     def _term_map_colforms(...):
                          for join in graph[tmap : rr.joinCondition]:
                              ccol = f'"{dbtable.name}".{graph.value(join, rr.child)}'
                              pcol = f'"{ptable.name}".{graph.value(join, rr.parent)}'
                              joins.append(literal_column(ccol) == literal_column(pcol))
+                             # skip NULL child values
+                            joins.append(literal_column(ccol) != null())
```

## 4. InverseExpression and JoinCondition SQL Generation

**Affected tests:**
- R2RMLTC0014b, R2RMLTC0014c (R014b, R014c)

**Issue:** The method `R2RMapping.inverse_condition()` builds raw `text()` clauses with `str.format` and simple quoting, but:
- Fails to properly quote identifiers with schema/table prefixes.
- Does not support multiple‐field inverse expressions correctly.

**Fix:** Rewrite `inverse_condition` to use SQLAlchemy constructs:
```diff
--- a/rdflib_r2r/r2r_mapping.py
+++ b/rdflib_r2r/r2r_mapping.py
@@     def inverse_condition(self, inverse_expr: str, field_values: Dict) -> ClauseElement:
        # old implementation
        t = text(inverse_expr.format(**col_replace, **param_replace))
        return t.bindparams(**field_values)
+      # new implementation
+      fields = {name: field_values[name]
+                for _, name, _, _ in Formatter().parse(inverse_expr) if name}
+      sql_text = inverse_expr
+      for name in fields:
+          sql_text = sql_text.replace(f"{{{name}}}", f":{name}")
+      clause = text(sql_text)
+      return clause.bindparams(**fields)
```

## 5. DuckDB Row Identifier Support

**Affected tests:**
- Many duckdb‐rdb2rdf failures (e.g., DirectGraphTC0002, R2RMLTC0002a, etc.)

**Issue:** DuckDB tables do not expose a built‐in `rowid` column, so the fallback blank‐node template (`_:TableName#<rowid>`) fails.

**Fix:** In `R2RStore._term_map_colforms`, replace the `".rowid"` fallback with a stable `row_number()` window function, for example:
```diff
--- a/rdflib_r2r/r2r_store.py
+++ b/rdflib_r2r/r2r_store.py
@@     def _term_map_colforms(...):
                      else:
-                        rowid = literal_column(f'"{dbtable.name}".rowid')
-                        yield ColForm(["_:" + dbtable.name + "#", None], [rowid]), dbtable
+                        # DuckDB: generate a stable row identifier
+                        rowid = sqlfunc.row_number().over(order_by=None)
+                        yield ColForm(["_:" + dbtable.name + "#", None], [rowid]), dbtable
```

## 6. Template Parsing Robustness

**Affected tests:**
- R2RMLTC0002a, R2RMLTC0002d, R2RMLTC0003b

**Issue:** The ad‐hoc regex in `_template_to_parser` mishandles escaped braces and nested placeholders, leading to incorrect parser patterns for complex `rr:template` URIs.

**Fix:** Replace the regex‐based approach with a formal `Formatter`‐based parser:
```diff
--- a/rdflib_r2r/r2r_mapping.py
+++ b/rdflib_r2r/r2r_mapping.py
@@     def _template_to_parser(cls, template, irisafe=None):
-      # current regex hack...
+      # new Formatter‐based parser:
+      parts = list(Formatter().parse(template))
+      fields = [fname for _, fname, _, _ in parts if fname]
+      regex = re.escape(template)
+      for fname in fields:
+          regex = regex.replace(re.escape(f"{{{fname}}}"), f"(?P<{fname}>.+?)")
+      return regex
```

---
_Implementing the above changes in_ `rdflib_r2r/r2r_mapping.py` _and_ `rdflib_r2r/r2r_store.py` _should resolve the majority of failing test cases on both SQLite and DuckDB._