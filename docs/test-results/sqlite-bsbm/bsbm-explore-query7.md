# bsbm-explore-query7
[bsbm-explore-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ7)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product86>
currentDate = "2008-05-28"^^<http://www.w3.org/2001/XMLSchema#date>
```

## SPARQL query
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?productLabel ?offer ?price ?vendor ?vendorTitle ?review ?revTitle 
       ?reviewer ?revName ?rating1 ?rating2
WHERE { 
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product86> rdfs:label ?productLabel .
    OPTIONAL {
        ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product86> .
		?offer bsbm:price ?price .
		?offer bsbm:vendor ?vendor .
		?vendor rdfs:label ?vendorTitle .
        ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#DE> .
        ?offer dc:publisher ?vendor . 
        ?offer bsbm:validTo ?date .
        FILTER (?date > "2008-05-28"^^<http://www.w3.org/2001/XMLSchema#date> )
    }
    OPTIONAL {
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product86> .
	?review rev:reviewer ?reviewer .
	?reviewer foaf:name ?revName .
	?review dc:title ?revTitle .
    OPTIONAL { ?review bsbm:rating1 ?rating1 . }
    OPTIONAL { ?review bsbm:rating2 ?rating2 . } 
    }
}
```

## Goal results
```
"anodizes expender elaborately"					bsbm-inst:Review419	"sportful travels procreative furies"@en	bsbm-inst:Reviewer22	"Toichi-Pavlya"	"4"^^xsd:integer	"3"^^xsd:integer
"anodizes expender elaborately"					bsbm-inst:Review835	"blearily nonformation eatable obeahs cummers"@en	bsbm-inst:Reviewer43	"Edmund-Nabeela"		"5"^^xsd:integer
"anodizes expender elaborately"					bsbm-inst:Review549	"alginates intercapillary fricassees banzais drudges dought jinns"@en	bsbm-inst:Reviewer28	"Hemanti-Suhaila"	"5"^^xsd:integer	"3"^^xsd:integer
"anodizes expender elaborately"					bsbm-inst:Review605	"unconstitutionally humaner eyrie nonmeasurable pyrotechnics invalidity radiolucency unscrambles misaddresses menstruation unwrapping cadetship encephalogram"@en	bsbm-inst:Reviewer30	"Raymon-Lonni"	"10"^^xsd:integer	
"anodizes expender elaborately"					bsbm-inst:Review227	"degummed gonadic tracheotomize tm abased battered translates sarees legacies gypsying"@en	bsbm-inst:Reviewer12	"Hachiro-Albanwr"	"1"^^xsd:integer	"4"^^xsd:integer
"anodizes expender elaborately"					bsbm-inst:Review786	"barbecues enjoyment grooming mediumistic diarrhea halberd cutpurses sheafs balustrades reexport kanjis impellors sliding"@en	bsbm-inst:Reviewer40	"Aroghetto-Etelani"	"10"^^xsd:integer	
```

