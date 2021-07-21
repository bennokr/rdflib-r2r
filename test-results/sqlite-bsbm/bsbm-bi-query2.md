
# bsbm-bi-query2

## Random parameter sample
```
{'Product': '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product95>'}
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/> 

  SELECT ?otherProduct ?sameFeatures
  {
    ?otherProduct a bsbm:Product .
    FILTER(?otherProduct != <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product95>)
    {
      SELECT ?otherProduct (count(?otherFeature) As ?sameFeatures)
      {
        <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product95> bsbm:productFeature ?feature .
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
bsbm-inst:Product11	"6"^^xsd:integer
bsbm-inst:Product19	"6"^^xsd:integer
bsbm-inst:Product100	"5"^^xsd:integer
bsbm-inst:Product29	"5"^^xsd:integer
bsbm-inst:Product55	"6"^^xsd:integer
bsbm-inst:Product26	"4"^^xsd:integer
bsbm-inst:Product18	"5"^^xsd:integer
bsbm-inst:Product61	"5"^^xsd:integer
bsbm-inst:Product84	"5"^^xsd:integer
bsbm-inst:Product20	"5"^^xsd:integer
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
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature,

        (SELECT "productfeature".nr
         FROM productfeature
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS "otherFeature"
      FROM productfeatureproduct) AS anon_4
   WHERE anon_4.feature = anon_4."otherFeature"
   GROUP BY anon_4."otherProduct") AS anon_2
WHERE anon_1."otherProduct" = anon_2."otherProduct"
  AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."otherProduct" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' != '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product95>'
ORDER BY anon_2.count_1 DESC,
         anon_1."otherProduct"
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product25	"34"^^xsd:integer
bsbm-inst:Product27	"34"^^xsd:integer
bsbm-inst:Product4	"33"^^xsd:integer
bsbm-inst:Product66	"33"^^xsd:integer
bsbm-inst:Product2	"34"^^xsd:integer
bsbm-inst:Product6	"38"^^xsd:integer
bsbm-inst:Product35	"38"^^xsd:integer
bsbm-inst:Product7	"32"^^xsd:integer
bsbm-inst:Product77	"41"^^xsd:integer
bsbm-inst:Product70	"38"^^xsd:integer
```
