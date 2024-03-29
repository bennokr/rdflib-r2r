# bsbm-explore-query3
[bsbm-explore-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ3)

## Random parameter sample
```
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature7>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature278>
x = "341"^^<http://www.w3.org/2001/XMLSchema#integer>
y = "401"^^<http://www.w3.org/2001/XMLSchema#integer>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7>
```

## SPARQL query
```sparql
PREFIX bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?product ?label
WHERE {
    ?product rdfs:label ?label .
    ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7> .
	?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature7> .
	?product bsbm:productPropertyNumeric1 ?p1 .
	FILTER ( ?p1 > "341"^^<http://www.w3.org/2001/XMLSchema#integer> ) 
	?product bsbm:productPropertyNumeric3 ?p3 .
	FILTER (?p3 < "401"^^<http://www.w3.org/2001/XMLSchema#integer> )
    OPTIONAL { 
        ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature278> .
        ?product rdfs:label ?testVar }
    FILTER (!bound(?testVar)) 
}
ORDER BY ?label
LIMIT 10


```

## Goal results
```
bsbm-inst:Product45	"unstacks"
bsbm-inst:Product61	"doctrines agoras axil"
```

## Created SQL query
```sql
SELECT product AS product,
       label AS label
FROM
  (SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_2.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product,
          anon_2.o AS label,
          anon_2."propertyNum1" AS p1,
          anon_2."propertyNum3" AS p3
   FROM
     (SELECT anon_3.product AS product,
             anon_4.o AS o,
             anon_5."propertyNum1" AS "propertyNum1",
             anon_5."propertyNum3" AS "propertyNum3"
      FROM
        (SELECT productfeatureproduct.product AS product
         FROM productfeatureproduct,
              productfeature AS productfeature_ref
         WHERE "productfeature_ref"."nr" = '7'
           AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_3,

        (SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                productfeature.label AS o,
                NULL AS g
         FROM productfeature
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          producttype.label AS o,
                          NULL AS g
         FROM producttype
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          producer.label AS o,
                          NULL AS g
         FROM producer
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          product.label AS o,
                          NULL AS g
         FROM product
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          vendor.label AS o,
                          NULL AS g
         FROM vendor) AS anon_4,

        (SELECT product."propertyNum1" AS "propertyNum1",
                product."propertyNum3" AS "propertyNum3",
                product.nr AS nr
         FROM product) AS anon_5,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype AS producttype_ref
         WHERE "producttype_ref"."nr" = '7'
           AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_6
      WHERE anon_3.product = anon_6.product
        AND anon_3.product = anon_5.nr
        AND '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_3.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_4.s) AS anon_2
   LEFT OUTER JOIN
     (SELECT anon_8.product AS product,
             anon_9.label AS label
      FROM
        (SELECT productfeatureproduct.product AS product
         FROM productfeatureproduct,
              productfeature AS productfeature_ref
         WHERE "productfeature_ref"."nr" = '278'
           AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_8,

        (SELECT productfeature.nr AS nr,
                productfeature.label AS label
         FROM productfeature) AS anon_9
      WHERE '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_8.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(anon_9.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>') AS anon_7 ON anon_2.product = anon_7.product) AS anon_1
WHERE (p1 > 341)
  AND (p3 < 401)
  AND testVar IS NOT NULL
ORDER BY label
LIMIT 10
```


```
Traceback (most recent call last):
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such column: testVar

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 242, in test_bsbm
    made = set(graph_rdb.query(query))
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/rdflib/query.py", line 300, in __iter__
    for b in self._genbindings:
  File "/rdflib_r2r/sparql_op.py", line 21, in freeze_bindings
    for bindings in res:
  File "/rdflib_r2r/r2r_store.py", line 1103, in exec
    results = conn.execute(query)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1583, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/sql/elements.py", line 323, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1452, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1814, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1995, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1771, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/envs/rdf/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such column: testVar
[SQL: SELECT product AS product, label AS label 
FROM (SELECT ? || replace(replace(replace(replace(replace(replace(CAST(anon_2.product AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS product, anon_2.o AS label, anon_2."propertyNum3" AS p3, anon_2."propertyNum1" AS p1 
FROM (SELECT anon_3.product AS product, anon_4.o AS o, anon_5."propertyNum3" AS "propertyNum3", anon_5."propertyNum1" AS "propertyNum1" 
FROM (SELECT productfeatureproduct.product AS product 
FROM productfeatureproduct, productfeature AS productfeature_ref 
WHERE "productfeature_ref"."nr" = ? AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_3, (SELECT ? || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, productfeature.label AS o, NULL AS g 
FROM productfeature UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, producttype.label AS o, NULL AS g 
FROM producttype UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, producer.label AS o, NULL AS g 
FROM producer UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, product.label AS o, NULL AS g 
FROM product UNION ALL SELECT ? || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, vendor.label AS o, NULL AS g 
FROM vendor) AS anon_4, (SELECT product.nr AS nr, product."propertyNum3" AS "propertyNum3", product."propertyNum1" AS "propertyNum1" 
FROM product) AS anon_5, (SELECT producttypeproduct.product AS product 
FROM producttypeproduct, producttype AS producttype_ref 
WHERE "producttype_ref"."nr" = ? AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_6 
WHERE anon_3.product = anon_6.product AND anon_3.product = anon_5.nr AND ? || replace(replace(replace(replace(replace(replace(CAST(anon_3.product AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = anon_4.s) AS anon_2 LEFT OUTER JOIN (SELECT anon_8.product AS product, anon_9.label AS label 
FROM (SELECT productfeatureproduct.product AS product 
FROM productfeatureproduct, productfeature AS productfeature_ref 
WHERE "productfeature_ref"."nr" = ? AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_8, (SELECT productfeature.nr AS nr, productfeature.label AS label 
FROM productfeature) AS anon_9 
WHERE ? || replace(replace(replace(replace(replace(replace(CAST(anon_8.product AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = ? || replace(replace(replace(replace(replace(replace(CAST(anon_9.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ?) AS anon_7 ON anon_2.product = anon_7.product) AS anon_1 
WHERE (p1 > ?) AND (p3 < ?) AND testVar IS NOT NULL ORDER BY label
 LIMIT ? OFFSET ?]
[parameters: ('<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '7', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '7', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '278', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 341, 401, 10, 0)]
(Background on this error at: https://sqlalche.me/e/14/e3q8)

```