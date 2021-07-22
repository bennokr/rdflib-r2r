# bsbm-bi-query2
[bsbm-bi-query2](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ2)

## Random parameter sample
```
Product = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product78>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> 

  SELECT ?otherProduct ?sameFeatures
  {
    ?otherProduct a bsbm:Product .
    FILTER(?otherProduct != <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product78>)
    {
      SELECT ?otherProduct (count(?otherFeature) As ?sameFeatures)
      {
        <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product78> bsbm:productFeature ?feature .
        ?otherProduct bsbm:productFeature ?otherFeature .
        FILTER(?feature=?otherFeature)
      }
      Group By ?otherProduct
    }
  }
  Order By desc(?sameFeatures) ?otherProduct
  Limit 10

```

## Goal results
```
bsbm-inst:Product61	"8"^^xsd:integer
bsbm-inst:Product64	"7"^^xsd:integer
bsbm-inst:Product68	"7"^^xsd:integer
bsbm-inst:Product20	"6"^^xsd:integer
bsbm-inst:Product51	"6"^^xsd:integer
bsbm-inst:Product80	"6"^^xsd:integer
bsbm-inst:Product39	"5"^^xsd:integer
bsbm-inst:Product16	"4"^^xsd:integer
bsbm-inst:Product18	"4"^^xsd:integer
bsbm-inst:Product30	"4"^^xsd:integer
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS "otherProduct",
       anon_2.count_1 AS "sameFeatures"
FROM
  (SELECT anon_3."otherProduct" AS "otherProduct"
   FROM
     (SELECT product.nr AS "otherProduct"
      FROM product) AS anon_3) AS anon_1,

  (SELECT anon_4.product AS product,
          count(anon_4.nr) AS count_1
   FROM
     (SELECT productfeatureproduct.product AS product,
             productfeature.nr AS nr
      FROM productfeatureproduct,
           productfeature
      WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS anon_4,

     (SELECT productfeature.nr AS nr
      FROM productfeature,
           productfeatureproduct
      WHERE "product" = '78'
        AND "productfeatureproduct".productFeature = "productfeature".nr) AS anon_5
   WHERE anon_5.nr = anon_4.nr
   GROUP BY anon_4.product) AS anon_2
WHERE anon_1."otherProduct" = anon_2.product
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product78>'
ORDER BY anon_2.count_1 DESC,
         anon_1."otherProduct"
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product61	"8"^^xsd:integer
bsbm-inst:Product64	"7"^^xsd:integer
bsbm-inst:Product68	"7"^^xsd:integer
bsbm-inst:Product20	"6"^^xsd:integer
bsbm-inst:Product51	"6"^^xsd:integer
bsbm-inst:Product80	"6"^^xsd:integer
bsbm-inst:Product39	"5"^^xsd:integer
bsbm-inst:Product16	"4"^^xsd:integer
bsbm-inst:Product18	"4"^^xsd:integer
bsbm-inst:Product30	"4"^^xsd:integer
```

SUCCES