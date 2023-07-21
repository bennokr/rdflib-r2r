# bsbm-bi-query8
[bsbm-bi-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ8)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType14>
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
        { ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType14> .
          ?offer bsbm:product ?product .
          ?offer bsbm:vendor ?vendor .
          ?offer bsbm:price ?price .
          { Select ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
            {
              ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType14> .
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
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType14> .
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
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS vendor,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) AS "cheapExpensiveRatio"
FROM
  (SELECT anon_3."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
          count(anon_3.nr) AS count_1
   FROM
     (SELECT anon_4.nr AS nr,
             anon_4."""product_ref"".nr_1" AS """product_ref"".nr_1",
             anon_4."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
             anon_4.price AS price,
             anon_5.avg_1 AS avg_1
      FROM
        (SELECT anon_6.nr AS nr,
                anon_6."""product_ref"".nr_1" AS """product_ref"".nr_1",
                anon_7."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
                anon_8.price AS price
         FROM
           (SELECT offer.nr AS nr,
                   "product_ref".nr AS """product_ref"".nr_1"
            FROM offer,
                 product AS product_ref
            WHERE "offer".product = "product_ref".nr) AS anon_6,

           (SELECT offer.nr AS nr,
                   "vendor_ref".nr AS """vendor_ref"".nr_1"
            FROM offer,
                 vendor AS vendor_ref
            WHERE "offer".vendor = "vendor_ref".nr) AS anon_7,

           (SELECT offer.nr AS nr,
                   offer.price AS price
            FROM offer) AS anon_8,

           (SELECT producttypeproduct.product AS product
            FROM producttypeproduct,
                 producttype AS producttype_ref
            WHERE "producttype_ref"."nr" = '14'
              AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_9
         WHERE anon_6.nr = anon_7.nr
           AND anon_6.nr = anon_8.nr
           AND anon_9.product = anon_6."""product_ref"".nr_1") AS anon_4,

        (SELECT anon_10."""product_ref"".nr_2" AS """product_ref"".nr_2",
                avg(CAST(CAST(anon_10.price AS VARCHAR) AS FLOAT)) AS avg_1
         FROM
           (SELECT anon_11.nr AS nr,
                   anon_11."""product_ref"".nr_2" AS """product_ref"".nr_2",
                   anon_12."""vendor_ref"".nr_2" AS """vendor_ref"".nr_2",
                   anon_13.price AS price
            FROM
              (SELECT offer.nr AS nr,
                      "product_ref".nr AS """product_ref"".nr_2"
               FROM offer,
                    product AS product_ref
               WHERE "offer".product = "product_ref".nr) AS anon_11,

              (SELECT offer.nr AS nr,
                      "vendor_ref".nr AS """vendor_ref"".nr_2"
               FROM offer,
                    vendor AS vendor_ref
               WHERE "offer".vendor = "vendor_ref".nr) AS anon_12,

              (SELECT offer.price AS price,
                      offer.nr AS nr
               FROM offer) AS anon_13,

              (SELECT producttypeproduct.product AS product
               FROM producttypeproduct,
                    producttype AS producttype_ref
               WHERE "producttype_ref"."nr" = '14'
                 AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_14
            WHERE anon_11.nr = anon_12.nr
              AND anon_11.nr = anon_13.nr
              AND anon_14.product = anon_11."""product_ref"".nr_2") AS anon_10
         GROUP BY anon_10."""product_ref"".nr_2") AS anon_5
      WHERE anon_4."""product_ref"".nr_1" = anon_5."""product_ref"".nr_2"
        AND (CAST(CAST(anon_4.price AS VARCHAR) AS FLOAT) < anon_5.avg_1)) AS anon_3
   GROUP BY anon_3."""vendor_ref"".nr_1") AS anon_1,

  (SELECT anon_15."""vendor_ref"".nr_3" AS """vendor_ref"".nr_3",
          count(anon_15.nr) AS count_2
   FROM
     (SELECT anon_16.nr AS nr,
             anon_16."""vendor_ref"".nr_3" AS """vendor_ref"".nr_3",
             anon_17."""product_ref"".nr_3" AS """product_ref"".nr_3"
      FROM
        (SELECT offer.nr AS nr,
                "vendor_ref".nr AS """vendor_ref"".nr_3"
         FROM offer,
              vendor AS vendor_ref
         WHERE "offer".vendor = "vendor_ref".nr) AS anon_16,

        (SELECT offer.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_3"
         FROM offer,
              product AS product_ref
         WHERE "offer".product = "product_ref".nr) AS anon_17,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype AS producttype_ref
         WHERE "producttype_ref"."nr" = '14'
           AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_18
      WHERE anon_16.nr = anon_17.nr
        AND anon_18.product = anon_17."""product_ref"".nr_3") AS anon_15
   GROUP BY anon_15."""vendor_ref"".nr_3") AS anon_2
WHERE anon_1."""vendor_ref"".nr_1" = anon_2."""vendor_ref"".nr_3"
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) DESC, CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
LIMIT 10
```

## Created SQL results
```
bsbm-inst:Vendor1	"0.4444444444444444"^^xsd:double
```

FAIL