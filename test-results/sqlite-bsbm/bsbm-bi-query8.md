# bsbm-bi-query8
[link]([bsbm-bi-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ8))

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?vendor (xsd:float(?belowAvg)/?offerCount As ?cheapExpensiveRatio)
  {
    { Select ?vendor (count(?offer) As ?belowAvg)
      {
        { ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> .
          ?offer bsbm:product ?product .
          ?offer bsbm:vendor ?vendor .
          ?offer bsbm:price ?price .
          { Select ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
            {
              ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> .
              ?offer bsbm:product ?product .
              ?offer bsbm:vendor ?vendor .
              ?offer bsbm:price ?price .
            }
            Group By ?product
          }
        } .
        FILTER (xsd:float(xsd:string(?price)) < ?avgPrice)
      }
      Group By ?vendor
    }
    { Select ?vendor (count(?offer) As ?offerCount)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> .
        ?offer bsbm:product ?product .
        ?offer bsbm:vendor ?vendor .
      }
      Group By ?vendor
    }
  }
  Order by desc(xsd:float(?belowAvg)/?offerCount) ?vendor
  limit 10

```

## Goal results
```
bsbm-inst:Vendor1	
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(anon_1.vendor AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS vendor,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) AS "cheapExpensiveRatio"
FROM
  (SELECT anon_3.vendor AS vendor,
          count(anon_3.offer) AS count_1
   FROM
     (SELECT anon_4.product AS product,
             anon_4.offer AS offer,
             anon_5.price AS price,
             anon_6.vendor AS vendor
      FROM
        (SELECT
           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product,
                offer.nr AS offer
         FROM offer) AS anon_4,

        (SELECT offer.price AS price,
                offer.nr AS offer
         FROM offer) AS anon_5,

        (SELECT
           (SELECT "vendor".nr
            FROM vendor
            WHERE "offer".vendor = "vendor".nr) AS vendor,
                offer.nr AS offer
         FROM offer) AS anon_6,

        (SELECT producttypeproduct.product AS product,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '9'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_8
         FROM producttypeproduct) AS anon_7
      WHERE anon_7.product = anon_4.product
        AND anon_4.offer = anon_5.offer
        AND anon_4.offer = anon_6.offer) AS anon_3,

     (SELECT anon_10.product AS product,
             avg(CAST(CAST(anon_11.price AS VARCHAR) AS FLOAT)) AS avg_1
      FROM
        (SELECT
           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product,
                offer.nr AS offer
         FROM offer) AS anon_10,

        (SELECT offer.price AS price,
                offer.nr AS offer
         FROM offer) AS anon_11,

        (SELECT producttypeproduct.product AS product,

           (SELECT "producttype".nr
            FROM producttype
            WHERE "producttype"."nr" = '9'
              AND "producttypeproduct".productType = "producttype".nr) AS anon_13
         FROM producttypeproduct) AS anon_12,

        (SELECT
           (SELECT "vendor".nr
            FROM vendor
            WHERE "offer".vendor = "vendor".nr) AS vendor,
                offer.nr AS offer
         FROM offer) AS anon_14
      WHERE anon_12.product = anon_10.product
        AND anon_10.offer = anon_11.offer
        AND anon_10.offer = anon_14.offer
      GROUP BY anon_10.product) AS anon_9
   WHERE anon_3.product = anon_9.product
     AND (CAST(CAST(anon_3.price AS VARCHAR) AS FLOAT) < anon_9.avg_1)
   GROUP BY anon_3.vendor) AS anon_1,

  (SELECT anon_15.vendor AS vendor,
          count(anon_16.offer) AS count_2
   FROM
     (SELECT
        (SELECT "vendor".nr
         FROM vendor
         WHERE "offer".vendor = "vendor".nr) AS vendor,
             offer.nr AS offer
      FROM offer) AS anon_15,

     (SELECT
        (SELECT "product".nr
         FROM product
         WHERE "offer".product = "product".nr) AS product,
             offer.nr AS offer
      FROM offer) AS anon_16,

     (SELECT producttypeproduct.product AS product,

        (SELECT "producttype".nr
         FROM producttype
         WHERE "producttype"."nr" = '9'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_18
      FROM producttypeproduct) AS anon_17
   WHERE anon_17.product = anon_16.product
     AND anon_16.offer = anon_15.offer
   GROUP BY anon_15.vendor) AS anon_2
WHERE anon_1.vendor = anon_2.vendor
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) DESC, anon_1.vendor
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Vendor1	"0.4885"^^xsd:double
```

FAIL