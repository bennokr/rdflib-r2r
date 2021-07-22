# bsbm-bi-query8
[bsbm-bi-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ8)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType13>
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
        { ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType13> .
          ?offer bsbm:product ?product .
          ?offer bsbm:vendor ?vendor .
          ?offer bsbm:price ?price .
          { Select ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
            {
              ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType13> .
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType13> .
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
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr_1 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS vendor,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) AS "cheapExpensiveRatio"
FROM
  (SELECT anon_3.nr_1 AS nr_1,
          count(anon_3.nr) AS count_1
   FROM
     (SELECT anon_4.nr AS nr,
             anon_4.nr_1 AS nr_1,
             anon_5.product AS product,
             anon_6.price AS price
      FROM
        (SELECT offer.nr AS nr,
                vendor.nr AS nr_1
         FROM offer,
              vendor
         WHERE "offer".vendor = "vendor".nr) AS anon_4,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype
         WHERE "nr" = '13'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_5,

        (SELECT offer.nr AS nr,
                offer.price AS price
         FROM offer) AS anon_6,

        (SELECT offer.nr AS nr,
                product.nr AS nr_2
         FROM offer,
              product
         WHERE "offer".product = "product".nr) AS anon_7
      WHERE anon_4.nr = anon_7.nr
        AND anon_4.nr = anon_6.nr
        AND anon_5.product = anon_7.nr_2) AS anon_3,

     (SELECT anon_9.product AS product,
             avg(CAST(CAST(anon_10.price AS VARCHAR) AS FLOAT)) AS avg_1
      FROM
        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype
         WHERE "nr" = '13'
           AND "producttypeproduct".productType = "producttype".nr) AS anon_9,

        (SELECT offer.nr AS nr,
                offer.price AS price
         FROM offer) AS anon_10,

        (SELECT offer.nr AS nr,
                vendor.nr AS nr_3
         FROM offer,
              vendor
         WHERE "offer".vendor = "vendor".nr) AS anon_11,

        (SELECT offer.nr AS nr,
                product.nr AS nr_4
         FROM offer,
              product
         WHERE "offer".product = "product".nr) AS anon_12
      WHERE anon_11.nr = anon_12.nr
        AND anon_11.nr = anon_10.nr
        AND anon_9.product = anon_12.nr_4
      GROUP BY anon_9.product) AS anon_8
   WHERE anon_3.product = anon_8.product
     AND (CAST(CAST(anon_3.price AS VARCHAR) AS FLOAT) < anon_8.avg_1)
   GROUP BY anon_3.nr_1) AS anon_1,

  (SELECT anon_13.nr_5 AS nr_5,
          count(anon_13.nr) AS count_2
   FROM
     (SELECT offer.nr AS nr,
             vendor.nr AS nr_5
      FROM offer,
           vendor
      WHERE "offer".vendor = "vendor".nr) AS anon_13,

     (SELECT offer.nr AS nr,
             product.nr AS nr_6
      FROM offer,
           product
      WHERE "offer".product = "product".nr) AS anon_14,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct,
           producttype
      WHERE "nr" = '13'
        AND "producttypeproduct".productType = "producttype".nr) AS anon_15
   WHERE anon_13.nr = anon_14.nr
     AND anon_15.product = anon_14.nr_6
   GROUP BY anon_13.nr_5) AS anon_2
WHERE anon_1.nr_1 = anon_2.nr_5
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) DESC, anon_1.nr_1
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Vendor1	"0.5290697674418605"^^xsd:double
```

FAIL