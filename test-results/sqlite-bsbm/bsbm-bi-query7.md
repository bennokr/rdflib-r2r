# bsbm-bi-query7
[bsbm-bi-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ7)

## Random parameter sample
```
Country = <http://downlode.org/rdf/iso-3166/countries#US>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType17>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?product
  {
    { Select ?product
      { 
        { Select ?product (count(?offer) As ?offerCount)
          { 
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType17> .
            ?offer bsbm:product ?product .
          }
          Group By ?product
        }
      }
      Order By desc(?offerCount)
      Limit 1000
    }
    FILTER NOT EXISTS
    {
      ?offer bsbm:product ?product .
      ?offer bsbm:vendor ?vendor .
      ?vendor bsbm:country ?country .
      FILTER(?country=<http://downlode.org/rdf/iso-3166/countries#US>)
    }
  }

```

## Goal results
```
bsbm-inst:Product44
bsbm-inst:Product35
bsbm-inst:Product43
bsbm-inst:Product32
bsbm-inst:Product77
bsbm-inst:Product94
bsbm-inst:Product6
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr_1 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product
FROM
  (SELECT offer.nr AS nr,
          product.nr AS nr_1
   FROM offer,
        product
   WHERE "offer".product = "product".nr) AS anon_1,

  (SELECT producttypeproduct.product AS product
   FROM producttypeproduct,
        producttype
   WHERE "nr" = '17'
     AND "producttypeproduct".productType = "producttype".nr) AS anon_2
WHERE anon_1.nr_1 = anon_2.product
  AND NOT (EXISTS
             (SELECT anon_3.s,
                     anon_3.o,
                     anon_4.nr,
                     anon_5.nr_2
              FROM
                (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                        '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                        '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                        NULL AS g
                 FROM person
                 UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                                  NULL AS g
                 FROM vendor
                 UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                                  NULL AS g
                 FROM producer) AS anon_3,

                (SELECT offer.nr AS nr,
                        vendor.nr AS nr_3
                 FROM offer,
                      vendor
                 WHERE "offer".vendor = "vendor".nr) AS anon_4,

                (SELECT offer.nr AS nr,
                        product.nr AS nr_2
                 FROM offer,
                      product
                 WHERE "offer".product = "product".nr) AS anon_5
              WHERE anon_3.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(anon_4.nr_3 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
                AND anon_4.nr = anon_5.nr
                AND anon_3.o = '<http://downlode.org/rdf/iso-3166/countries#US>'
                AND anon_1.nr_1 = anon_5.nr_2))
GROUP BY anon_1.nr_1
ORDER BY count(anon_1.nr) DESC
LIMIT 1000
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product44
bsbm-inst:Product35
bsbm-inst:Product43
bsbm-inst:Product32
bsbm-inst:Product77
bsbm-inst:Product94
bsbm-inst:Product6
```

SUCCES