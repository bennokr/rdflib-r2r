# bsbm-bi-query7
[bsbm-bi-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ7)

## Random parameter sample
```
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType8>
Country = <http://downlode.org/rdf/iso-3166/countries#KR>
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
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType8> .
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
      FILTER(?country=<http://downlode.org/rdf/iso-3166/countries#KR>)
    }
  }

```

## Goal results
```
bsbm-inst:Product98
bsbm-inst:Product72
bsbm-inst:Product52
bsbm-inst:Product34
bsbm-inst:Product46
bsbm-inst:Product50
bsbm-inst:Product99
bsbm-inst:Product26
bsbm-inst:Product54
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
      WHERE "producttype_ref"."nr" = '8'
        AND "producttypeproduct".productType = "producttype_ref".nr) AS anon_3
   WHERE anon_3.product = anon_2."""product_ref"".nr_1") AS anon_1
WHERE NOT (EXISTS
             (SELECT anon_4.nr,
                     anon_4."""product_ref"".nr_2",
                     anon_5."""vendor_ref"".nr_1",
                     anon_6.o
              FROM
                (SELECT offer.nr AS nr,
                        "product_ref".nr AS """product_ref"".nr_2"
                 FROM offer,
                      product AS product_ref
                 WHERE "offer".product = "product_ref".nr) AS anon_4,

                (SELECT offer.nr AS nr,
                        "vendor_ref".nr AS """vendor_ref"".nr_1"
                 FROM offer,
                      vendor AS vendor_ref
                 WHERE "offer".vendor = "vendor_ref".nr) AS anon_5,

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
                 FROM person) AS anon_6
              WHERE anon_4.nr = anon_5.nr
                AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_5."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_6.s
                AND anon_6.o = '<http://downlode.org/rdf/iso-3166/countries#KR>'
                AND anon_1."""product_ref"".nr_1" = anon_4."""product_ref"".nr_2"))
GROUP BY anon_1."""product_ref"".nr_1"
ORDER BY count(anon_1.nr) DESC
LIMIT 1000
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product98
bsbm-inst:Product72
bsbm-inst:Product52
bsbm-inst:Product34
bsbm-inst:Product46
bsbm-inst:Product50
bsbm-inst:Product99
bsbm-inst:Product26
bsbm-inst:Product54
```

SUCCES