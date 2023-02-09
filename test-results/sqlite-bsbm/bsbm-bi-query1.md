# bsbm-bi-query1
[bsbm-bi-query1](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ1)

## Random parameter sample
```
Country1 = <http://downlode.org/rdf/iso-3166/countries#US>
Country2 = <http://downlode.org/rdf/iso-3166/countries#FR>
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
   ?reviewer bsbm:country <http://downlode.org/rdf/iso-3166/countries#FR> .
  }
  Group By ?productType
 }
}
Order By desc(?reviewCount) ?productType
Limit 10

```

## Goal results
```
bsbm-inst:ProductType7	"4"^^xsd:integer
bsbm-inst:ProductType13	"5"^^xsd:integer
bsbm-inst:ProductType10	"2"^^xsd:integer
bsbm-inst:ProductType11	"2"^^xsd:integer
bsbm-inst:ProductType12	"2"^^xsd:integer
```

## Created SQL query
```sql
SELECT anon_1.o_1 AS "productType",
       count(anon_1.nr) AS "reviewCount"
FROM
  (SELECT anon_2.s AS s,
          anon_2.o AS o,
          anon_3.nr AS nr,
          anon_4."""person_ref"".nr_1" AS """person_ref"".nr_1",
          anon_5.o AS o_1
   FROM
     (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
             CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
             NULL AS g
      FROM product,
           producer AS producer_ref
      WHERE "product".producer = "producer_ref".nr
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM offer,
           producer AS producer_ref
      WHERE "offer".producer = "producer_ref".nr
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producer_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM review,
           producer AS producer_ref
      WHERE "review".producer = "producer_ref".nr) AS anon_2,

     (SELECT review.nr AS nr,
             "product_ref".nr AS """product_ref"".nr_1"
      FROM review,
           product AS product_ref
      WHERE "review".product = "product_ref".nr) AS anon_3,

     (SELECT review.nr AS nr,
             "person_ref".nr AS """person_ref"".nr_1"
      FROM review,
           person AS person_ref
      WHERE "review".person = "person_ref".nr) AS anon_4,

     (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(productfeature.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
             '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/ProductFeature>' AS o,
             NULL AS g
      FROM productfeature
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producttype.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/ProductType>' AS o,
                       NULL AS g
      FROM producttype
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Producer>' AS o,
                       NULL AS g
      FROM producer
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Product>' AS o,
                       NULL AS g
      FROM product
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producttypeproduct.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("producttype_ref".nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM producttypeproduct,
           producttype AS producttype_ref
      WHERE "producttypeproduct".productType = "producttype_ref".nr
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Vendor>' AS o,
                       NULL AS g
      FROM vendor
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Offer>' AS o,
                       NULL AS g
      FROM offer
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Person>' AS o,
                       NULL AS g
      FROM person
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/Review>' AS o,
                       NULL AS g
      FROM review) AS anon_5,

     (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
             CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
             NULL AS g
      FROM producer
      WHERE "producer"."country" = 'US'
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM vendor
      WHERE "vendor"."country" = 'US'
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM person
      WHERE "person"."country" = 'US') AS anon_6,

     (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
             CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
             NULL AS g
      FROM producer
      WHERE "producer"."country" = 'FR'
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM vendor
      WHERE "vendor"."country" = 'FR'
      UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                       '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                       CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                       NULL AS g
      FROM person
      WHERE "person"."country" = 'FR') AS anon_7,

     (SELECT producttype.nr AS "productType"
      FROM producttype) AS anon_8
   WHERE anon_2.s = anon_5.s
     AND anon_2.s = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_3."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
     AND anon_2.o = anon_6.s
     AND anon_3.nr = anon_4.nr
     AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_4."""person_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_7.s
     AND anon_5.o = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_8."productType" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)) AS anon_1
GROUP BY anon_1.o_1
ORDER BY count(anon_1.nr) DESC, anon_1.o_1
LIMIT 10
OFFSET 0
```

## Created SQL results
```
bsbm-inst:ProductType7	"4"^^xsd:integer
bsbm-inst:ProductType13	"5"^^xsd:integer
bsbm-inst:ProductType10	"2"^^xsd:integer
bsbm-inst:ProductType11	"2"^^xsd:integer
bsbm-inst:ProductType12	"2"^^xsd:integer
```

SUCCES