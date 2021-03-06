# bsbm-explore-query7
[bsbm-explore-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ7)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product74>
currentDate = "2008-07-19"^^<http://www.w3.org/2001/XMLSchema#date>
```

## SPARQL query
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?productLabel ?offer ?price ?vendor ?vendorTitle ?review ?revTitle 
       ?reviewer ?revName ?rating1 ?rating2
WHERE { 
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product74> rdfs:label ?productLabel .
    OPTIONAL {
        ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product74> .
		?offer bsbm:price ?price .
		?offer bsbm:vendor ?vendor .
		?vendor rdfs:label ?vendorTitle .
        ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#DE> .
        ?offer dc:publisher ?vendor . 
        ?offer bsbm:validTo ?date .
        FILTER (?date > "2008-07-19"^^<http://www.w3.org/2001/XMLSchema#date> )
    }
    OPTIONAL {
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product74> .
	?review rev:reviewer ?reviewer .
	?reviewer foaf:name ?revName .
	?review dc:title ?revTitle .
    OPTIONAL { ?review bsbm:rating1 ?rating1 . }
    OPTIONAL { ?review bsbm:rating2 ?rating2 . } 
    }
}
```

## Goal results
```
"embow"					bsbm-inst:Review45	"blowsily sublimes freeload binding lordly embryogenic modification replacements tracks subsiding nutritiousness sheols"@en	bsbm-inst:Reviewer3	"Danijela-Adalbrand"		"5"^^xsd:integer
"embow"					bsbm-inst:Review190	"aggressively tangs individuating firepans overfatigued sports"@en	bsbm-inst:Reviewer10	"Shareese-Amaya"	"10"^^xsd:integer	"10"^^xsd:integer
"embow"					bsbm-inst:Review343	"forsaker ladles loutishly regimes blimps calcification adducted benevolently laparotomy rigors headaches"@en	bsbm-inst:Reviewer18	"Emmy"	"9"^^xsd:integer	
"embow"					bsbm-inst:Review384	"yellowest spears valvelets liquors unobserved clack globetrotter unsalted contrasts founded bechamel laboriousness bitterness"@en	bsbm-inst:Reviewer21	"Analee-Lorenz"	"5"^^xsd:integer	"4"^^xsd:integer
"embow"					bsbm-inst:Review242	"heralding crashed dragropes tommyrot impecuniously impanels cons pocketing underages predominately glens wheals stenciling purslanes"@en	bsbm-inst:Reviewer13	"Inka-Shunsho"	"5"^^xsd:integer	"6"^^xsd:integer
"embow"					bsbm-inst:Review244	"rarefaction obsoleting revalues annalists advocates cumulonimbus"@en	bsbm-inst:Reviewer13	"Inka-Shunsho"	"9"^^xsd:integer	
"embow"					bsbm-inst:Review180	"erupted lecturing instincts clarinettists"@en	bsbm-inst:Reviewer9	"Takiji-Yaphet"	"2"^^xsd:integer	"7"^^xsd:integer
"embow"					bsbm-inst:Review609	"pingers resowing vans boatsmen disregardful enfranchise wadded"@en	bsbm-inst:Reviewer30	"Raymon-Lonni"	"1"^^xsd:integer	"7"^^xsd:integer
```

