# bsbm-bi-query5
[bsbm-bi-query5](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ5)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix rev: <http://purl.org/stuff/rev#>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?country ?product ?nrOfReviews ?avgPrice
  {
    { Select ?country (max(?nrOfReviews) As ?maxReviews)
      {
        { Select ?country ?product (count(?review) As ?nrOfReviews)
          {
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> .
            ?review bsbm:reviewFor ?product ;
                    rev:reviewer ?reviewer .
            ?reviewer bsbm:country ?country .
          }
          Group By ?country ?product
        }
      }
      Group By ?country
    }
    { Select ?country ?product (avg(xsd:float(xsd:string(?price))) As ?avgPrice)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> .
        ?offer bsbm:product ?product .
        ?offer bsbm:price ?price .
      }
      Group By ?country ?product
    }
    { Select ?country ?product (count(?review) As ?nrOfReviews)
      {
        ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType15> .
        ?review bsbm:reviewFor ?product .
        ?review rev:reviewer ?reviewer .
        ?reviewer bsbm:country ?country .
      }
      Group By ?country ?product
    }
    FILTER(?nrOfReviews=?maxReviews)
  }
  Order By desc(?nrOfReviews) ?country ?product

```

## Goal results
```
<http://downlode.org/rdf/iso-3166/countries#US>	bsbm-inst:Product70	"7"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product25	"2"^^xsd:integer	"4994.044210526316"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product70	"2"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product70	"2"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product82	"2"^^xsd:integer	"5205.682857142857"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#ES>	bsbm-inst:Product25	"2"^^xsd:integer	"4994.044210526316"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#GB>	bsbm-inst:Product82	"2"^^xsd:integer	"5205.682857142857"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product70	"1"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product82	"1"^^xsd:integer	"5205.682857142857"^^xsd:double
```

## Created SQL query
```sql
SELECT anon_1.o AS country,
       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS product,
       anon_1.avg_1 AS "avgPrice",
       anon_2.count_1 AS "nrOfReviews"
FROM
  (SELECT anon_3.o AS o,
          anon_3.max_1 AS max_1,
          anon_4.product AS product,
          anon_4.avg_1 AS avg_1
   FROM
     (SELECT anon_5.o AS o,
             max(anon_5.count_2) AS max_1
      FROM
        (SELECT anon_6.o AS o,
                anon_6.product AS product,
                count(anon_6.nr) AS count_2
         FROM
           (SELECT anon_7.nr AS nr,
                   anon_7."""person_ref"".nr_1" AS """person_ref"".nr_1",
                   anon_8.o AS o,
                   anon_9.product AS product
            FROM
              (SELECT review.nr AS nr,
                      "person_ref".nr AS """person_ref"".nr_1"
               FROM review,
                    person AS person_ref
               WHERE "review".person = "person_ref".nr) AS anon_7,

              (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                      '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                      CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                      NULL AS g
               FROM person
               UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                NULL AS g
               FROM vendor
               UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                NULL AS g
               FROM producer) AS anon_8,

              (SELECT producttypeproduct.product AS product
               FROM producttypeproduct,
                    producttype AS producttype_ref
               WHERE "producttype_ref"."nr" = '15'
                 AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_9,

              (SELECT review.nr AS nr,
                      "product_ref".nr AS """product_ref"".nr_1"
               FROM review,
                    product AS product_ref
               WHERE "review".product = "product_ref".nr) AS anon_10
            WHERE anon_7.nr = anon_10.nr
              AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_7."""person_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_8.s
              AND anon_9.product = anon_10."""product_ref"".nr_1") AS anon_6
         GROUP BY anon_6.o,
                  anon_6.product) AS anon_5
      GROUP BY anon_5.o) AS anon_3,

     (SELECT anon_11.product AS product,
             avg(CAST(CAST(anon_11.price AS VARCHAR) AS FLOAT)) AS avg_1
      FROM
        (SELECT anon_12.product AS product,
                anon_13.nr AS nr,
                anon_14.price AS price
         FROM
           (SELECT producttypeproduct.product AS product
            FROM producttypeproduct,
                 producttype AS producttype_ref
            WHERE "producttype_ref"."nr" = '15'
              AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_12,

           (SELECT offer.nr AS nr,
                   "product_ref".nr AS """product_ref"".nr_2"
            FROM offer,
                 product AS product_ref
            WHERE "offer".product = "product_ref".nr) AS anon_13,

           (SELECT offer.price AS price,
                   offer.nr AS offer
            FROM offer) AS anon_14
         WHERE anon_12.product = anon_13."""product_ref"".nr_2"
           AND anon_13.nr = anon_14.offer) AS anon_11
      GROUP BY anon_11.product) AS anon_4) AS anon_1,

  (SELECT anon_15.o AS o,
          anon_15.product AS product,
          count(anon_15.nr) AS count_1
   FROM
     (SELECT anon_16.nr AS nr,
             anon_16."""person_ref"".nr_2" AS """person_ref"".nr_2",
             anon_17.o AS o,
             anon_18.product AS product
      FROM
        (SELECT review.nr AS nr,
                "person_ref".nr AS """person_ref"".nr_2"
         FROM review,
              person AS person_ref
         WHERE "review".person = "person_ref".nr) AS anon_16,

        (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                NULL AS g
         FROM person
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                          CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                          NULL AS g
         FROM vendor
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                          CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                          NULL AS g
         FROM producer) AS anon_17,

        (SELECT producttypeproduct.product AS product
         FROM producttypeproduct,
              producttype AS producttype_ref
         WHERE "producttype_ref"."nr" = '15'
           AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_18,

        (SELECT review.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_3"
         FROM review,
              product AS product_ref
         WHERE "review".product = "product_ref".nr) AS anon_19
      WHERE anon_16.nr = anon_19.nr
        AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_16."""person_ref"".nr_2" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_17.s
        AND anon_18.product = anon_19."""product_ref"".nr_3") AS anon_15
   GROUP BY anon_15.o,
            anon_15.product) AS anon_2
WHERE anon_1.o = anon_2.o
  AND anon_1.product = anon_2.product
  AND anon_2.count_1 = anon_1.max_1
ORDER BY anon_2.count_1 DESC,
         anon_1.o,
         anon_1.product
```

## Created SQL results
```
<http://downlode.org/rdf/iso-3166/countries#US>	bsbm-inst:Product70	"7"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product25	"2"^^xsd:integer	"4994.0442105263155"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#CN>	bsbm-inst:Product70	"2"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product70	"2"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#DE>	bsbm-inst:Product82	"2"^^xsd:integer	"5205.682857142857"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#ES>	bsbm-inst:Product25	"2"^^xsd:integer	"4994.0442105263155"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#GB>	bsbm-inst:Product82	"2"^^xsd:integer	"5205.682857142857"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product70	"1"^^xsd:integer	"4129.256923076923"^^xsd:double
<http://downlode.org/rdf/iso-3166/countries#JP>	bsbm-inst:Product82	"1"^^xsd:integer	"5205.682857142857"^^xsd:double
```

FAIL