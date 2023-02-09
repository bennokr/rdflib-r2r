# bsbm-bi-query6
[bsbm-bi-query6](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ6)

## Random parameter sample
```
Producer = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix rev: <http://purl.org/stuff/rev#>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?reviewer (avg(xsd:float(?score)) As ?reviewerAvgScore)
  {
    { Select (avg(xsd:float(?score)) As ?avgScore)
      {
        ?product bsbm:producer <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3> .
        ?review bsbm:reviewFor ?product .
        { ?review bsbm:rating1 ?score . } UNION
        { ?review bsbm:rating2 ?score . } UNION
        { ?review bsbm:rating3 ?score . } UNION
        { ?review bsbm:rating4 ?score . }
      }
    }
    ?product bsbm:producer <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3> .
    ?review bsbm:reviewFor ?product .
    ?review rev:reviewer ?reviewer .
    { ?review bsbm:rating1 ?score . } UNION
    { ?review bsbm:rating2 ?score . } UNION
    { ?review bsbm:rating3 ?score . } UNION
    { ?review bsbm:rating4 ?score . }
  }
  Group By ?reviewer
  Having (avg(xsd:float(?score)) > min(?avgScore) * 1.5)

```

## Goal results
```
bsbm-inst:Reviewer40	"9.0"^^xsd:double
```

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""person_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS reviewer,
       avg(CAST(anon_1.score AS FLOAT)) AS "reviewerAvgScore"
