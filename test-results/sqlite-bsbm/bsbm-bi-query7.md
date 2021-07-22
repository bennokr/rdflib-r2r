# bsbm-bi-query7
[link]([bsbm-bi-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ7))

## Random parameter sample
```
Country = <http://downlode.org/rdf/iso-3166/countries#US>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9>
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
            ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> .
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
bsbm-inst:Product51
bsbm-inst:Product56
bsbm-inst:Product30
bsbm-inst:Product29
bsbm-inst:Product9
bsbm-inst:Product86
bsbm-inst:Product100
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_1.product AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS product
FROM
  (SELECT
     (SELECT "product".nr
      FROM product
      WHERE "offer".product = "product".nr) AS product,
          offer.nr AS offer
   FROM offer) AS anon_1,

  (SELECT producttypeproduct.product AS product,

     (SELECT "producttype".nr
      FROM producttype
      WHERE "producttype"."nr" = '9'
        AND "producttypeproduct".productType = "producttype".nr) AS anon_3
   FROM producttypeproduct) AS anon_2
WHERE anon_2.product = anon_1.product
  AND NOT (EXISTS
             (SELECT anon_4.s,
                     anon_4.o,
                     anon_5.offer,
                     anon_5.product
              FROM
                (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(person.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                        '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                        '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(person.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                        NULL AS g
                 FROM person
                 UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                                  NULL AS g
                 FROM producer
                 UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                                  '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                                  '<' || 'http://downlode.org/rdf/iso-3166/countries#' || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                                  NULL AS g
                 FROM vendor) AS anon_4,

                (SELECT offer.nr AS offer,

                   (SELECT "product".nr
                    FROM product
                    WHERE "offer".product = "product".nr) AS product
                 FROM offer) AS anon_5,

                (SELECT
                   (SELECT "vendor".nr
                    FROM vendor
                    WHERE "offer".vendor = "vendor".nr) AS vendor,
                        offer.nr AS offer
                 FROM offer) AS anon_6
              WHERE anon_4.s = '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' || replace(replace(replace(replace(replace(replace(CAST(anon_6.vendor AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>'
                AND anon_5.offer = anon_6.offer
                AND anon_4.o = '<http://downlode.org/rdf/iso-3166/countries#US>'
                AND anon_1.product = anon_5.product))
GROUP BY anon_1.product
ORDER BY count(anon_1.offer) DESC
LIMIT 1000
OFFSET 0
```

## Created SQL results
```
bsbm-inst:Product48
bsbm-inst:Product58
bsbm-inst:Product47
bsbm-inst:Product61
bsbm-inst:Product49
bsbm-inst:Product51
bsbm-inst:Product39
bsbm-inst:Product45
bsbm-inst:Product57
bsbm-inst:Product53
bsbm-inst:Product44
bsbm-inst:Product42
bsbm-inst:Product34
bsbm-inst:Product65
bsbm-inst:Product27
bsbm-inst:Product68
bsbm-inst:Product55
bsbm-inst:Product69
bsbm-inst:Product67
bsbm-inst:Product50
bsbm-inst:Product41
bsbm-inst:Product56
bsbm-inst:Product54
bsbm-inst:Product35
bsbm-inst:Product66
bsbm-inst:Product43
bsbm-inst:Product37
bsbm-inst:Product64
bsbm-inst:Product63
bsbm-inst:Product60
bsbm-inst:Product70
bsbm-inst:Product62
bsbm-inst:Product52
bsbm-inst:Product40
bsbm-inst:Product73
bsbm-inst:Product74
bsbm-inst:Product38
bsbm-inst:Product31
bsbm-inst:Product26
bsbm-inst:Product59
bsbm-inst:Product32
bsbm-inst:Product28
bsbm-inst:Product22
bsbm-inst:Product83
bsbm-inst:Product82
bsbm-inst:Product46
bsbm-inst:Product36
bsbm-inst:Product80
bsbm-inst:Product77
bsbm-inst:Product71
bsbm-inst:Product30
bsbm-inst:Product33
bsbm-inst:Product25
bsbm-inst:Product24
bsbm-inst:Product20
bsbm-inst:Product78
bsbm-inst:Product72
bsbm-inst:Product15
bsbm-inst:Product75
bsbm-inst:Product29
bsbm-inst:Product23
bsbm-inst:Product84
bsbm-inst:Product21
bsbm-inst:Product18
bsbm-inst:Product93
bsbm-inst:Product87
bsbm-inst:Product79
bsbm-inst:Product19
bsbm-inst:Product13
bsbm-inst:Product90
bsbm-inst:Product76
bsbm-inst:Product17
bsbm-inst:Product12
bsbm-inst:Product95
bsbm-inst:Product89
bsbm-inst:Product85
bsbm-inst:Product81
bsbm-inst:Product10
bsbm-inst:Product8
bsbm-inst:Product7
bsbm-inst:Product88
bsbm-inst:Product11
bsbm-inst:Product91
bsbm-inst:Product16
bsbm-inst:Product5
bsbm-inst:Product97
bsbm-inst:Product1
bsbm-inst:Product98
bsbm-inst:Product94
bsbm-inst:Product92
bsbm-inst:Product14
bsbm-inst:Product9
bsbm-inst:Product99
bsbm-inst:Product96
bsbm-inst:Product86
bsbm-inst:Product100
bsbm-inst:Product6
bsbm-inst:Product3
bsbm-inst:Product4
bsbm-inst:Product2
```

FAIL