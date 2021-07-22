# bsbm-bi-query5
[link]([bsbm-bi-query5](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ5))

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType16>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix rev: <http://purl.org/stuff/rev#>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?country ?product ?nrOfReviews ?avgPrice
  {
    { Select ?country (max(?nrOfReviews) As ?maxReviews)
      {
        { Select ?country ?product (count(?review) As ?nrOfReviews)
          {
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType16> .
            ?review bsbm:reviewFor ?product ;
                    rev:reviewer ?reviewer .
            ?reviewer bsbm:country ?country .
          }
          Group By ?country ?product
        }
      }
      Group By ?country
    }
    { Select ?country ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType16> .
        ?offer bsbm:product ?product .
        ?offer bsbm:price ?price .
      }
      Group By ?country ?product
    }
    { Select ?country ?product (count(?review) As ?nrOfReviews)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType16> .
        ?review bsbm:reviewFor ?product .
        ?review rev:reviewer ?reviewer .
        ?reviewer bsbm:country ?country .
      }
      Group By ?country ?product
    }
    FILTER(?nrOfReviews=?maxReviews)
  }
  Order By desc(?nrOfReviews) ?country ?product

```

## Goal results
```
<http://downlode.org/rdf/iso-3166/countries#US>	bsbm-inst:Product33	"5"^^xsd:integer	"5947.95"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#ES>	bsbm-inst:Product27	"3"^^xsd:integer	"3874.3548484848493"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product22	"2"^^xsd:integer	"4724.523636363636"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product27	"2"^^xsd:integer	"3874.3548484848493"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product33	"2"^^xsd:integer	"5947.95"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product89	"2"^^xsd:integer	"5490.6269999999995"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product27	"2"^^xsd:integer	"3874.3548484848493"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product89	"2"^^xsd:integer	"5490.6269999999995"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#FR>	bsbm-inst:Product33	"2"^^xsd:integer	"5947.95"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#RU>	bsbm-inst:Product33	"2"^^xsd:integer	"5947.95"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#GB>	bsbm-inst:Product27	"1"^^xsd:integer	"3874.3548484848493"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#GB>	bsbm-inst:Product33	"1"^^xsd:integer	"5947.95"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product14	"1"^^xsd:integer	"4780.541666666667"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product27	"1"^^xsd:integer	"3874.3548484848493"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product33	"1"^^xsd:integer	"5947.95"^^xsd:double
```

## Created SQL query
```sql
SELECT anon_1.o AS country,
       '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product,
       anon_1.avg_1 AS "avgPrice",
       anon_2.count_1 AS "nrOfReviews"
