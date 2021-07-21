
# bsbm-bi-query4

## Random parameter sample
```
{'ProductType': '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7>'}
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?feature (?withFeaturePrice/?withoutFeaturePrice As ?priceRatio)
  {
    { Select ?feature (avg(xsd:float(xsd:string(?price))) As ?withFeaturePrice)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7> ;
                 bsbm:productFeature ?feature .
        ?offer bsbm:product ?product ;
               bsbm:price ?price .
      }
      Group By ?feature
    }
    { Select ?feature (avg(xsd:float(xsd:string(?price))) As ?withoutFeaturePrice)
      {
        { Select distinct ?feature { 
          ?p a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7> ;
             bsbm:productFeature ?feature .
        } }
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType7> .
        ?offer bsbm:product ?product ;
               bsbm:price ?price .
        FILTER NOT EXISTS { ?product bsbm:productFeature ?feature }
      }
      Group By ?feature
    }
  }
  Order By desc(?withFeaturePrice/?withoutFeaturePrice) ?feature
  Limit 10

```

## Goal results
```
bsbm-inst:ProductFeature31	"1.1675522586646772"^^xsd:double
bsbm-inst:ProductFeature249	"1.1387245474585204"^^xsd:double
bsbm-inst:ProductFeature269	"1.1387245474585204"^^xsd:double
bsbm-inst:ProductFeature284	"1.1331527317401733"^^xsd:double
bsbm-inst:ProductFeature275	"1.1208144510986275"^^xsd:double
bsbm-inst:ProductFeature288	"1.1393941266027228"^^xsd:double
bsbm-inst:ProductFeature246	"1.1257920426094123"^^xsd:double
bsbm-inst:ProductFeature35	"1.1331527317401733"^^xsd:double
bsbm-inst:ProductFeature247	"1.1233115131667597"^^xsd:double
bsbm-inst:ProductFeature251	"1.1427364965272493"^^xsd:double
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(anon_1.feature AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS feature,
       CAST(anon_1.avg_1 / anon_2.avg_2 AS FLOAT) AS "priceRatio"
FROM
  (SELECT anon_3.feature AS feature,
          avg(CAST(CAST(anon_4.price AS VARCHAR) AS FLOAT)) AS avg_1
   FROM
     (SELECT productfeatureproduct.product AS product,

        (SELECT "productfeature".nr
         FROM productfeature
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
      FROM productfeatureproduct) AS anon_3,

     (SELECT offer.price AS price,
             offer.nr AS offer,

        (SELECT "product".nr
         FROM product
         WHERE "offer".product = "product".nr) AS product
      FROM offer) AS anon_4,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct) AS anon_5
   WHERE anon_5.product = anon_4.product
     AND anon_3.product = anon_4.product
   GROUP BY anon_3.feature) AS anon_1,

  (SELECT anon_6.feature AS feature,
          avg(CAST(CAST(anon_7.price AS VARCHAR) AS FLOAT)) AS avg_2
   FROM
     (SELECT DISTINCT anon_8.feature AS feature
      FROM
        (SELECT productfeatureproduct.product AS p,

           (SELECT "productfeature".nr
            FROM productfeature
            WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
         FROM productfeatureproduct) AS anon_8,

        (SELECT producttypeproduct.product AS p
         FROM producttypeproduct) AS anon_9
      WHERE anon_9.p = anon_8.p) AS anon_6,

     (SELECT anon_10.product AS product,
             anon_10.offer AS offer,
             anon_10.price AS price
      FROM
        (SELECT
           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product,
                offer.nr AS offer,
                offer.price AS price
         FROM offer) AS anon_10,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct) AS anon_11
      WHERE anon_11.product = anon_10.product) AS anon_7
   WHERE NOT (EXISTS
                (SELECT anon_12.product,
                        anon_12.feature
                 FROM
                   (SELECT productfeatureproduct.product AS product,

                      (SELECT "productfeature".nr
                       FROM productfeature
                       WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
                    FROM productfeatureproduct) AS anon_12
                 WHERE anon_6.feature = anon_12.feature
                   AND anon_12.product = anon_7.product))
   GROUP BY anon_6.feature) AS anon_2
WHERE anon_1.feature = anon_2.feature
ORDER BY CAST(anon_1.avg_1 / anon_2.avg_2 AS FLOAT) DESC, anon_1.feature
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductFeature251	"1.216800142145025"^^xsd:double
bsbm-inst:ProductFeature288	"1.2302046910251092"^^xsd:double
bsbm-inst:ProductFeature249	"1.232136071397448"^^xsd:double
bsbm-inst:ProductFeature269	"1.232136071397448"^^xsd:double
bsbm-inst:ProductFeature419	"1.2812520583731255"^^xsd:double
bsbm-inst:ProductFeature284	"1.2202122424187025"^^xsd:double
bsbm-inst:ProductFeature812	"1.2435943359688573"^^xsd:double
bsbm-inst:ProductFeature410	"1.2520972939260449"^^xsd:double
bsbm-inst:ProductFeature765	"1.2435943359688573"^^xsd:double
bsbm-inst:ProductFeature417	"1.2532995987875322"^^xsd:double
```
