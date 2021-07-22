
# [bsbm-explore-query1]([bsbm-explore-query1](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ1))

## Random parameter sample
```
x = "114"^^<http://www.w3.org/2001/XMLSchema#integer>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9>
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature351>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature349>
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
    ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> .
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature351> . 
    ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature349> . 
    ?product bsbm:productPropertyNumeric1 ?value1 . 
	FILTER (?value1 > "114"^^<http://www.w3.org/2001/XMLSchema#integer>) 
	}
ORDER BY ?label
LIMIT 10

```

## Goal results
```
bsbm-inst:Product56	"pseudointellectuals"
```

## Created SQL query
```sql
SELECT DISTINCT anon_1.s AS product,
                anon_1.o AS label
FROM
  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
          vendor.label AS o,
          NULL AS g
   FROM vendor
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producer.label AS o,
                    NULL AS g
   FROM producer
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    producttype.label AS o,
                    NULL AS g
   FROM producttype
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    product.label AS o,
                    NULL AS g
   FROM product
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                    productfeature.label AS o,
                    NULL AS g
   FROM productfeature) AS anon_1,

  (SELECT productfeatureproduct.product AS product,

     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeature"."nr" = '349'
        AND "productfeatureproduct".productFeature = "productfeature".nr) AS anon_3
   FROM productfeatureproduct) AS anon_2,

  (SELECT productfeatureproduct.product AS product,

     (SELECT "productfeature".nr
      FROM productfeature
      WHERE "productfeature"."nr" = '351'
        AND "productfeatureproduct".productFeature = "productfeature".nr) AS anon_5
   FROM productfeatureproduct) AS anon_4,

  (SELECT producttypeproduct.product AS product,

     (SELECT "producttype".nr
      FROM producttype
      WHERE "producttype"."nr" = '9'
        AND "producttypeproduct".productType = "producttype".nr) AS anon_7
   FROM producttypeproduct) AS anon_6,

  (SELECT product.nr AS product,
          product."propertyNum1" AS value1
   FROM product) AS anon_8
WHERE anon_2.product = anon_4.product
  AND anon_2.product = anon_6.product
  AND anon_2.product = anon_8.product
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_2.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_1.s
  AND (anon_8.value1 > 114)
ORDER BY anon_1.o
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product84	"acclimating"
bsbm-inst:Product34	"amtrac puckery"
bsbm-inst:Product71	"anesthesiologist"
bsbm-inst:Product2	"anglians"
bsbm-inst:Product86	"anodizes expender elaborately"
bsbm-inst:Product75	"anoxias fruiter"
bsbm-inst:Product9	"anytime conservators flivver"
bsbm-inst:Product58	"bettas swerved deflea"
bsbm-inst:Product25	"boundaries proselyted"
bsbm-inst:Product21	"burrowers accommodations"
```

FAIL
