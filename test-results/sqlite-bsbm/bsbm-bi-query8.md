
# bsbm-bi-query8

## Random parameter sample
```
{'ProductType': '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType21>'}
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
        { ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType21> .
          ?offer bsbm:product ?product .
          ?offer bsbm:vendor ?vendor .
          ?offer bsbm:price ?price .
          { Select ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
            {
              ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType21> .
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType21> .
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
             anon_5.offer AS offer,
             anon_5.price AS price,
             anon_5.vendor AS vendor
      FROM
        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct) AS anon_4,

        (SELECT offer.nr AS offer,
                offer.price AS price,

           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product,

           (SELECT "vendor".nr
            FROM vendor
            WHERE "offer".vendor = "vendor".nr) AS vendor
         FROM offer) AS anon_5
      WHERE anon_4.product = anon_5.product) AS anon_3,

     (SELECT anon_7.product AS product,
             avg(CAST(CAST(anon_8.price AS VARCHAR) AS FLOAT)) AS avg_1
      FROM
        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct) AS anon_7,

        (SELECT offer.nr AS offer,

           (SELECT "product".nr
            FROM product
            WHERE "offer".product = "product".nr) AS product,

           (SELECT "vendor".nr
            FROM vendor
            WHERE "offer".vendor = "vendor".nr) AS vendor,
                offer.price AS price
         FROM offer) AS anon_8
      WHERE anon_7.product = anon_8.product
      GROUP BY anon_7.product) AS anon_6
   WHERE anon_3.product = anon_6.product
     AND (CAST(CAST(anon_3.price AS VARCHAR) AS FLOAT) < anon_6.avg_1)
   GROUP BY anon_3.vendor) AS anon_1,

  (SELECT anon_9.vendor AS vendor,
          count(anon_9.offer) AS count_2
   FROM
     (SELECT
        (SELECT "product".nr
         FROM product
         WHERE "offer".product = "product".nr) AS product,

        (SELECT "vendor".nr
         FROM vendor
         WHERE "offer".vendor = "vendor".nr) AS vendor,
             offer.nr AS offer
      FROM offer) AS anon_9,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct) AS anon_10
   WHERE anon_10.product = anon_9.product
   GROUP BY anon_9.vendor) AS anon_2
WHERE anon_1.vendor = anon_2.vendor
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) DESC, anon_1.vendor
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Vendor1	"0.4885"^^xsd:double
```
