
# [bsbm-bi-query1]([bsbm-bi-query1](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ1))

## Random parameter sample
```
Country2 = <http://downlode.org/rdf/iso-3166/countries#RU>
Country1 = <http://downlode.org/rdf/iso-3166/countries#US>
```

## SPARQL query
```sparql
prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
prefix rev: <http://purl.org/stuff/rev#>

Select ?productType ?reviewCount
{
 { Select ?productType (count(?review) As ?reviewCount)
  {
   ?productType a bsbm:ProductType .
   ?product a ?productType .
   ?product bsbm:producer ?producer .
   ?producer bsbm:country <http://downlode.org/rdf/iso-3166/countries#US> .
   ?review bsbm:reviewFor ?product .
   ?review rev:reviewer ?reviewer .
   ?reviewer bsbm:country <http://downlode.org/rdf/iso-3166/countries#RU> .
  }
  Group By ?productType
 }
}
Order By desc(?reviewCount) ?productType
Limit 10

```

## Goal results
```
bsbm-inst:ProductType7	"10"^^xsd:integer
bsbm-inst:ProductType13	"6"^^xsd:integer
bsbm-inst:ProductType10	"3"^^xsd:integer
bsbm-inst:ProductType11	"3"^^xsd:integer
bsbm-inst:ProductType12	"3"^^xsd:integer
bsbm-inst:ProductType17	"1"^^xsd:integer
bsbm-inst:ProductType18	"1"^^xsd:integer
bsbm-inst:ProductType9	"1"^^xsd:integer
```

## Created SQL query
```sql
SELECT anon_1.o AS "productType",
       count(anon_2.review) AS "reviewCount"
FROM
  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Product>' AS o,
          NULL AS g
   FROM product
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(producttypeproduct.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                            (SELECT "producttype".nr
                                                                                                                                                             FROM producttype
                                                                                                                                                             WHERE "producttypeproduct".productType = "producttype".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM producttypeproduct
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Vendor>' AS o,
                    NULL AS g
   FROM vendor
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Review>' AS o,
                    NULL AS g
   FROM review
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Producer>' AS o,
                    NULL AS g
   FROM producer
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/ProductType>' AS o,
                    NULL AS g
   FROM producttype
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Offer>' AS o,
                    NULL AS g
   FROM offer
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Person>' AS o,
                    NULL AS g
   FROM person
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/ProductFeature>' AS o,
                    NULL AS g
   FROM productfeature) AS anon_1,

  (SELECT review.nr AS review,

     (SELECT "person".nr
      FROM person
      WHERE "review".person = "person".nr) AS reviewer
   FROM review) AS anon_2,

  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
          '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
          NULL AS g
   FROM vendor
   WHERE "vendor"."country" = 'RU'
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                    '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM producer
   WHERE "producer"."country" = 'RU'
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                    '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM person
   WHERE "person"."country" = 'RU') AS anon_3,

  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
          '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
          NULL AS g
   FROM vendor
   WHERE "vendor"."country" = 'US'
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                    '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM producer
   WHERE "producer"."country" = 'US'
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                    '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM person
   WHERE "person"."country" = 'US') AS anon_4,

  (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
          '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                               (SELECT "producer".nr
                                                                                                                                                FROM producer
                                                                                                                                                WHERE "product".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
          NULL AS g
   FROM product
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                    '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                         (SELECT "producer".nr
                                                                                                                                                          FROM producer
                                                                                                                                                          WHERE "review".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM review
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                    '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(
                                                                                                                                                         (SELECT "producer".nr
                                                                                                                                                          FROM producer
                                                                                                                                                          WHERE "offer".producer = "producer".nr) AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM offer) AS anon_5,

  (SELECT review.nr AS review,

     (SELECT "product".nr
      FROM product
      WHERE "review".product = "product".nr) AS product
   FROM review) AS anon_6,

  (SELECT producttype.nr AS "productType"
   FROM producttype) AS anon_7
WHERE anon_3.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(anon_2.reviewer AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
  AND anon_4.s = anon_5.o
  AND anon_5.s = anon_1.s
  AND anon_5.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_6.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
  AND anon_1.o = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' || replace(replace(replace(replace(replace(replace(CAST(anon_7."productType" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
  AND anon_2.review = anon_6.review
GROUP BY anon_1.o
ORDER BY count(anon_2.review) DESC, anon_1.o
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductType7	"10"^^xsd:integer
bsbm-inst:ProductType13	"6"^^xsd:integer
bsbm-inst:ProductType10	"3"^^xsd:integer
bsbm-inst:ProductType11	"3"^^xsd:integer
bsbm-inst:ProductType12	"3"^^xsd:integer
bsbm-inst:ProductType17	"1"^^xsd:integer
bsbm-inst:ProductType18	"1"^^xsd:integer
bsbm-inst:ProductType9	"1"^^xsd:integer
```

SUCCES
