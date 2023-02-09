# bsbm-bi-query3
[bsbm-bi-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ3)

## Random parameter sample
```
ConsecutiveMonth_0 = 2007-12-01
ConsecutiveMonth_1 = 2008-01-01
ConsecutiveMonth_2 = 2008-02-01
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
        Filter(?date >= "2008-01-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-02-01"^^<http://www.w3.org/2001/XMLSchema#date>) 
      }
      Group By ?product
    }  {
      Select ?product (count(?review) As ?monthBeforeCount)
      {
        ?review bsbm:reviewFor ?product .
        ?review dc:date ?date .
        Filter(?date >= "2007-12-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-01-01"^^<http://www.w3.org/2001/XMLSchema#date>) #
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
bsbm-inst:Product17	"2"^^xsd:decimal
bsbm-inst:Product62	"2"^^xsd:decimal
bsbm-inst:Product6	"2"^^xsd:decimal
bsbm-inst:Product29	"1"^^xsd:decimal
bsbm-inst:Product31	"2"^^xsd:decimal
bsbm-inst:Product32	"1"^^xsd:decimal
bsbm-inst:Product46	"4"^^xsd:decimal
bsbm-inst:Product33	"1"^^xsd:decimal
bsbm-inst:Product56	"3"^^xsd:decimal
bsbm-inst:Product79	"4"^^xsd:decimal
```

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS product,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) AS ratio
FROM
  (SELECT anon_3."""product_ref"".nr_1" AS """product_ref"".nr_1",
          count(anon_3.nr) AS count_1
   FROM
     (SELECT anon_4.nr AS nr,
             anon_4."""product_ref"".nr_1" AS """product_ref"".nr_1",
             anon_5.o AS o
      FROM
        (SELECT review.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_1"
         FROM review,
              product AS product_ref
         WHERE "review".product = "product_ref".nr) AS anon_4,

        (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                '<http://purl.org/dc/elements/1.1/date>' AS p,
                product."publishDate" AS o,
                NULL AS g
         FROM product
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          offer."publishDate" AS o,
                          NULL AS g
         FROM offer
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          review."publishDate" AS o,
                          NULL AS g
         FROM review) AS anon_5
      WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_4.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_5.s
        AND (anon_5.o >= '2008-01-01')
        AND (anon_5.o < '2008-02-01')) AS anon_3
   GROUP BY anon_3."""product_ref"".nr_1") AS anon_1,

  (SELECT anon_6."""product_ref"".nr_2" AS """product_ref"".nr_2",
          count(anon_6.nr) AS count_2
   FROM
     (SELECT anon_7.nr AS nr,
             anon_7."""product_ref"".nr_2" AS """product_ref"".nr_2",
             anon_8.o AS o
      FROM
        (SELECT review.nr AS nr,
                "product_ref".nr AS """product_ref"".nr_2"
         FROM review,
              product AS product_ref
         WHERE "review".product = "product_ref".nr) AS anon_7,

        (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                '<http://purl.org/dc/elements/1.1/date>' AS p,
                product."publishDate" AS o,
                NULL AS g
         FROM product
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          offer."publishDate" AS o,
                          NULL AS g
         FROM offer
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://purl.org/dc/elements/1.1/date>' AS p,
                          review."publishDate" AS o,
                          NULL AS g
         FROM review) AS anon_8
      WHERE CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_7.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_8.s
        AND (anon_8.o >= '2007-12-01')
        AND (anon_8.o < '2008-01-01')) AS anon_6
   GROUP BY anon_6."""product_ref"".nr_2"
   HAVING count(anon_6.nr) > 0) AS anon_2
WHERE anon_1."""product_ref"".nr_1" = anon_2."""product_ref"".nr_2"
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS REAL) DESC, CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product17	"2"^^xsd:decimal
bsbm-inst:Product62	"2"^^xsd:decimal
bsbm-inst:Product6	"2"^^xsd:decimal
bsbm-inst:Product29	"1"^^xsd:decimal
bsbm-inst:Product31	"2"^^xsd:decimal
bsbm-inst:Product32	"1"^^xsd:decimal
bsbm-inst:Product46	"4"^^xsd:decimal
bsbm-inst:Product33	"1"^^xsd:decimal
bsbm-inst:Product56	"3"^^xsd:decimal
bsbm-inst:Product79	"4"^^xsd:decimal
```

SUCCES