## Created SQL query
```sql
SELECT anon_1."productLabel" AS "productLabel",
       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS offer,
       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_1."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS vendor,
       anon_1.o AS "vendorTitle",
       anon_1.price AS price,
       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_2.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS review,
       CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_2."""person_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS reviewer,
       CAST('"' AS VARCHAR) || CAST(anon_2."revTitle" AS VARCHAR) || CAST('"@en' AS VARCHAR) AS "revTitle",
       anon_2."revName" AS "revName",
       anon_2.rating1 AS rating1,
       anon_2.rating2 AS rating2
FROM
  (SELECT anon_3."productLabel" AS "productLabel",
          anon_4.nr AS nr,
          anon_4."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
          anon_4.o AS o,
          anon_4.date AS date,
          anon_4.price AS price
   FROM
     (SELECT anon_5."productLabel" AS "productLabel"
      FROM
        (SELECT product.label AS "productLabel"
         FROM product
         WHERE "product"."nr" = '74') AS anon_5) AS anon_3,

     (SELECT anon_6.nr AS nr,
             anon_6."""vendor_ref"".nr_1" AS """vendor_ref"".nr_1",
             anon_7.o AS o,
             anon_8.date AS date,
             anon_8.price AS price
      FROM
        (SELECT offer.nr AS nr,
                "vendor_ref".nr AS """vendor_ref"".nr_1"
         FROM offer,
              vendor AS vendor_ref
         WHERE "offer".vendor = "vendor_ref".nr) AS anon_6,

        (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                product.label AS o,
                NULL AS g
         FROM product
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          producer.label AS o,
                          NULL AS g
         FROM producer
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://www.w3.org/2000/01/rdf-schema#label>' AS p,
                          vendor.label AS o,
                          NULL AS g
         FROM vendor) AS anon_7,

        (SELECT offer.nr AS offer,
                offer."validTo" AS date,
                offer.price AS price
         FROM offer) AS anon_8,

        (SELECT offer.nr AS nr,
                "vendor_ref".nr AS """vendor_ref"".nr_2"
         FROM offer,
              vendor AS vendor_ref
         WHERE "offer".publisher = "vendor_ref".nr) AS anon_9,

        (SELECT offer.nr AS nr
         FROM offer,
              product AS product_ref
         WHERE "product_ref"."nr" = '74'
           AND "offer".product = "product_ref".nr) AS anon_10,

        (SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(producer.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                NULL AS g
         FROM producer
         WHERE "producer"."country" = 'DE'
         UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/country>' AS p,
                          CAST('<' AS VARCHAR) || CAST('http://downlode.org/rdf/iso-3166/countries#' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(vendor.country AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
                          NULL AS g
         FROM vendor
         WHERE "vendor"."country" = 'DE') AS anon_11
      WHERE anon_6.nr = anon_9.nr
        AND anon_6.nr = anon_10.nr
        AND anon_6.nr = anon_8.offer
        AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_6."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_11.s
        AND anon_6."""vendor_ref"".nr_1" = anon_9."""vendor_ref"".nr_2"
        AND CAST('<' AS VARCHAR) || CAST('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Vendor' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(anon_6."""vendor_ref"".nr_1" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) = anon_7.s) AS anon_4) AS anon_1,

  (SELECT anon_12.nr AS nr,
          anon_12."""person_ref"".nr_1" AS """person_ref"".nr_1",
          anon_12."revTitle" AS "revTitle",
          anon_12."revName" AS "revName",
          anon_12.rating1 AS rating1,
          anon_13.rating2 AS rating2
   FROM
     (SELECT anon_14.nr AS nr,
             anon_14."""person_ref"".nr_1" AS """person_ref"".nr_1",
             anon_14."revTitle" AS "revTitle",
             anon_14."revName" AS "revName",
             anon_15.rating1 AS rating1
      FROM
        (SELECT anon_16.nr AS nr,
                anon_16."""person_ref"".nr_1" AS """person_ref"".nr_1",
                anon_17."revTitle" AS "revTitle",
                anon_18."revName" AS "revName"
         FROM
           (SELECT review.nr AS nr,
                   "person_ref".nr AS """person_ref"".nr_1"
            FROM review,
                 person AS person_ref
            WHERE "review".person = "person_ref".nr) AS anon_16,

           (SELECT CAST(review.title AS VARCHAR) AS "revTitle",
                   review.nr AS review
            FROM review) AS anon_17,

           (SELECT person.nr AS reviewer,
                   person.name AS "revName"
            FROM person) AS anon_18,

           (SELECT review.nr AS nr
            FROM review,
                 product AS product_ref
            WHERE "product_ref"."nr" = '74'
              AND "review".product = "product_ref".nr) AS anon_19
         WHERE anon_16.nr = anon_19.nr
           AND anon_16.nr = anon_17.review
           AND anon_18.reviewer = anon_16."""person_ref"".nr_1") AS anon_14,

        (SELECT anon_20.rating1 AS rating1,
                anon_20.review AS review
         FROM
           (SELECT review.rating1 AS rating1,
                   review.nr AS review
            FROM review) AS anon_20) AS anon_15
      WHERE anon_14.nr = anon_15.review) AS anon_12,

     (SELECT anon_21.review AS review,
             anon_21.rating2 AS rating2
      FROM
        (SELECT review.nr AS review,
                review.rating2 AS rating2
         FROM review) AS anon_21) AS anon_13
   WHERE anon_12.nr = anon_13.review) AS anon_2
```

## Created SQL results
```

```

FAIL