## Created SQL query
```sql
SELECT productLabel AS "productLabel",
       offer AS offer,
       vendor AS vendor,
       vendorTitle AS "vendorTitle",
       price AS price,
       review AS review,
       reviewer AS reviewer,
       revTitle AS "revTitle",
       revName AS "revName",
       rating1 AS rating1,
       rating2 AS rating2
FROM
  (SELECT anon_2.productLabel AS "productLabel",
          anon_2.offer AS offer,
          anon_2.vendor AS vendor,
          anon_2.vendorTitle AS "vendorTitle",
          anon_2.price AS price,
          anon_2.date AS date
   FROM
     (SELECT productLabel,
             offer,
             vendor,
             vendorTitle,
             price, date
      FROM
        (SELECT anon_4."productLabel" AS "productLabel"
         FROM
           (SELECT anon_5."productLabel" AS "productLabel"
            FROM
              (SELECT product.label AS "productLabel"
               FROM product
               WHERE "product"."nr" = '86') AS anon_5) AS anon_4
         LEFT OUTER JOIN
           (SELECT anon_7.nr AS nr,
                   anon_8."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
                   anon_9.o AS o,
                   anon_10.price AS price,
                   anon_10.date AS date
            FROM
              (SELECT offer.nr AS nr
               FROM offer,
                    product AS product_ref
               WHERE "product_ref"."nr" = '86'
                 AND "offer".product = "product_ref".nr) AS anon_7,

              (SELECT offer.nr AS nr,
                      "vendor_ref".nr AS """vendor_ref"".nr_1"
               FROM offer,
                    vendor AS vendor_ref
               WHERE "offer".publisher = "vendor_ref".nr) AS anon_8,

              (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                      '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                      producer.label AS o,
                      NULL AS g
               FROM producer
               UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                                product.label AS o,
                                NULL AS g
               FROM product
               UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                                vendor.label AS o,
                                NULL AS g
               FROM vendor) AS anon_9,

              (SELECT offer.price AS price,
                      offer."validTo" AS date,
                      offer.nr AS offer
               FROM offer) AS anon_10,

              (SELECT offer.nr AS nr,
                      "vendor_ref".nr AS """vendor_ref"".nr_2"
               FROM offer,
                    vendor AS vendor_ref
               WHERE "offer".vendor = "vendor_ref".nr) AS anon_11,

              (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                      '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                      CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                      NULL AS g
               FROM producer
               WHERE "producer"."country" = 'DE'
               UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                NULL AS g
               FROM vendor
               WHERE "vendor"."country" = 'DE') AS anon_12
            WHERE anon_7.nr = anon_8.nr
              AND anon_7.nr = anon_11.nr
              AND anon_7.nr = anon_10.offer
              AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_12.s
              AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_9.s
              AND anon_8."""vendor_ref"".nr_1" = anon_11."""vendor_ref"".nr_2") AS anon_6 ON) AS anon_3) AS anon_2
   LEFT OUTER JOIN
     (SELECT review,
             reviewer,
             revTitle,
             revName,
             rating1,
             rating2
      FROM
        (SELECT anon_15.review AS review,
                anon_15.reviewer AS reviewer,
                anon_15.revTitle AS "revTitle",
                anon_15.revName AS "revName",
                anon_15.rating1 AS rating1
         FROM
           (SELECT review,
                   reviewer,
                   revTitle,
                   revName,
                   rating1
            FROM
              (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_17.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review,
                      CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_17."""person_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS reviewer,
                      CAST('"' AS VARCHAR) || CAST(anon_17."revTitle" AS VARCHAR) || CAST('"@en' AS VARCHAR) AS "revTitle",
                      anon_17."revName" AS "revName"
               FROM
                 (SELECT anon_18.nr AS nr,
                         anon_18."""person_ref"".nr_1" AS """person_ref"".nr_1",
                         anon_19."revTitle" AS "revTitle",
                         anon_20."revName" AS "revName"
                  FROM
                    (SELECT review.nr AS nr,
                            "person_ref".nr AS """person_ref"".nr_1"
                     FROM review,
                          person AS person_ref
                     WHERE "review".person = "person_ref".nr) AS anon_18,

                    (SELECT review.nr AS review,
                            CAST(review.title AS VARCHAR) AS "revTitle"
                     FROM review) AS anon_19,

                    (SELECT person.nr AS reviewer,
                            person.name AS "revName"
                     FROM person) AS anon_20,

                    (SELECT review.nr AS nr
                     FROM review,
                          product AS product_ref
                     WHERE "product_ref"."nr" = '86'
                       AND "review".product = "product_ref".nr) AS anon_21
                  WHERE anon_18.nr = anon_21.nr
                    AND anon_18.nr = anon_19.review
                    AND anon_20.reviewer = anon_18."""person_ref"".nr_1") AS anon_17
               LEFT OUTER JOIN
                 (SELECT anon_23.review AS review,
                         anon_23.rating1 AS rating1
                  FROM
                    (SELECT review.nr AS review,
                            review.rating1 AS rating1
                     FROM review) AS anon_23) AS anon_22 ON anon_17.nr = anon_22.review) AS anon_16) AS anon_15
         LEFT OUTER JOIN
           (SELECT anon_25.rating2 AS rating2,
                   anon_25.review AS review
            FROM
              (SELECT review.rating2 AS rating2,
                      review.nr AS review
               FROM review) AS anon_25) AS anon_24 ON anon_15.review = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_24.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)) AS anon_14) AS anon_13 ON) AS anon_1
```


