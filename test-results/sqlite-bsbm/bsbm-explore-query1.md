# bsbm-explore-query1
[bsbm-explore-query1](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ1)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType18>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature142>
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature816>
x = "158"^^<http://www.w3.org/2001/XMLSchema#integer>
```

## SPARQL query
```sparql
PREFIX bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?product ?label
WHERE { 
    ?product rdfs:label ?label .
    ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType18> .
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature816> . 
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature142> . 
    ?product bsbm:productPropertyNumeric1 ?value1 . 
	FILTER (?value1 > "158"^^<http://www.w3.org/2001/XMLSchema#integer>) 
	}
ORDER BY ?label
LIMIT 10

```

## Goal results
```
bsbm-inst:Product91	"prelate"
```

## Created SQL query
```sql
SELECT DISTINCT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS product,
                anon_2.o AS label
FROM
  (SELECT producttypeproduct.product AS product
   FROM producttypeproduct,
        producttype AS producttype_ref
   WHERE "producttype_ref"."nr" = '18'
     AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_1,

  (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          productfeature.label AS o,
          NULL AS g
   FROM productfeature
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producttype.label AS o,
                    NULL AS g
   FROM producttype
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
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
   FROM vendor) AS anon_2,

  (SELECT productfeatureproduct.product AS product
   FROM productfeatureproduct,
        productfeature AS productfeature_ref
   WHERE "productfeature_ref"."nr" = '142'
     AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_3,

  (SELECT productfeatureproduct.product AS product
   FROM productfeatureproduct,
        productfeature AS productfeature_ref
   WHERE "productfeature_ref"."nr" = '816'
     AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_4,

  (SELECT product.nr AS product,
          product."propertyNum1" AS value1
   FROM product) AS anon_5
WHERE anon_1.product = anon_3.product
  AND anon_1.product = anon_4.product
  AND anon_1.product = anon_5.product
  AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_2.s
  AND (anon_5.value1 > 158)
ORDER BY anon_2.o
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product91	"prelate"
```

SUCCES