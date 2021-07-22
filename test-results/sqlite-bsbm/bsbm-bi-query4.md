# bsbm-bi-query4
[link]([bsbm-bi-query4](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ4))

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15>
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> ;
                 bsbm:productFeature ?feature .
        ?offer bsbm:product ?product ;
               bsbm:price ?price .
      }
      Group By ?feature
    }
    { Select ?feature (avg(xsd:float(xsd:string(?price))) As ?withoutFeaturePrice)
      {
        { Select distinct ?feature { 
          ?p a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> ;
             bsbm:productFeature ?feature .
        } }
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> .
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
bsbm-inst:ProductFeature653	"2.3414939544364013"^^xsd:double
bsbm-inst:ProductFeature137	"1.8935085688431526"^^xsd:double
bsbm-inst:ProductFeature134	"1.320744567610804"^^xsd:double
bsbm-inst:ProductFeature627	"1.320744567610804"^^xsd:double
bsbm-inst:ProductFeature99	"1.320744567610804"^^xsd:double
bsbm-inst:ProductFeature641	"1.2405515472854671"^^xsd:double
bsbm-inst:ProductFeature100	"1.2122419531648487"^^xsd:double
bsbm-inst:ProductFeature112	"1.2122419531648487"^^xsd:double
bsbm-inst:ProductFeature115	"1.2122419531648487"^^xsd:double
bsbm-inst:ProductFeature117	"1.2122419531648487"^^xsd:double
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
             offer.nr AS offer
      FROM offer) AS anon_4,

     (SELECT producttypeproduct.product AS product,

        (SELECT "producttype".nr
         FROM producttype
         WHERE "producttype"."nr" = '15'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_6
      FROM producttypeproduct) AS anon_5,

     (SELECT
        (SELECT "product".nr
         FROM product
         WHERE "offer".product = "product".nr) AS product,
             offer.nr AS offer
      FROM offer) AS anon_7
   WHERE anon_5.product = anon_7.product
     AND anon_3.product = anon_7.product
     AND anon_7.offer = anon_4.offer
   GROUP BY anon_3.feature) AS anon_1,

  (SELECT anon_8.feature AS feature,
          avg(CAST(CAST(anon_9.price AS VARCHAR) AS FLOAT)) AS avg_2
   FROM
     (SELECT DISTINCT anon_10.feature AS feature
      FROM
        (SELECT productfeatureproduct.product AS p,

           (SELECT "productfeature".nr
            FROM productfeature
            WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
         FROM productfeatureproduct) AS anon_10,

        (SELECT producttypeproduct.product AS p,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '15'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_12
         FROM producttypeproduct) AS anon_11
      WHERE anon_11.p = anon_10.p) AS anon_8,

     (SELECT anon_13.offer AS offer,
             anon_13.product AS product,
             anon_14.price AS price
      FROM
        (SELECT offer.nr AS offer,

           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product
         FROM offer) AS anon_13,

        (SELECT offer.price AS price,
                offer.nr AS offer
         FROM offer) AS anon_14,

        (SELECT producttypeproduct.product AS product,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '15'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_16
         FROM producttypeproduct) AS anon_15
      WHERE anon_13.offer = anon_14.offer
        AND anon_15.product = anon_13.product) AS anon_9
   WHERE NOT (EXISTS
                (SELECT anon_17.product,
                        anon_17.feature
                 FROM
                   (SELECT productfeatureproduct.product AS product,

                      (SELECT "productfeature".nr
                       FROM productfeature
                       WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS feature
                    FROM productfeatureproduct) AS anon_17
                 WHERE anon_8.feature = anon_17.feature
                   AND anon_17.product = anon_9.product))
   GROUP BY anon_8.feature) AS anon_2
WHERE anon_1.feature = anon_2.feature
ORDER BY CAST(anon_1.avg_1 / anon_2.avg_2 AS FLOAT) DESC, anon_1.feature
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductFeature419	"1.2812520583731255"^^xsd:double
bsbm-inst:ProductFeature417	"1.2532995987875322"^^xsd:double
bsbm-inst:ProductFeature410	"1.2520972939260449"^^xsd:double
bsbm-inst:ProductFeature765	"1.2435943359688573"^^xsd:double
bsbm-inst:ProductFeature812	"1.2435943359688573"^^xsd:double
bsbm-inst:ProductFeature249	"1.232136071397448"^^xsd:double
bsbm-inst:ProductFeature269	"1.232136071397448"^^xsd:double
bsbm-inst:ProductFeature288	"1.2302046910251092"^^xsd:double
bsbm-inst:ProductFeature284	"1.2202122424187025"^^xsd:double
bsbm-inst:ProductFeature251	"1.216800142145025"^^xsd:double
```

FAIL