# bsbm-explore-query7
[link]([bsbm-explore-query7](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ7))

## Random parameter sample
```
currentDate = "2008-07-13"^^<http://www.w3.org/2001/XMLSchema#date>
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product80>
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
	<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product80> rdfs:label ?productLabel .
    OPTIONAL {
        ?offer bsbm:product <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product80> .
		?offer bsbm:price ?price .
		?offer bsbm:vendor ?vendor .
		?vendor rdfs:label ?vendorTitle .
        ?vendor bsbm:country <http://downlode.org/rdf/iso-3166/countries#DE> .
        ?offer dc:publisher ?vendor . 
        ?offer bsbm:validTo ?date .
        FILTER (?date > "2008-07-13"^^<http://www.w3.org/2001/XMLSchema#date> )
    }
    OPTIONAL {
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product80> .
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
"tutors animists rocs"					bsbm-inst:Review807	"menstruum rules deeper heifers booed hornswoggled minicomputers cowled vedic rickettsias stilts flounciest"@en	bsbm-inst:Reviewer42	"Kura-Janette"	"10"^^xsd:integer	
"tutors animists rocs"					bsbm-inst:Review71	"advocacies bludgeons brickiest boneblack uncomfortably analysts wen retranslation mammoths reexhibited kilty"@en	bsbm-inst:Reviewer5	"Przemek-Berte"	"9"^^xsd:integer	"5"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review529	"limpidly scarified swiping frisian minutia sportiest narrates infarcts shopbreaker blankets apologizer frizzers revoker"@en	bsbm-inst:Reviewer27	"Constantin-Vasilis"		"9"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review677	"balladeer reapply nauseates indurating brail catamite unhats monomaniacs effaced capuchin assertors unsafeties bisecting grudgers"@en	bsbm-inst:Reviewer34	"Iaroia-Shabaan"	"10"^^xsd:integer	
"tutors animists rocs"					bsbm-inst:Review367	"nestled exposes moltenly ammonite widowered marching softies inertness proconsuls ramps lamenters"@en	bsbm-inst:Reviewer20	"Hostena-Yasmin"		"9"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review845	"sociopathy bloats turnings bullweed lengthiness oncological respecters pompons quadruplets limiter"@en	bsbm-inst:Reviewer43	"Edmund-Nabeela"		"8"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review920	"elongating retried crosswords sluggishly"@en	bsbm-inst:Reviewer47	"Gebharde-Yumako"		"4"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review310	"bioenergetics sties eely atonally racoon"@en	bsbm-inst:Reviewer16	"Viviane-Stephano"	"9"^^xsd:integer	
"tutors animists rocs"					bsbm-inst:Review308	"incertitude stratigraphy stratums evitable basinets domini counteropening deluded watersheds rattraps bewilderingly panpipes gunships"@en	bsbm-inst:Reviewer16	"Viviane-Stephano"		"5"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review583	"ideologic garbanzos bedstands retributory"@en	bsbm-inst:Reviewer30	"Raymon-Lonni"		"3"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review983	"bedfellow felled roomed terns timbering flamier monetarily tumps gustiest reblooming tentacular"@en	bsbm-inst:Reviewer49	"Patrice-Aristea"	"7"^^xsd:integer	"4"^^xsd:integer
"tutors animists rocs"					bsbm-inst:Review336	"wawls computations plangent asthmatic representor leftists conoid zizzling ounces carbineer lips lube hermeneutical"@en	bsbm-inst:Reviewer18	"Emmy"	"5"^^xsd:integer	
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 212, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1045, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 995, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 970, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 882, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 992, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 939, in queryLeftJoin
    query1, var_subform1 = self.queryPart(conn, part.p1)
  File "/rdflib_r2r/r2r_store.py", line 992, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 958, in queryLeftJoin
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
sqlalchemy.exc.ArgumentError: Join target, typically a FROM expression, or ORM relationship attribute expected, got <sqlalchemy.sql.selectable.Select object at 0x7fc88ceb2280>.

```