# bsbm-bi-query4
[bsbm-bi-query4](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ4)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6>
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6> ;
                 bsbm:productFeature ?feature .
        ?offer bsbm:product ?product ;
               bsbm:price ?price .
      }
      Group By ?feature
    }
    { Select ?feature (avg(xsd:float(xsd:string(?price))) As ?withoutFeaturePrice)
      {
        { Select distinct ?feature { 
          ?p a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6> ;
             bsbm:productFeature ?feature .
        } }
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6> .
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
bsbm-inst:ProductFeature24	"1.259561207826258"^^xsd:double
bsbm-inst:ProductFeature188	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature204	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature192	"1.3154491134790216"^^xsd:double
bsbm-inst:ProductFeature32	"1.3503245989096258"^^xsd:double
bsbm-inst:ProductFeature29	"1.4046384162624663"^^xsd:double
bsbm-inst:ProductFeature21	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature211	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature194	"1.4027255189393937"^^xsd:double
bsbm-inst:ProductFeature202	"1.2590702833251517"^^xsd:double
```

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""productfeature_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS feature,
       CAST(anon_1.avg_1 / anon_2.avg_2 AS REAL) AS "priceRatio"
FROM
  (SELECT anon_3."""productfeature_ref"".nr_1" AS """productfeature_ref"".nr_1",
          avg(CAST(CAST(anon_3.price AS VARCHAR) AS FLOAT)) AS avg_1
   FROM
     (SELECT anon_4.nr AS nr,
             anon_4."""product_ref"".nr_1" AS """product_ref"".nr_1",
             anon_5."""productfeature_ref"".nr_1" AS """productfeature_ref"".nr_1",
             anon_6.price AS price
      FROM
        (SELECT offer.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_1"
         FROM offer,
              product AS product_ref
         WHERE "offer".product = "product_ref".nr) AS anon_4,

        (SELECT productfeatureproduct.product AS product,
                "productfeature_ref".nr AS """productfeature_ref"".nr_1"
         FROM productfeatureproduct,
              productfeature AS productfeature_ref
         WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_5,

        (SELECT offer.price AS price,
                offer.nr AS offer
         FROM offer) AS anon_6,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype AS producttype_ref
         WHERE "producttype_ref"."nr" = '6'
           AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_7
      WHERE anon_4.nr = anon_6.offer
        AND anon_7.product = anon_4."""product_ref"".nr_1"
        AND anon_5.product = anon_4."""product_ref"".nr_1") AS anon_3
   GROUP BY anon_3."""productfeature_ref"".nr_1") AS anon_1,

  (SELECT anon_8."""productfeature_ref"".nr_2" AS """productfeature_ref"".nr_2",
          avg(CAST(CAST(anon_8.price AS VARCHAR) AS FLOAT)) AS avg_2
   FROM
     (SELECT anon_9."""productfeature_ref"".nr_2" AS """productfeature_ref"".nr_2",
             anon_10.nr AS nr,
             anon_10."""product_ref"".nr_2" AS """product_ref"".nr_2",
             anon_10.price AS price
      FROM
        (SELECT DISTINCT anon_11."""productfeature_ref"".nr_2" AS """productfeature_ref"".nr_2"
         FROM
           (SELECT productfeatureproduct.product AS product,
                   "productfeature_ref".nr AS """productfeature_ref"".nr_2"
            FROM productfeatureproduct,
                 productfeature AS productfeature_ref
            WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_11,

           (SELECT producttypeproduct.product AS product
            FROM producttypeproduct,
                 producttype AS producttype_ref
            WHERE "producttype_ref"."nr" = '6'
              AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_12
         WHERE anon_11.product = anon_12.product) AS anon_9,

        (SELECT anon_13.nr AS nr,
                anon_13."""product_ref"".nr_2" AS """product_ref"".nr_2",
                anon_14.price AS price
         FROM
           (SELECT offer.nr AS nr,
                   "product_ref".nr AS """product_ref"".nr_2"
            FROM offer,
                 product AS product_ref
            WHERE "offer".product = "product_ref".nr) AS anon_13,

           (SELECT offer.price AS price,
                   offer.nr AS offer
            FROM offer) AS anon_14,

           (SELECT producttypeproduct.product AS product
            FROM producttypeproduct,
                 producttype AS producttype_ref
            WHERE "producttype_ref"."nr" = '6'
              AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_15
         WHERE anon_13.nr = anon_14.offer
           AND anon_15.product = anon_13."""product_ref"".nr_2") AS anon_10
      WHERE NOT (EXISTS
                   (SELECT anon_16.product,
                           anon_16."""productfeature_ref"".nr_3"
                    FROM
                      (SELECT productfeatureproduct.product AS product,
                              "productfeature_ref".nr AS """productfeature_ref"".nr_3"
                       FROM productfeatureproduct,
                            productfeature AS productfeature_ref
                       WHERE "productfeatureproduct".productFeature = "productfeature_ref".nr) AS anon_16
                    WHERE anon_9."""productfeature_ref"".nr_2" = anon_16."""productfeature_ref"".nr_3"
                      AND anon_16.product = anon_10."""product_ref"".nr_2"))) AS anon_8
   GROUP BY anon_8."""productfeature_ref"".nr_2") AS anon_2
WHERE anon_1."""productfeature_ref"".nr_1" = anon_2."""productfeature_ref"".nr_2"
ORDER BY CAST(anon_1.avg_1 / anon_2.avg_2 AS REAL) DESC, CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""productfeature_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductFeature29	"1.404638416262466"^^xsd:double
bsbm-inst:ProductFeature188	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature32	"1.3503245989096262"^^xsd:double
bsbm-inst:ProductFeature202	"1.2590702833251513"^^xsd:double
bsbm-inst:ProductFeature204	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature192	"1.3154491134790216"^^xsd:double
bsbm-inst:ProductFeature24	"1.2595612078262581"^^xsd:double
bsbm-inst:ProductFeature194	"1.4027255189393946"^^xsd:double
bsbm-inst:ProductFeature21	"1.2556040041761343"^^xsd:double
bsbm-inst:ProductFeature211	"1.2556040041761343"^^xsd:double
```

FAIL