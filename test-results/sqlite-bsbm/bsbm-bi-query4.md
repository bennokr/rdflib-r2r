# bsbm-bi-query4
[bsbm-bi-query4](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ4)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12>
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12> ;
                 bsbm:productFeature ?feature .
        ?offer bsbm:product ?product ;
               bsbm:price ?price .
      }
      Group By ?feature
    }
    { Select ?feature (avg(xsd:float(xsd:string(?price))) As ?withoutFeaturePrice)
      {
        { Select distinct ?feature { 
          ?p a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12> ;
             bsbm:productFeature ?feature .
        } }
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12> .
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
bsbm-inst:ProductFeature41	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature453	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature48	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature487	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature53	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature56	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature66	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature67	"1.0956197170460957"^^xsd:double
bsbm-inst:ProductFeature62	"1.0916082101177007"^^xsd:double
bsbm-inst:ProductFeature466	"1.0887155863497342"^^xsd:double
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS feature,
       CAST(anon_1.avg_1 / anon_2.avg_2 AS FLOAT) AS "priceRatio"
FROM
  (SELECT anon_3.nr AS nr,
          avg(CAST(CAST(anon_4.price AS VARCHAR) AS FLOAT)) AS avg_1
   FROM
     (SELECT productfeatureproduct.product AS product,
             productfeature.nr AS nr
      FROM productfeatureproduct,
           productfeature
      WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS anon_3,

     (SELECT offer.nr AS nr,
             offer.price AS price
      FROM offer) AS anon_4,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct,
           producttype
      WHERE "nr" = '12'
        AND "producttypeproduct".productType = "producttype".nr) AS anon_5,

     (SELECT offer.nr AS nr,
             product.nr AS nr_1
      FROM offer,
           product
      WHERE "offer".product = "product".nr) AS anon_6
   WHERE anon_5.product = anon_3.product
     AND anon_5.product = anon_6.nr_1
     AND anon_6.nr = anon_4.nr
   GROUP BY anon_3.nr) AS anon_1,

  (SELECT anon_7.nr AS nr,
          avg(CAST(CAST(anon_8.price AS VARCHAR) AS FLOAT)) AS avg_2
   FROM
     (SELECT DISTINCT anon_9.nr AS nr
      FROM
        (SELECT productfeatureproduct.product AS product,
                productfeature.nr AS nr
         FROM productfeatureproduct,
              productfeature
         WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS anon_9,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype
         WHERE "nr" = '12'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_10
      WHERE anon_10.product = anon_9.product) AS anon_7,

     (SELECT anon_11.product AS product,
             anon_12.nr AS nr,
             anon_13.price AS price
      FROM
        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype
         WHERE "nr" = '12'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_11,

        (SELECT offer.nr AS nr,
                product.nr AS nr_2
         FROM offer,
              product
         WHERE "offer".product = "product".nr) AS anon_12,

        (SELECT offer.nr AS nr,
                offer.price AS price
         FROM offer) AS anon_13
      WHERE anon_11.product = anon_12.nr_2
        AND anon_12.nr = anon_13.nr) AS anon_8
   WHERE NOT (EXISTS
                (SELECT anon_14.product,
                        anon_14.nr
                 FROM
                   (SELECT productfeatureproduct.product AS product,
                           productfeature.nr AS nr
                    FROM productfeatureproduct,
                         productfeature
                    WHERE "productfeatureproduct".productFeature = "productfeature".nr) AS anon_14
                 WHERE anon_7.nr = anon_14.nr
                   AND anon_8.product = anon_14.product))
   GROUP BY anon_7.nr) AS anon_2
WHERE anon_1.nr = anon_2.nr
ORDER BY CAST(anon_1.avg_1 / anon_2.avg_2 AS FLOAT) DESC, anon_1.nr
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductFeature41	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature48	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature53	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature56	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature66	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature67	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature453	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature487	"1.0956197170460955"^^xsd:double
bsbm-inst:ProductFeature62	"1.0916082101177005"^^xsd:double
bsbm-inst:ProductFeature466	"1.0887155863497342"^^xsd:double
```

FAIL