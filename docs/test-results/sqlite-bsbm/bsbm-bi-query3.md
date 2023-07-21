# bsbm-bi-query3
[bsbm-bi-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ3)

## Random parameter sample
```
ConsecutiveMonth_0 = 2008-04-01
ConsecutiveMonth_1 = 2008-05-01
ConsecutiveMonth_2 = 2008-06-01
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix rev: <http://purl.org/stuff/rev#>
  prefix dc: <http://purl.org/dc/elements/1.1/>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?product (xsd:float(?monthCount)/?monthBeforeCount As ?ratio)
  {
    { Select ?product (count(?review) As ?monthCount)
      {
        ?review bsbm:reviewFor ?product .
        ?review dc:date ?date .
        Filter(?date >= "2008-05-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-06-01"^^<http://www.w3.org/2001/XMLSchema#date>) 
      }
      Group By ?product
    }  {
      Select ?product (count(?review) As ?monthBeforeCount)
      {
        ?review bsbm:reviewFor ?product .
        ?review dc:date ?date .
        Filter(?date >= "2008-04-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-05-01"^^<http://www.w3.org/2001/XMLSchema#date>) #
      }
      Group By ?product
      Having (count(?review)>0)
    }
  }
  Order By desc(xsd:float(?monthCount) / ?monthBeforeCount) ?product
  Limit 10

```

## Goal results
```
bsbm-inst:Product40	"4"^^xsd:decimal
bsbm-inst:Product33	"5"^^xsd:decimal
bsbm-inst:Product35	"4"^^xsd:decimal
bsbm-inst:Product65	"7"^^xsd:decimal
bsbm-inst:Product47	"4"^^xsd:decimal
bsbm-inst:Product77	"5"^^xsd:decimal
bsbm-inst:Product92	"4"^^xsd:decimal
bsbm-inst:Product67	"4"^^xsd:decimal
bsbm-inst:Product68	"5"^^xsd:decimal
bsbm-inst:Product53	"3.5"^^xsd:decimal
```

## Created SQL query
```sql
SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) AS ratio
FROM
  (SELECT anon_3."""product_ref"".nr_1" AS """product_ref"".nr_1",
          count(anon_3.s) AS count_1
   FROM
     (SELECT anon_4.s AS s,
             anon_4.o AS o,
             anon_5."""product_ref"".nr_1" AS """product_ref"".nr_1"
      FROM
        (SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://purl.org/dc/elements/1.1/date>' AS p,
                product."publishDate" AS o,
                NULL AS g
         FROM product
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          offer."publishDate" AS o,
                          NULL AS g
         FROM offer
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          review."publishDate" AS o,
                          NULL AS g
         FROM review) AS anon_4,

        (SELECT review.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_1"
         FROM review,
              product AS product_ref
         WHERE "review".product = "product_ref".nr) AS anon_5
      WHERE anon_4.s = '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_5.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
        AND (anon_4.o >= '2008-05-01')
        AND (anon_4.o < '2008-06-01')) AS anon_3
   GROUP BY anon_3."""product_ref"".nr_1") AS anon_1,

  (SELECT anon_6."""product_ref"".nr_2" AS """product_ref"".nr_2",
          count(anon_6.s) AS count_2
   FROM
     (SELECT anon_7.s AS s,
             anon_7.o AS o,
             anon_8."""product_ref"".nr_2" AS """product_ref"".nr_2"
      FROM
        (SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://purl.org/dc/elements/1.1/date>' AS p,
                product."publishDate" AS o,
                NULL AS g
         FROM product
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          offer."publishDate" AS o,
                          NULL AS g
         FROM offer
         UNION ALL SELECT '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          review."publishDate" AS o,
                          NULL AS g
         FROM review) AS anon_7,

        (SELECT review.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_2"
         FROM review,
              product AS product_ref
         WHERE "review".product = "product_ref".nr) AS anon_8
      WHERE anon_7.s = '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_8.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
        AND (anon_7.o >= '2008-04-01')
        AND (anon_7.o < '2008-05-01')) AS anon_6
   GROUP BY anon_6."""product_ref"".nr_2"
   HAVING count(anon_6.s) > 0) AS anon_2
WHERE anon_1."""product_ref"".nr_1" = anon_2."""product_ref"".nr_2"
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) DESC, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
LIMIT 10
```

## Created SQL results
```
bsbm-inst:Product47	"4.0"^^xsd:double
bsbm-inst:Product68	"5.0"^^xsd:double
bsbm-inst:Product77	"5.0"^^xsd:double
bsbm-inst:Product92	"4.0"^^xsd:double
bsbm-inst:Product65	"7.0"^^xsd:double
bsbm-inst:Product67	"4.0"^^xsd:double
bsbm-inst:Product53	"3.5"^^xsd:double
bsbm-inst:Product40	"4.0"^^xsd:double
bsbm-inst:Product33	"5.0"^^xsd:double
bsbm-inst:Product35	"4.0"^^xsd:double
```

FAIL