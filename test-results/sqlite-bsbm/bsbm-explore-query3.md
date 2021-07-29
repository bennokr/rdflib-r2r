# bsbm-explore-query3
[bsbm-explore-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ3)

## Random parameter sample
```
y = "366"^^<http://www.w3.org/2001/XMLSchema#integer>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature582>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15>
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature127>
x = "47"^^<http://www.w3.org/2001/XMLSchema#integer>
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
    ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> .
	?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature127> .
	?product bsbm:productPropertyNumeric1 ?p1 .
	FILTER ( ?p1 > "47"^^<http://www.w3.org/2001/XMLSchema#integer> ) 
	?product bsbm:productPropertyNumeric3 ?p3 .
	FILTER (?p3 < "366"^^<http://www.w3.org/2001/XMLSchema#integer> )
    OPTIONAL { 
        ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature582> .
        ?product rdfs:label ?testVar }
    FILTER (!bound(?testVar)) 
}
ORDER BY ?label
LIMIT 10


```

## Goal results
```
bsbm-inst:Product70	"lettering sardonyxes"
```

## Created SQL query
```sql
SELECT anon_1.s AS product,
       anon_1.o AS label
FROM
  (SELECT anon_2.s AS s,
          anon_2.o AS o,
          anon_3.p1 AS p1,
          anon_3.p3 AS p3
   FROM
     (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
             '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
             vendor.label AS o,
             NULL AS g
      FROM vendor
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
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                       producttype.label AS o,
                       NULL AS g
      FROM producttype
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                       product.label AS o,
                       NULL AS g
      FROM product) AS anon_2,

     (SELECT product.nr AS product,
             product."propertyNum1" AS p1,
             product."propertyNum3" AS p3
      FROM product) AS anon_3,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct,
           producttype AS producttype_ref
      WHERE "producttype_ref"."nr" = '15'
        AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_4,

     (SELECT productfeatureproduct.product AS product
      FROM productfeatureproduct,
           productfeature AS productfeature_ref
      WHERE "productfeature_ref"."nr" = '127'
        AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_5
   WHERE anon_4.product = anon_5.product
     AND anon_4.product = anon_3.product
     AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_4.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_2.s) AS anon_1,

  (SELECT anon_7.product AS product,
          anon_8."testVar" AS "testVar"
   FROM
     (SELECT productfeatureproduct.product AS product
      FROM productfeatureproduct,
           productfeature AS productfeature_ref
      WHERE "productfeature_ref"."nr" = '582'
        AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_7,

     (SELECT productfeature.nr AS product,
             productfeature.label AS "testVar"
      FROM productfeature) AS anon_8
   WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_7.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)) AS anon_6
WHERE anon_1.s = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_6.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
  AND (anon_1.p1 > 47)
  AND (anon_1.p3 < 366)
  AND anon_6."testVar" IS NOT NULL
ORDER BY anon_1.o
LIMIT 10
OFFSET 0
```

## Created SQL results
```

```

FAIL