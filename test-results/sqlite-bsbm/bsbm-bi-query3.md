# bsbm-bi-query3
[bsbm-bi-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ3)

## Random parameter sample
```
ConsecutiveMonth_0 = 2008-02-01
ConsecutiveMonth_1 = 2008-03-01
ConsecutiveMonth_2 = 2008-04-01
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
        Filter(?date >= "2008-03-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-04-01"^^<http://www.w3.org/2001/XMLSchema#date>) 
      }
      Group By ?product
    }  {
      Select ?product (count(?review) As ?monthBeforeCount)
      {
        ?review bsbm:reviewFor ?product .
        ?review dc:date ?date .
        Filter(?date >= "2008-02-01"^^<http://www.w3.org/2001/XMLSchema#date> && ?date < "2008-03-01"^^<http://www.w3.org/2001/XMLSchema#date>) #
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
bsbm-inst:Product51	"4"^^xsd:decimal
bsbm-inst:Product12	"3"^^xsd:decimal
bsbm-inst:Product40	"2"^^xsd:decimal
bsbm-inst:Product57	"2"^^xsd:decimal
bsbm-inst:Product60	"2"^^xsd:decimal
bsbm-inst:Product65	"2"^^xsd:decimal
bsbm-inst:Product80	"2"^^xsd:decimal
bsbm-inst:Product16	"1"^^xsd:decimal
bsbm-inst:Product17	"1"^^xsd:decimal
bsbm-inst:Product20	"1"^^xsd:decimal
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr_1 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product,
       CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) AS ratio
FROM
  (SELECT anon_3.nr_1 AS nr_1,
          count(anon_4.s) AS count_1
   FROM
     (SELECT review.nr AS nr,
             product.nr AS nr_1
      FROM review,
           product
      WHERE "review".product = "product".nr) AS anon_3,

     (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
             '<http://purl.org/dc/elements/1.1/date>' AS p,
             product."publishDate" AS o,
             NULL AS g
      FROM product
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                       '<http://purl.org/dc/elements/1.1/date>' AS p,
                       review."publishDate" AS o,
                       NULL AS g
      FROM review) AS anon_4
   WHERE anon_4.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_3.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
     AND (anon_4.o >= '2008-03-01')
     AND (anon_4.o < '2008-04-01')
   GROUP BY anon_3.nr_1) AS anon_1,

  (SELECT anon_5.nr_2 AS nr_2,
          count(anon_6.s) AS count_2
   FROM
     (SELECT review.nr AS nr,
             product.nr AS nr_2
      FROM review,
           product
      WHERE "review".product = "product".nr) AS anon_5,

     (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
             '<http://purl.org/dc/elements/1.1/date>' AS p,
             product."publishDate" AS o,
             NULL AS g
      FROM product
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                       '<http://purl.org/dc/elements/1.1/date>' AS p,
                       review."publishDate" AS o,
                       NULL AS g
      FROM review) AS anon_6
   WHERE anon_6.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_5.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
     AND (anon_6.o >= '2008-02-01')
     AND (anon_6.o < '2008-03-01')
   GROUP BY anon_5.nr_2
   HAVING count(anon_6.s) > 0) AS anon_2
WHERE anon_1.nr_1 = anon_2.nr_2
ORDER BY CAST(CAST(anon_1.count_1 AS FLOAT) / anon_2.count_2 AS FLOAT) DESC, anon_1.nr_1
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product51	"4.0"^^xsd:double
bsbm-inst:Product12	"3.0"^^xsd:double
bsbm-inst:Product40	"2.0"^^xsd:double
bsbm-inst:Product57	"2.0"^^xsd:double
bsbm-inst:Product60	"2.0"^^xsd:double
bsbm-inst:Product65	"2.0"^^xsd:double
bsbm-inst:Product80	"2.0"^^xsd:double
bsbm-inst:Product9	"1.0"^^xsd:double
bsbm-inst:Product16	"1.0"^^xsd:double
bsbm-inst:Product17	"1.0"^^xsd:double
```

FAIL