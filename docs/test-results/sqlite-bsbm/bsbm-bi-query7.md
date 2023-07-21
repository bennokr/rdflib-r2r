# bsbm-bi-query7
[bsbm-bi-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ7)

## Random parameter sample
```
Country = <http://downlode.org/rdf/iso-3166/countries#JP>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType11>
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
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType11> .
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
      FILTER(?country=<http://downlode.org/rdf/iso-3166/countries#JP>)
    }
  }

```

## Goal results
```
bsbm-inst:Product3
bsbm-inst:Product48
bsbm-inst:Product1
bsbm-inst:Product10
bsbm-inst:Product71
bsbm-inst:Product73
bsbm-inst:Product75
```

## Created SQL query
```sql
SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""product_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS product
FROM
  (SELECT anon_2.nr AS nr,
          anon_2."""product_ref"".nr_1" AS """product_ref"".nr_1"
   FROM
     (SELECT offer.nr AS nr,
             "product_ref".nr AS """product_ref"".nr_1"
      FROM offer,
           product AS product_ref
      WHERE "offer".product = "product_ref".nr) AS anon_2,

     (SELECT producttypeproduct.product AS product
      FROM producttypeproduct,
           producttype AS producttype_ref
      WHERE "producttype_ref"."nr" = '11'
        AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_3
   WHERE anon_3.product = anon_2."""product_ref"".nr_1") AS anon_1
WHERE NOT (EXISTS
             (SELECT anon_4.s,
                     anon_4.o,
                     anon_5.nr,
                     anon_6."""product_ref"".nr_2"
              FROM
                (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                        '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                        CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                        NULL AS g
                 FROM producer
                 UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                  NULL AS g
                 FROM vendor
                 UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                                  NULL AS g
                 FROM person) AS anon_4,

                (SELECT offer.nr AS nr,
                        "vendor_ref".nr AS """vendor_ref"".nr_1"
                 FROM offer,
                      vendor AS vendor_ref
                 WHERE "offer".vendor = "vendor_ref".nr) AS anon_5,

                (SELECT offer.nr AS nr,
                        "product_ref".nr AS """product_ref"".nr_2"
                 FROM offer,
                      product AS product_ref
                 WHERE "offer".product = "product_ref".nr) AS anon_6
              WHERE anon_4.s = CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_5."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR)
                AND anon_5.nr = anon_6.nr
                AND anon_4.o = '<http://downlode.org/rdf/iso-3166/countries#JP>'
                AND anon_1."""product_ref"".nr_1" = anon_6."""product_ref"".nr_2"))
GROUP BY anon_1."""product_ref"".nr_1"
ORDER BY count(anon_1.nr) DESC
LIMIT 1000
```

## Created SQL results
```
bsbm-inst:Product3
bsbm-inst:Product48
bsbm-inst:Product1
bsbm-inst:Product10
bsbm-inst:Product71
bsbm-inst:Product73
bsbm-inst:Product75
```

SUCCES