FROM
  (SELECT anon_2.avg_1 AS avg_1,
          anon_2.nr AS nr,
          anon_2."""product_ref"".nr_1" AS """product_ref"".nr_1",
          anon_2."""person_ref"".nr_1" AS """person_ref"".nr_1",
          anon_3.score AS score
   FROM
     (SELECT anon_4.avg_1 AS avg_1,
             anon_5.nr AS nr,
             anon_5."""product_ref"".nr_1" AS """product_ref"".nr_1",
             anon_5."""person_ref"".nr_1" AS """person_ref"".nr_1"
      FROM
        (SELECT avg(CAST(anon_6.score AS FLOAT)) AS avg_1
         FROM
           (SELECT anon_7.nr AS nr,
                   anon_7."""product_ref"".nr_2" AS """product_ref"".nr_2",
                   anon_8.score AS score
            FROM
              (SELECT anon_9.nr AS nr,
                      anon_9."""product_ref"".nr_2" AS """product_ref"".nr_2"
               FROM
                 (SELECT review.nr AS nr,
                         "product_ref".nr AS """product_ref"".nr_2"
                  FROM review,
                       product AS product_ref
                  WHERE "review".product = "product_ref".nr) AS anon_9,

                 (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                         '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                         CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                         NULL AS g
                  FROM product,
                       producer AS producer_ref
                  WHERE "producer_ref"."nr" = '3'
                    AND "product".producer = "producer_ref".nr
                  UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                   '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                                   CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                   NULL AS g
                  FROM offer,
                       producer AS producer_ref
                  WHERE "producer_ref"."nr" = '3'
                    AND "offer".producer = "producer_ref".nr
                  UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                   '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                                   CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                   NULL AS g
                  FROM review,
                       producer AS producer_ref
                  WHERE "producer_ref"."nr" = '3'
                    AND "review".producer = "producer_ref".nr) AS anon_10
               WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_9."""product_ref"".nr_2" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_10.s) AS anon_7,

              (SELECT anon_11.score AS score,
                      anon_11.review AS review
               FROM
                 (SELECT anon_12.score AS score,
                         anon_12.review AS review
                  FROM
                    (SELECT anon_13.score AS score,
                            CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_13.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
                     FROM
                       (SELECT anon_14.review AS review,
                               anon_14.score AS score
                        FROM
                          (SELECT review.nr AS review,
                                  review.rating1 AS score
                           FROM review) AS anon_14) AS anon_13
                     UNION ALL SELECT anon_15.score AS score,
                                      CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_15.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
                     FROM
                       (SELECT anon_16.score AS score,
                               anon_16.review AS review
                        FROM
                          (SELECT review.rating2 AS score,
                                  review.nr AS review
                           FROM review) AS anon_16) AS anon_15) AS anon_12
                  UNION ALL SELECT anon_17.score AS score,
                                   CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_17.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
                  FROM
                    (SELECT anon_18.score AS score,
                            anon_18.review AS review
                     FROM
                       (SELECT review.rating3 AS score,
                               review.nr AS review
                        FROM review) AS anon_18) AS anon_17) AS anon_11
               UNION ALL SELECT anon_19.score AS score,
                                CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_19.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
               FROM
                 (SELECT anon_20.review AS review,
                         anon_20.score AS score
                  FROM
                    (SELECT review.nr AS review,
                            review.rating4 AS score
                     FROM review) AS anon_20) AS anon_19) AS anon_8
            WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_7.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_8.review) AS anon_6) AS anon_4,

        (SELECT anon_21.nr AS nr,
                anon_21."""product_ref"".nr_1" AS """product_ref"".nr_1",
                anon_22."""person_ref"".nr_1" AS """person_ref"".nr_1"
         FROM
           (SELECT review.nr AS nr,
                   "product_ref".nr AS """product_ref"".nr_1"
            FROM review,
                 product AS product_ref
            WHERE "review".product = "product_ref".nr) AS anon_21,

           (SELECT review.nr AS nr,
                   "person_ref".nr AS """person_ref"".nr_1"
            FROM review,
                 person AS person_ref
            WHERE "review".person = "person_ref".nr) AS anon_22,

           (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                   '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                   CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                   NULL AS g
            FROM product,
                 producer AS producer_ref
            WHERE "producer_ref"."nr" = '3'
              AND "product".producer = "producer_ref".nr
            UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                             NULL AS g
            FROM offer,
                 producer AS producer_ref
            WHERE "producer_ref"."nr" = '3'
              AND "offer".producer = "producer_ref".nr
            UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                             NULL AS g
            FROM review,
                 producer AS producer_ref
            WHERE "producer_ref"."nr" = '3'
              AND "review".producer = "producer_ref".nr) AS anon_23
         WHERE anon_21.nr = anon_22.nr
           AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_21."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_23.s) AS anon_5) AS anon_2,

     (SELECT anon_24.score AS score,
             anon_24.review AS review
      FROM
        (SELECT anon_25.score AS score,
                anon_25.review AS review
         FROM
           (SELECT anon_26.score AS score,
                   CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_26.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
            FROM
              (SELECT anon_27.review AS review,
                      anon_27.score AS score
               FROM
                 (SELECT review.nr AS review,
                         review.rating1 AS score
                  FROM review) AS anon_27) AS anon_26
            UNION ALL SELECT anon_28.score AS score,
                             CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_28.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
            FROM
              (SELECT anon_29.score AS score,
                      anon_29.review AS review
               FROM
                 (SELECT review.rating2 AS score,
                         review.nr AS review
                  FROM review) AS anon_29) AS anon_28) AS anon_25
         UNION ALL SELECT anon_30.score AS score,
                          CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_30.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
         FROM
           (SELECT anon_31.review AS review,
                   anon_31.score AS score
            FROM
              (SELECT review.nr AS review,
                      review.rating3 AS score
               FROM review) AS anon_31) AS anon_30) AS anon_24
      UNION ALL SELECT anon_32.score AS score,
                       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_32.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review
      FROM
        (SELECT anon_33.score AS score,
                anon_33.review AS review
         FROM
           (SELECT review.rating4 AS score,
                   review.nr AS review
            FROM review) AS anon_33) AS anon_32) AS anon_3
   WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_2.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_3.review) AS anon_1
GROUP BY anon_1."""person_ref"".nr_1"
HAVING avg(CAST(anon_1.score AS FLOAT)) > (min(anon_1.avg_1) * 1.5)
```

## Created SQL results
```
bsbm-inst:Reviewer17	"8.666666666666666"^^xsd:double
bsbm-inst:Reviewer40	"9"^^xsd:decimal
```

FAIL