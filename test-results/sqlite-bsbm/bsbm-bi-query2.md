# bsbm-bi-query2
[link]([bsbm-bi-query2](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ2))

## Random parameter sample
```
Product = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product50>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> 

  SELECT ?otherProduct ?sameFeatures
  {
    ?otherProduct a bsbm:Product .
    FILTER(?otherProduct != <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product50>)
    {
      SELECT ?otherProduct (count(?otherFeature) As ?sameFeatures)
      {
        <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product50> bsbm:productFeature ?feature .
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
bsbm-inst:Product26	"6"^^xsd:integer
bsbm-inst:Product52	"6"^^xsd:integer
bsbm-inst:Product72	"6"^^xsd:integer
bsbm-inst:Product30	"4"^^xsd:integer
bsbm-inst:Product34	"4"^^xsd:integer
bsbm-inst:Product40	"4"^^xsd:integer
bsbm-inst:Product98	"4"^^xsd:integer
bsbm-inst:Product11	"3"^^xsd:integer
bsbm-inst:Product29	"3"^^xsd:integer
bsbm-inst:Product46	"3"^^xsd:integer
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

  (SELECT anon_4."otherProduct" AS "otherProduct",
          count(anon_4."otherFeature") AS count_1
   FROM
     (SELECT productfeatureproduct.product AS "otherProduct",

        (SELECT "productfeature".nr
         FROM productfeature
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS "otherFeature"
      FROM productfeatureproduct) AS anon_4,

     (SELECT
        (SELECT "productfeature".nr
         FROM productfeature
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
      FROM productfeatureproduct
      WHERE "productfeatureproduct"."product" = '50') AS anon_5
   WHERE anon_5.feature = anon_4."otherFeature"
   GROUP BY anon_4."otherProduct") AS anon_2
WHERE anon_1."otherProduct" = anon_2."otherProduct"
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product50>'
ORDER BY anon_2.count_1 DESC,
         anon_1."otherProduct"
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product26	"6"^^xsd:integer
bsbm-inst:Product52	"6"^^xsd:integer
bsbm-inst:Product72	"6"^^xsd:integer
bsbm-inst:Product30	"4"^^xsd:integer
bsbm-inst:Product34	"4"^^xsd:integer
bsbm-inst:Product40	"4"^^xsd:integer
bsbm-inst:Product98	"4"^^xsd:integer
bsbm-inst:Product11	"3"^^xsd:integer
bsbm-inst:Product29	"3"^^xsd:integer
bsbm-inst:Product46	"3"^^xsd:integer
```

SUCCES