FROM
  (SELECT anon_3.o AS o,
          anon_3.max_1 AS max_1,
          anon_4.product AS product,
          anon_4.avg_1 AS avg_1
   FROM
     (SELECT anon_5.o AS o,
             max(count(anon_6.review)) AS max_1
      FROM
        (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                NULL AS g
         FROM person
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                          '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM producer
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                          '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM vendor) AS anon_5,

        (SELECT review.nr AS review,

           (SELECT "product".nr
            FROM product
            WHERE "review".product = "product".nr) AS product
         FROM review) AS anon_6,

        (SELECT
           (SELECT "person".nr
            FROM person
            WHERE "review".person = "person".nr) AS reviewer,
                review.nr AS review
         FROM review) AS anon_7,

        (SELECT producttypeproduct.product AS product,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '16'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_9
         FROM producttypeproduct) AS anon_8
      WHERE anon_5.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(anon_7.reviewer AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
        AND anon_8.product = anon_6.product
        AND anon_6.review = anon_7.review
      GROUP BY anon_5.o,
               anon_8.product,
               anon_5.o) AS anon_3,

     (SELECT anon_10.product AS product,
             avg(CAST(CAST(anon_11.price AS VARCHAR) AS FLOAT)) AS avg_1
      FROM
        (SELECT offer.nr AS offer,

           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product
         FROM offer) AS anon_10,

        (SELECT offer.nr AS offer,
                offer.price AS price
         FROM offer) AS anon_11,

        (SELECT producttypeproduct.product AS product,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '16'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_13
         FROM producttypeproduct) AS anon_12
      WHERE anon_10.offer = anon_11.offer
        AND anon_12.product = anon_10.product
      GROUP BY anon_10.product) AS anon_4) AS anon_1,

  (SELECT anon_14.o AS o,
          anon_15.product AS product,
          count(anon_16.review) AS count_1
   FROM
     (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
             '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
             NULL AS g
      FROM person
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                       NULL AS g
      FROM producer
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                       NULL AS g
      FROM vendor) AS anon_14,

     (SELECT producttypeproduct.product AS product,

        (SELECT "producttype".nr
         FROM producttype
         WHERE "producttype"."nr" = '16'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_17
      FROM producttypeproduct) AS anon_15,

     (SELECT review.nr AS review,

        (SELECT "product".nr
         FROM product
         WHERE "review".product = "product".nr) AS product
      FROM review) AS anon_16,

     (SELECT
        (SELECT "person".nr
         FROM person
         WHERE "review".person = "person".nr) AS reviewer,
             review.nr AS review
      FROM review) AS anon_18
   WHERE anon_14.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(anon_18.reviewer AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
     AND anon_15.product = anon_16.product
     AND anon_16.review = anon_18.review
   GROUP BY anon_14.o,
            anon_15.product) AS anon_2
WHERE anon_1.o = anon_2.o
  AND anon_2.product = anon_1.product
  AND anon_2.count_1 = anon_1.max_1
ORDER BY anon_2.count_1 DESC,
         anon_1.o,
         anon_1.product
```


```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: misuse of aggregate function count()

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 215, in test_bsbm
    made = tuple(graph_rdb.query(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/query.py", line 254, in __len__
    return len(self.bindings)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/query.py", line 185, in _get_bindings
    self._bindings += list(self._genbindings)
  File "/rdflib_r2r/sparql_op.py", line 21, in freeze_bindings
    for bindings in res:
  File "/rdflib_r2r/r2r_store.py", line 1006, in exec
    results = conn.execute(query)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1994, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) misuse of aggregate function count()
[SQL: SELECT anon_1.o AS country, ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS product, anon_1.avg_1 AS "avgPrice", anon_2.count_1 AS "nrOfReviews" 
FROM (SELECT anon_3.o AS o, anon_3.max_1 AS max_1, anon_4.product AS product, anon_4.avg_1 AS avg_1 
FROM (SELECT anon_5.o AS o, max(count(anon_6.review)) AS max_1 
FROM (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM person UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM producer UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM vendor) AS anon_5, (SELECT review.nr AS review, (SELECT "product".nr 
FROM product 
WHERE "review".product = "product".nr) AS product 
FROM review) AS anon_6, (SELECT review.nr AS review, (SELECT "person".nr 
FROM person 
WHERE "review".person = "person".nr) AS reviewer 
FROM review) AS anon_7, (SELECT producttypeproduct.product AS product, (SELECT "producttype".nr 
FROM producttype 
WHERE "producttype"."nr" = ? AND "producttypeproduct".productType = "producttype".nr) AS anon_9 
FROM producttypeproduct) AS anon_8 
WHERE anon_5.s = ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_7.reviewer AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AND anon_8.product = anon_6.product AND anon_6.review = anon_7.review GROUP BY anon_5.o, anon_8.product, anon_5.o) AS anon_3, (SELECT anon_10.product AS product, avg(CAST(CAST(anon_11.price AS VARCHAR) AS FLOAT)) AS avg_1 
FROM (SELECT (SELECT "product".nr 
FROM product 
WHERE "offer".product = "product".nr) AS product, offer.nr AS offer 
FROM offer) AS anon_10, (SELECT offer.price AS price, offer.nr AS offer 
FROM offer) AS anon_11, (SELECT producttypeproduct.product AS product, (SELECT "producttype".nr 
FROM producttype 
WHERE "producttype"."nr" = ? AND "producttypeproduct".productType = "producttype".nr) AS anon_13 
FROM producttypeproduct) AS anon_12 
WHERE anon_12.product = anon_10.product AND anon_10.offer = anon_11.offer GROUP BY anon_10.product) AS anon_4) AS anon_1, (SELECT anon_14.o AS o, anon_15.product AS product, count(anon_16.review) AS count_1 
FROM (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM person UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM producer UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM vendor) AS anon_14, (SELECT producttypeproduct.product AS product, (SELECT "producttype".nr 
FROM producttype 
WHERE "producttype"."nr" = ? AND "producttypeproduct".productType = "producttype".nr) AS anon_17 
FROM producttypeproduct) AS anon_15, (SELECT review.nr AS review, (SELECT "product".nr 
FROM product 
WHERE "review".product = "product".nr) AS product 
FROM review) AS anon_16, (SELECT review.nr AS review, (SELECT "person".nr 
FROM person 
WHERE "review".person = "person".nr) AS reviewer 
FROM review) AS anon_18 
WHERE anon_14.s = ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_18.reviewer AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AND anon_15.product = anon_16.product AND anon_16.review = anon_18.review GROUP BY anon_14.o, anon_15.product) AS anon_2 
WHERE anon_1.o = anon_2.o AND anon_2.product = anon_1.product AND anon_2.count_1 = anon_1.max_1 ORDER BY anon_2.count_1 DESC, anon_1.o, anon_1.product]
[parameters: ('<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '16', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '16', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '16', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```