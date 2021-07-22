# bsbm-explore-query5
[link]([bsbm-explore-query5](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ5))

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48>
```

## SPARQL query
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

SELECT DISTINCT ?product ?productLabel
WHERE { 
	?product rdfs:label ?productLabel .
    FILTER (<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48> != ?product)
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48> bsbm:productFeature ?prodFeature .
	?product bsbm:productFeature ?prodFeature .
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48> bsbm:productPropertyNumeric1 ?origProperty1 .
	?product bsbm:productPropertyNumeric1 ?simProperty1 .
	FILTER (?simProperty1 < (?origProperty1 + 120) && ?simProperty1 > (?origProperty1 - 120))
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48> bsbm:productPropertyNumeric2 ?origProperty2 .
	?product bsbm:productPropertyNumeric2 ?simProperty2 .
	FILTER (?simProperty2 < (?origProperty2 + 170) && ?simProperty2 > (?origProperty2 - 170))
}
ORDER BY ?productLabel
LIMIT 5
```

## Goal results
```
bsbm-inst:Product75	"anoxias fruiter"
```

## Created SQL query
```sql
SELECT DISTINCT anon_1.s AS product,
                anon_1.o AS "productLabel"
FROM
  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          vendor.label AS o,
          NULL AS g
   FROM vendor
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    product.label AS o,
                    NULL AS g
   FROM product
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producttype.label AS o,
                    NULL AS g
   FROM producttype
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producer.label AS o,
                    NULL AS g
   FROM producer
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    productfeature.label AS o,
                    NULL AS g
   FROM productfeature) AS anon_1,

  (SELECT product.nr AS product,
          product."propertyNum1" AS "simProperty1",
          product."propertyNum2" AS "simProperty2"
   FROM product) AS anon_2,

  (SELECT
     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS "prodFeature",
          productfeatureproduct.product AS product
   FROM productfeatureproduct) AS anon_3,

  (SELECT
     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS "prodFeature"
   FROM productfeatureproduct
   WHERE "productfeatureproduct"."product" = '48') AS anon_4,

  (SELECT product."propertyNum1" AS "origProperty1"
   FROM product
   WHERE "product"."nr" = '48') AS anon_5,

  (SELECT product."propertyNum2" AS "origProperty2"
   FROM product
   WHERE "product"."nr" = '48') AS anon_6
WHERE anon_2.product = anon_3.product
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_2.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_1.s
  AND anon_4."prodFeature" = anon_3."prodFeature"
  AND anon_1.s != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product48>'
  AND (anon_2."simProperty1" < (anon_5."origProperty1" + 120))
  AND (anon_2."simProperty1" > (anon_5."origProperty1" - 120))
  AND (anon_2."simProperty2" < (anon_6."origProperty2" + 170))
  AND (anon_2."simProperty2" > (anon_6."origProperty2" - 170))
ORDER BY anon_1.o
LIMIT 5
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product75	"anoxias fruiter"
```

SUCCES