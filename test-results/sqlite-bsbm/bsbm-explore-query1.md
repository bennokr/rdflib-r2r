# bsbm-explore-query1
[link]([bsbm-explore-query1](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ1))

## Random parameter sample
```
x = "21"^^<http://www.w3.org/2001/XMLSchema#integer>
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature166>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature180>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType18>
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
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature166> . 
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature180> . 
    ?product bsbm:productPropertyNumeric1 ?value1 . 
	FILTER (?value1 > "21"^^<http://www.w3.org/2001/XMLSchema#integer>) 
	}
ORDER BY ?label
LIMIT 10

```

## Goal results
```
bsbm-inst:Product93	"kimonos adaptor lifer"
bsbm-inst:Product28	"multilingual"
```

## Created SQL query
```sql
SELECT DISTINCT anon_1.s AS product,
                anon_1.o AS label
FROM
  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          producttype.label AS o,
          NULL AS g
   FROM producttype
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    product.label AS o,
                    NULL AS g
   FROM product
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    vendor.label AS o,
                    NULL AS g
   FROM vendor
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    productfeature.label AS o,
                    NULL AS g
   FROM productfeature
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producer.label AS o,
                    NULL AS g
   FROM producer) AS anon_1,

  (SELECT productfeatureproduct.product AS product,

     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeature"."nr" = '166'
        AND "productfeatureproduct".productFeature = "productfeature".nr) AS anon_3
   FROM productfeatureproduct) AS anon_2,

  (SELECT product."propertyNum1" AS value1,
          product.nr AS product
   FROM product) AS anon_4,

  (SELECT productfeatureproduct.product AS product,

     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeature"."nr" = '180'
        AND "productfeatureproduct".productFeature = "productfeature".nr) AS anon_6
   FROM productfeatureproduct) AS anon_5,

  (SELECT producttypeproduct.product AS product,

     (SELECT "producttype".nr
      FROM producttype
      WHERE "producttype"."nr" = '18'
        AND "producttypeproduct".productType = "producttype".nr) AS anon_8
   FROM producttypeproduct) AS anon_7
WHERE anon_2.product = anon_4.product
  AND anon_2.product = anon_5.product
  AND anon_2.product = anon_7.product
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_2.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_1.s
  AND (anon_4.value1 > 21)
ORDER BY anon_1.o
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product11	"absolvers pomades"
bsbm-inst:Product84	"acclimating"
bsbm-inst:Product41	"accrued"
bsbm-inst:Product34	"amtrac puckery"
bsbm-inst:Product71	"anesthesiologist"
bsbm-inst:Product2	"anglians"
bsbm-inst:Product86	"anodizes expender elaborately"
bsbm-inst:Product75	"anoxias fruiter"
bsbm-inst:Product9	"anytime conservators flivver"
bsbm-inst:Product58	"bettas swerved deflea"
```

FAIL