# bsbm-bi-query2
[bsbm-bi-query2](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ2)

## Random parameter sample
```
Product = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product84>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> 

  SELECT ?otherProduct ?sameFeatures
  {
    ?otherProduct a bsbm:Product .
    FILTER(?otherProduct != <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product84>)
    {
      SELECT ?otherProduct (count(?otherFeature) As ?sameFeatures)
      {
        <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product84> bsbm:productFeature ?feature .
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
bsbm-inst:Product19	"3"^^xsd:integer
bsbm-inst:Product39	"3"^^xsd:integer
bsbm-inst:Product11	"4"^^xsd:integer
bsbm-inst:Product95	"5"^^xsd:integer
bsbm-inst:Product52	"4"^^xsd:integer
bsbm-inst:Product18	"4"^^xsd:integer
bsbm-inst:Product83	"5"^^xsd:integer
bsbm-inst:Product55	"4"^^xsd:integer
bsbm-inst:Product13	"3"^^xsd:integer
bsbm-inst:Product50	"3"^^xsd:integer
```

## Created SQL query
```sql
SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS "otherProduct",
       anon_2.count_1 AS "sameFeatures"
FROM
  (SELECT anon_3.nr AS nr
   FROM
     (SELECT product.nr AS nr
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
         WHERE "productfeatureproduct"."product" = '84'
           AND "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_5,

        (SELECT productfeatureproduct.product AS product,
                "productfeature_ref".nr AS """productfeature_ref"".nr_1"
         FROM productfeatureproduct,
              productfeature AS productfeature_ref
         WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_6
      WHERE anon_5."""productfeature_ref"".nr_2" = anon_6."""productfeature_ref"".nr_1") AS anon_4
   GROUP BY anon_4.product) AS anon_2
WHERE anon_1.nr = anon_2.product
  AND '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product84>'
ORDER BY anon_2.count_1 DESC,
         '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
LIMIT 10
```

## Created SQL results
```
bsbm-inst:Product19	"3"^^xsd:integer
bsbm-inst:Product39	"3"^^xsd:integer
bsbm-inst:Product11	"4"^^xsd:integer
bsbm-inst:Product95	"5"^^xsd:integer
bsbm-inst:Product52	"4"^^xsd:integer
bsbm-inst:Product18	"4"^^xsd:integer
bsbm-inst:Product83	"5"^^xsd:integer
bsbm-inst:Product55	"4"^^xsd:integer
bsbm-inst:Product13	"3"^^xsd:integer
bsbm-inst:Product50	"3"^^xsd:integer
```

SUCCES