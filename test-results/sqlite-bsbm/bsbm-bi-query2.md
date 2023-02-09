# bsbm-bi-query2
[bsbm-bi-query2](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ2)

## Random parameter sample
```
Product = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product33>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> 

  SELECT ?otherProduct ?sameFeatures
  {
    ?otherProduct a bsbm:Product .
    FILTER(?otherProduct != <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product33>)
    {
      SELECT ?otherProduct (count(?otherFeature) As ?sameFeatures)
      {
        <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product33> bsbm:productFeature ?feature .
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
bsbm-inst:Product22	"7"^^xsd:integer
bsbm-inst:Product25	"5"^^xsd:integer
bsbm-inst:Product94	"7"^^xsd:integer
bsbm-inst:Product14	"10"^^xsd:integer
bsbm-inst:Product35	"6"^^xsd:integer
bsbm-inst:Product77	"7"^^xsd:integer
bsbm-inst:Product27	"5"^^xsd:integer
bsbm-inst:Product8	"14"^^xsd:integer
bsbm-inst:Product89	"6"^^xsd:integer
bsbm-inst:Product7	"7"^^xsd:integer
```

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS "otherProduct",
       anon_2.count_1 AS "sameFeatures"
FROM
  (SELECT anon_3."otherProduct" AS "otherProduct"
   FROM
     (SELECT product.nr AS "otherProduct"
      FROM product) AS anon_3) AS anon_1,

  (SELECT anon_4.product AS product,
          count(anon_4."""productfeature_ref"".nr_1") AS count_1
   FROM
     (SELECT anon_5."""productfeature_ref"".nr_2" AS """productfeature_ref"".nr_2",
             anon_6.product AS product,
             anon_6."""productfeature_ref"".nr_1" AS """productfeature_ref"".nr_1"
      FROM
        (SELECT "productfeature_ref".nr AS """productfeature_ref"".nr_2"
         FROM productfeature AS productfeature_ref,
              productfeatureproduct
         WHERE "productfeatureproduct"."product" = '33'
           AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_5,

        (SELECT productfeatureproduct.product AS product,
                "productfeature_ref".nr AS """productfeature_ref"".nr_1"
         FROM productfeatureproduct,
              productfeature AS productfeature_ref
         WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_6
      WHERE anon_5."""productfeature_ref"".nr_2" = anon_6."""productfeature_ref"".nr_1") AS anon_4
   GROUP BY anon_4.product) AS anon_2
WHERE anon_1."otherProduct" = anon_2.product
  AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product33>'
ORDER BY anon_2.count_1 DESC,
         CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product22	"7"^^xsd:integer
bsbm-inst:Product25	"5"^^xsd:integer
bsbm-inst:Product94	"7"^^xsd:integer
bsbm-inst:Product14	"10"^^xsd:integer
bsbm-inst:Product35	"6"^^xsd:integer
bsbm-inst:Product77	"7"^^xsd:integer
bsbm-inst:Product27	"5"^^xsd:integer
bsbm-inst:Product8	"14"^^xsd:integer
bsbm-inst:Product89	"6"^^xsd:integer
bsbm-inst:Product7	"7"^^xsd:integer
```

SUCCES