# bsbm-explore-query5
[bsbm-explore-query5](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ5)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61>
```

## SPARQL query
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

SELECT DISTINCT ?product ?productLabel
WHERE { 
	?product rdfs:label ?productLabel .
    FILTER (<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61> != ?product)
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61> bsbm:productFeature ?prodFeature .
	?product bsbm:productFeature ?prodFeature .
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61> bsbm:productPropertyNumeric1 ?origProperty1 .
	?product bsbm:productPropertyNumeric1 ?simProperty1 .
	FILTER (?simProperty1 < (?origProperty1 + 120) && ?simProperty1 > (?origProperty1 - 120))
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61> bsbm:productPropertyNumeric2 ?origProperty2 .
	?product bsbm:productPropertyNumeric2 ?simProperty2 .
	FILTER (?simProperty2 < (?origProperty2 + 170) && ?simProperty2 > (?origProperty2 - 170))
}
ORDER BY ?productLabel
LIMIT 5
```

## Goal results
```
bsbm-inst:Product18	"liter"
bsbm-inst:Product95	"edgers defensiveness"
bsbm-inst:Product16	"puppydoms"
```

## Created SQL query
```sql
SELECT DISTINCT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS product,
                anon_2.o AS "productLabel"
FROM
  (SELECT productfeatureproduct.product AS product,
          "productfeature_ref".nr AS """productfeature_ref"".nr_1"
   FROM productfeatureproduct,
        productfeature AS productfeature_ref
   WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_1,

  (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          product.label AS o,
          NULL AS g
   FROM product
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producer.label AS o,
                    NULL AS g
   FROM producer
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    productfeature.label AS o,
                    NULL AS g
   FROM productfeature
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    vendor.label AS o,
                    NULL AS g
   FROM vendor
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producttype.label AS o,
                    NULL AS g
   FROM producttype) AS anon_2,

  (SELECT "productfeature_ref".nr AS """productfeature_ref"".nr_2"
   FROM productfeatureproduct,
        productfeature AS productfeature_ref
   WHERE "productfeatureproduct"."product" = '61'
     AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_3,

  (SELECT product.nr AS product,
          product."propertyNum2" AS "simProperty2",
          product."propertyNum1" AS "simProperty1"
   FROM product) AS anon_4,

  (SELECT product."propertyNum1" AS "origProperty1"
   FROM product
   WHERE "product"."nr" = '61') AS anon_5,

  (SELECT product."propertyNum2" AS "origProperty2"
   FROM product
   WHERE "product"."nr" = '61') AS anon_6
WHERE anon_3."""productfeature_ref"".nr_2" = anon_1."""productfeature_ref"".nr_1"
  AND anon_1.product = anon_4.product
  AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_2.s
  AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product61>'
  AND (anon_4."simProperty1" < (anon_5."origProperty1" + 120))
  AND (anon_4."simProperty1" > (anon_5."origProperty1" - 120))
  AND (anon_4."simProperty2" < (anon_6."origProperty2" + 170))
  AND (anon_4."simProperty2" > (anon_6."origProperty2" - 170))
ORDER BY anon_2.o
LIMIT 5
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product18	"liter"
bsbm-inst:Product95	"edgers defensiveness"
bsbm-inst:Product16	"puppydoms"
```

SUCCES