
# bsbm-bi-query6

## Random parameter sample
```
{'Producer': '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3>'}
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
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(anon_1.reviewer AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS reviewer,
       avg(CAST(anon_2.score AS FLOAT)) AS "reviewerAvgScore"
FROM
  (SELECT anon_3.avg_1 AS avg_1,
          anon_4.s AS s,
          anon_4.reviewer AS reviewer,
          anon_4.review AS review
   FROM
     (SELECT avg(CAST(anon_5.score AS FLOAT)) AS avg_1
      FROM
        (SELECT anon_6.review AS review,
                anon_6.score AS score
         FROM
           (SELECT anon_7.review AS review,
                   anon_7.score AS score
            FROM
              (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_8.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                      anon_8.score AS score
               FROM
                 (SELECT anon_9.score AS score,
                         anon_9.review AS review
                  FROM
                    (SELECT review.rating1 AS score,
                            review.nr AS review
                     FROM review) AS anon_9) AS anon_8
               UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_10.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                                anon_10.score AS score
               FROM
                 (SELECT anon_11.review AS review,
                         anon_11.score AS score
                  FROM
                    (SELECT review.nr AS review,
                            review.rating2 AS score
                     FROM review) AS anon_11) AS anon_10) AS anon_7
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_12.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                             anon_12.score AS score
            FROM
              (SELECT anon_13.score AS score,
                      anon_13.review AS review
               FROM
                 (SELECT review.rating3 AS score,
                         review.nr AS review
                  FROM review) AS anon_13) AS anon_12) AS anon_6
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_14.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                          anon_14.score AS score
         FROM
           (SELECT anon_15.score AS score,
                   anon_15.review AS review
            FROM
              (SELECT review.rating4 AS score,
                      review.nr AS review
               FROM review) AS anon_15) AS anon_14) AS anon_5,

        (SELECT anon_17.s AS s,
                anon_18.review AS review
         FROM
           (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                   '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                   '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                        (SELECT "producer".nr
                                                                                                                                                         FROM producer
                                                                                                                                                         WHERE "producer"."nr" = '3'
                                                                                                                                                           AND "offer".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                   NULL AS g
            FROM offer
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                                  (SELECT "producer".nr
                                                                                                                                                                   FROM producer
                                                                                                                                                                   WHERE "producer"."nr" = '3'
                                                                                                                                                                     AND "review".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                             NULL AS g
            FROM review
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                                  (SELECT "producer".nr
                                                                                                                                                                   FROM producer
                                                                                                                                                                   WHERE "producer"."nr" = '3'
                                                                                                                                                                     AND "product".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                             NULL AS g
            FROM product) AS anon_17,

           (SELECT
              (SELECT "product".nr
               FROM product
               WHERE "review".product = "product".nr) AS product,
                   review.nr AS review
            FROM review) AS anon_18
         WHERE anon_17.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_18.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>') AS anon_16
      WHERE '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_16.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_5.review) AS anon_3,

     (SELECT anon_19.s AS s,
             anon_20.reviewer AS reviewer,
             anon_20.review AS review
      FROM
        (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                     (SELECT "producer".nr
                                                                                                                                                      FROM producer
                                                                                                                                                      WHERE "producer"."nr" = '3'
                                                                                                                                                        AND "offer".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                NULL AS g
         FROM offer
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                          '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                               (SELECT "producer".nr
                                                                                                                                                                FROM producer
                                                                                                                                                                WHERE "producer"."nr" = '3'
                                                                                                                                                                  AND "review".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM review
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                          '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                               (SELECT "producer".nr
                                                                                                                                                                FROM producer
                                                                                                                                                                WHERE "producer"."nr" = '3'
                                                                                                                                                                  AND "product".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM product) AS anon_19,

        (SELECT
           (SELECT "product".nr
            FROM product
            WHERE "review".product = "product".nr) AS product,

           (SELECT "person".nr
            FROM person
            WHERE "review".person = "person".nr) AS reviewer,
                review.nr AS review
         FROM review) AS anon_20
      WHERE anon_19.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_20.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>') AS anon_4) AS anon_1,

  (SELECT anon_21.review AS review,
          anon_21.score AS score
   FROM
     (SELECT anon_22.review AS review,
             anon_22.score AS score
      FROM
        (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_23.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                anon_23.score AS score
         FROM
           (SELECT anon_24.score AS score,
                   anon_24.review AS review
            FROM
              (SELECT review.rating1 AS score,
                      review.nr AS review
               FROM review) AS anon_24) AS anon_23
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_25.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                          anon_25.score AS score
         FROM
           (SELECT anon_26.score AS score,
                   anon_26.review AS review
            FROM
              (SELECT review.rating2 AS score,
                      review.nr AS review
               FROM review) AS anon_26) AS anon_25) AS anon_22
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_27.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                       anon_27.score AS score
      FROM
        (SELECT anon_28.score AS score,
                anon_28.review AS review
         FROM
           (SELECT review.rating3 AS score,
                   review.nr AS review
            FROM review) AS anon_28) AS anon_27) AS anon_21
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_29.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                    anon_29.score AS score
   FROM
     (SELECT anon_30.review AS review,
             anon_30.score AS score
      FROM
        (SELECT review.nr AS review,
                review.rating4 AS score
         FROM review) AS anon_30) AS anon_29) AS anon_2
WHERE '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_1.review AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_2.review
GROUP BY anon_1.reviewer
HAVING avg(CAST(anon_2.score AS FLOAT)) > (min(anon_1.avg_1) * 1.5)
```

## Created SQL results
```

```
