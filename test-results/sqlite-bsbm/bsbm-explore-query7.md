# bsbm-explore-query7
[bsbm-explore-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ7)

## Random parameter sample
```
currentDate = "2008-07-23"^^<http://www.w3.org/2001/XMLSchema#date>
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product65>
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
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product65> rdfs:label ?productLabel .
    OPTIONAL {
        ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product65> .
		?offer bsbm:price ?price .
		?offer bsbm:vendor ?vendor .
		?vendor rdfs:label ?vendorTitle .
        ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#DE> .
        ?offer dc:publisher ?vendor . 
        ?offer bsbm:validTo ?date .
        FILTER (?date > "2008-07-23"^^<http://www.w3.org/2001/XMLSchema#date> )
    }
    OPTIONAL {
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product65> .
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
"illuminator demeanor henhouses"					bsbm-inst:Review665	"khanates impracticalities viscidity enveloping pharmaceutically industrializing cervicitis universalization pluralities snoutish"@en	bsbm-inst:Reviewer34	"Iaroia-Shabaan"	"4"^^xsd:integer	
"illuminator demeanor henhouses"					bsbm-inst:Review44	"airstream fauces adrenocortical penicillinic gildings goshawks munchies larches"@en	bsbm-inst:Reviewer3	"Danijela-Adalbrand"	"2"^^xsd:integer	"1"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review719	"primeros outwitted assemblers destructing craton lucks pieces medics thwarters"@en	bsbm-inst:Reviewer37	"Sepat-Jelizaveta"		
"illuminator demeanor henhouses"					bsbm-inst:Review698	"bylining scuttler midways nutted pintos"@en	bsbm-inst:Reviewer36	"Tabora-Blanco"		"5"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review240	"scatterbrained shipwright subheading upholsteries"@en	bsbm-inst:Reviewer13	"Inka-Shunsho"	"4"^^xsd:integer	"2"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review272	"duteously transcribers deveining cowpat releasability"@en	bsbm-inst:Reviewer14	"Leonarda-Ajanta"	"3"^^xsd:integer	"3"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review208	"shaggily chronologically comperes stuffily retell"@en	bsbm-inst:Reviewer11	"Fona-Ivanova"	"9"^^xsd:integer	"5"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review79	"dazzler outboxed feasant mintiest cameoed solido aviarists nurserymaid rabbis ferule victress labials rends"@en	bsbm-inst:Reviewer5	"Przemek-Berte"	"1"^^xsd:integer	"6"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review854	"repatriated enunciating animators ural spermatozoon"@en	bsbm-inst:Reviewer44	"Ignacia"	"2"^^xsd:integer	"1"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review503	"sensorial interrupter dunged cribber celandines approximation pegless dicotyledons birthed specking roundhouses quaveringly tunings"@en	bsbm-inst:Reviewer26	"Autolycus-Christy"		"6"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review523	"strives acidoses sardinians calculatingly grayness macaroni proceeds arsonic nontechnical inflammative hallucinates"@en	bsbm-inst:Reviewer27	"Constantin-Vasilis"	"4"^^xsd:integer	"4"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review967	"foliages molls interpreters audiometrist magistracies caskets dragster hinderers chapels darks hakeems frankest encasement brownest"@en	bsbm-inst:Reviewer49	"Patrice-Aristea"	"4"^^xsd:integer	"6"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review427	"overseership deionizations bestialize retested wheats aerating slouchiest depreciatingly assonantly decollated bosh consomme sepulchered"@en	bsbm-inst:Reviewer22	"Toichi-Pavlya"		"10"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review279	"playmates hidebound sensitometric lassitudes swabbie tideways perpetually"@en	bsbm-inst:Reviewer15	"Kirtana"	"2"^^xsd:integer	"6"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review460	"picoseconds frowningly blabbers anticlines engraves scission votaries rehearses ophidian avast"@en	bsbm-inst:Reviewer24	"Danja-Hroswitha"	"3"^^xsd:integer	"8"^^xsd:integer
"illuminator demeanor henhouses"					bsbm-inst:Review266	"changeful ottawas sparking keeper trackers unmorality modernness commiserative nutcrackers semiresolute samechs grograms peddler"@en	bsbm-inst:Reviewer14	"Leonarda-Ajanta"		
"illuminator demeanor henhouses"					bsbm-inst:Review876	"scrambling anatomies guzzled repossessed intricately toddies"@en	bsbm-inst:Reviewer45	"Manu-Liron"		
"illuminator demeanor henhouses"					bsbm-inst:Review448	"molecularly complies bursae mushiness threnodies dozening freeborn discolored villainess gibbering lover"@en	bsbm-inst:Reviewer23	"Analeigh-Oda"		"8"^^xsd:integer
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 212, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1041, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 991, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 966, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 878, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 935, in queryLeftJoin
    query1, var_subform1 = self.queryPart(conn, part.p1)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 954, in queryLeftJoin
    fromquery = query1.join(query2, onclause=onclause, isouter=True)
  File "<string>", line 2, in join
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/base.py", line 104, in _generative
    x = fn(self, *args, **kw)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/selectable.py", line 5127, in join
    target = coercions.expect(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 211, in expect
    return impl._implicit_coercions(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 915, in _implicit_coercions
    self._raise_for_expected(original_element, argname, resolved)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/coercions.py", line 282, in _raise_for_expected
    util.raise_(exc.ArgumentError(msg, code=code), replace_context=err)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
sqlalchemy.exc.ArgumentError: Join target, typically a FROM expression, or ORM relationship attribute expected, got <sqlalchemy.sql.selectable.Select object at 0x7f95e55c43a0>.

```