```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: near ")": syntax error

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 242, in test_bsbm
    made = set(graph_rdb.query(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/query.py", line 292, in __iter__
    for b in self._genbindings:
  File "/rdflib_r2r/sparql_op.py", line 21, in freeze_bindings
    for bindings in res:
  File "/rdflib_r2r/r2r_store.py", line 1044, in exec
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
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) near ")": syntax error
[SQL: SELECT productLabel AS "productLabel", offer AS offer, vendor AS vendor, vendorTitle AS "vendorTitle", price AS price, review AS review, reviewer AS reviewer, revTitle AS "revTitle", revName AS "revName", rating1 AS rating1, rating2 AS rating2 
FROM (SELECT anon_2.productLabel AS "productLabel", anon_2.offer AS offer, anon_2.vendor AS vendor, anon_2.vendorTitle AS "vendorTitle", anon_2.date AS date, anon_2.price AS price 
FROM (SELECT productLabel, offer, vendor, vendorTitle, date, price 
FROM (SELECT anon_4."productLabel" AS "productLabel" 
FROM (SELECT anon_5."productLabel" AS "productLabel" 
FROM (SELECT product.label AS "productLabel" 
FROM product 
WHERE "product"."nr" = ?) AS anon_5) AS anon_4 LEFT OUTER JOIN (SELECT anon_7.nr AS nr, anon_8."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1", anon_9.o AS o, anon_10.date AS date, anon_10.price AS price 
FROM (SELECT offer.nr AS nr 
FROM offer, product AS product_ref 
WHERE "product_ref"."nr" = ? AND "offer".product = "product_ref".nr) AS anon_7, (SELECT offer.nr AS nr, "vendor_ref".nr AS """vendor_ref"".nr_1" 
FROM offer, vendor AS vendor_ref 
WHERE "offer".publisher = "vendor_ref".nr) AS anon_8, (SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, producer.label AS o, NULL AS g 
FROM producer UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, product.label AS o, NULL AS g 
FROM product UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www.w3.org/2000/01/rdf-schema#label>' AS p, vendor.label AS o, NULL AS g 
FROM vendor) AS anon_9, (SELECT offer.nr AS offer, offer."validTo" AS date, offer.price AS price 
FROM offer) AS anon_10, (SELECT offer.nr AS nr, "vendor_ref".nr AS """vendor_ref"".nr_2" 
FROM offer, vendor AS vendor_ref 
WHERE "offer".vendor = "vendor_ref".nr) AS anon_11, (SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM producer 
WHERE "producer"."country" = ? UNION ALL SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p, CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS o, NULL AS g 
FROM vendor 
WHERE "vendor"."country" = ?) AS anon_12 
WHERE anon_7.nr = anon_8.nr AND anon_7.nr = anon_11.nr AND anon_7.nr = anon_10.offer AND CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8."""vendor_ref"".nr_1" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) = anon_12.s AND CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8."""vendor_ref"".nr_1" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) = anon_9.s AND anon_8."""vendor_ref"".nr_1" = anon_11."""vendor_ref"".nr_2") AS anon_6 ON ) AS anon_3) AS anon_2 LEFT OUTER JOIN (SELECT review, reviewer, revTitle, revName, rating1, rating2 
FROM (SELECT anon_15.review AS review, anon_15.reviewer AS reviewer, anon_15.revTitle AS "revTitle", anon_15.revName AS "revName", anon_15.rating1 AS rating1 
FROM (SELECT review, reviewer, revTitle, revName, rating1 
FROM (SELECT CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_17.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS review, CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_17."""person_ref"".nr_1" AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR) AS reviewer, CAST(? AS VARCHAR) || CAST(anon_17."revTitle" AS VARCHAR) || CAST(? AS VARCHAR) AS "revTitle", anon_17."revName" AS "revName" 
FROM (SELECT anon_18.nr AS nr, anon_18."""person_ref"".nr_1" AS """person_ref"".nr_1", anon_19."revTitle" AS "revTitle", anon_20."revName" AS "revName" 
FROM (SELECT review.nr AS nr, "person_ref".nr AS """person_ref"".nr_1" 
FROM review, person AS person_ref 
WHERE "review".person = "person_ref".nr) AS anon_18, (SELECT CAST(review.title AS VARCHAR) AS "revTitle", review.nr AS review 
FROM review) AS anon_19, (SELECT person.nr AS reviewer, person.name AS "revName" 
FROM person) AS anon_20, (SELECT review.nr AS nr 
FROM review, product AS product_ref 
WHERE "product_ref"."nr" = ? AND "review".product = "product_ref".nr) AS anon_21 
WHERE anon_18.nr = anon_21.nr AND anon_18.nr = anon_19.review AND anon_20.reviewer = anon_18."""person_ref"".nr_1") AS anon_17 LEFT OUTER JOIN (SELECT anon_23.review AS review, anon_23.rating1 AS rating1 
FROM (SELECT review.nr AS review, review.rating1 AS rating1 
FROM review) AS anon_23) AS anon_22 ON anon_17.nr = anon_22.review) AS anon_16) AS anon_15 LEFT OUTER JOIN (SELECT anon_25.review AS review, anon_25.rating2 AS rating2 
FROM (SELECT review.nr AS review, review.rating2 AS rating2 
FROM review) AS anon_25) AS anon_24 ON anon_15.review = CAST(? AS VARCHAR) || CAST(? AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_24.review AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || CAST(? AS VARCHAR)) AS anon_14) AS anon_13 ON ) AS anon_1]
[parameters: ('86', '86', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'DE', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://downlode.org/rdf/iso-3166/countries#', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 'DE', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '"', '"@en', '86', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>')]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```