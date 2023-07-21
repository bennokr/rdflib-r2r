# bsbm-explore-query8
[bsbm-explore-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ8)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product21>
```

## SPARQL query
```sparql
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?title ?text ?reviewDate ?reviewer ?reviewerName ?rating1 ?rating2 ?rating3 ?rating4 
WHERE { 
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product21> .
	?review dc:title ?title .
	?review rev:text ?text .
	FILTER langMatches( lang(?text), "EN" ) 
	?review bsbm:reviewDate ?reviewDate .
	?review rev:reviewer ?reviewer .
	?reviewer foaf:name ?reviewerName .
	OPTIONAL { ?review bsbm:rating1 ?rating1 . }
	OPTIONAL { ?review bsbm:rating2 ?rating2 . }
	OPTIONAL { ?review bsbm:rating3 ?rating3 . }
	OPTIONAL { ?review bsbm:rating4 ?rating4 . }
}
ORDER BY DESC(?reviewDate)
LIMIT 20
```

## Goal results
```
"trampish bimonthlies employments logjams"@en	"impanel pavan borstals trooper nucleoplasmatic freaked honoring cranes ophthalmoscopy dunces seabag brotherly hissings womaned extractive overreact biophysiography snoozers casus pac boches trumping miscarriage rallyists luckless adultly whoppers unuttered cosmogonist cruder youthfulness asked malodors pharmaceutically stratocumuli smells oohing cuckoldry forefingers sapiently meshes chollas tenthly banco diuretically anthropologies campy hitchers cosiest blistery deoxygenating secularizer ozonize ironed hushful tonsuring sequestering reciprocative beys externalism hypotrophies radomes nonmotile hereupon siameses blowby stylizers hoecakes irreproachably"@en	"2008-04-14"^^xsd:date	bsbm-inst:Reviewer21	"Analee-Lorenz"	"9"^^xsd:integer	"5"^^xsd:integer	"2"^^xsd:integer	
"narwhales sanest liberalness metaphase"@en	"lentils rosin irreconcilability welterweight cichlidae promptly toter submembers rocker sordidness freewheeling trollings slithered pounding aggrieving reaccompany basketwork frightens veinings beautification charactery bolding unassessed solved thermometry camphorating repertorial endamages wordier americans manacles monastical bitter litterateur materializes interline forenamed sprattle crotchetiness colts deco realising deters spinsterhood eventuations demagogs oenophiles scummier imply beneficing articulated crosspiece safetying unvarying habited scissors crispy deceitfully transcriber faultiest flattered urethrae immunopathology youthfully arsenious goodliest cloverleaf excitability twiddler concisely gourmand hatchable exhilarates universes jutted hygeist depicting spraddle laurels expediter unmeasured stenciling nonnatural batiste rafter fait raceways packaging depolarize redetermines howbeit daunters limberly destructive numbering capacitation reconsider stretto deans behavior heroize flirtiest functionless warmer takers deprival lynchings scullery trespassers fostering combes brickwork eyehook confection ties devils distributution broker prinked kaliphs hawkweeds foolhardier purlieus undiscernible corsets quantities articulator sprayer quacky cajoleries androgyny midwifes candlesticks collocate funniness vivisectionist insolvency inhering quadrillionth prorated superannuity stingo framing creepier pelf milliners interlibrary pinholes quipus easer scrubby dossing coracle reconnoiter effuse rafts snorters soever heathens glistened outgrowths dyads chalcedonies pitmen intersocietal townfolk leitmotifs reeled heralding decibels brachiation narrows nonluminous chrisms arf intitling"@en	"2008-04-16"^^xsd:date	bsbm-inst:Reviewer48	"Labeeb-Tonasha"			"7"^^xsd:integer	"4"^^xsd:integer
"xanthic cherished chevaux probities copouts lopping tabulated liposoluble"@en	"mesentery yielders liker juiceless cawing chanty seditionist indications butterier besieging gills preestablishing debates layover misdiagnosed pursuing inflammability untrustful waterworthy dauphins synchronization rattans buckets unaccredited stupors evincive riposting nonvoter reclassified lacerates airdropping spongier clastic candler valorizations handsewn debriefing grunters ostia transfusions lampoonery contingentiam princes toolboxes rhetoricians whops naivety gleams unceasing hypochondria dundee newswomen ecumenicism storied curviness discreeter overdelicate lofter bidding adds raffles reimprisons gainsay groundhog bracts skeletally anearing degaussing ballasting teacherage sieging bondmaids paranoids bigamist incorruptibilities crystallization daylit ponderously dandier unprintable hipped ricotta rotes ugli winos subdirectories martyrs plaudit busher displaying dividers baals dehorns capitals gyroscopic tastelessly sideswiping knaves frostwork kidders samphires reconfirm accommodational electorates arsenals clubhauled wringed nuncio pamphleteer evangelical needles passerine toggery beheaded kingdoms berceuse colloids crannied packed wearily corrosively informer surprize misdefine mendacities foreordains insinuations laten integers shriving borons errancies philtre fiducially replacements grograms pinpointing measliest provided wreckers grogshops crenel kaliums cullet"@en	"2008-01-07"^^xsd:date	bsbm-inst:Reviewer23	"Analeigh-Oda"	"6"^^xsd:integer	"6"^^xsd:integer	"1"^^xsd:integer	"9"^^xsd:integer
"impalements ambivalently overprotect disrupts vitalisms liberals sirs outspelling planaria timely multifaced furcated syncopes larboards"@en	"forbearer insulars ledgy shammies talmudist allergology archaisms reprinting alternately subtrahends cents welds moolah exonerating retractions pulques cabals thoued throwaways dramatized saltboxes heifers mastheads freckly turgors dedicator registrability skeined emanation nepotism sherd shinsplints uncorrupted electrophorese couldst afrit atwitter diggings stereotypers dichotic anisette appetizing eviction hornpipe playsuit wainscotting legs flinting veniremen thorp presiders letups orchestrations futurologist airbills fantails etheric lubricated panderers desalinize lilies cassabas shows windpipes preheated tubal outbidden farthings forspent doomful forwardsearch maroons juicing reorganization circularizers hards subagent figurer clericalism bandaged hemisection ungovernable marihuana legislatorial manufacturers handicrafts forebodies pecks clevis nippiest recapitulation kibitzes keepsake faithed trampled cupronickel salmonellas crucifies dakoit hardwares shirtiest baulking procreators stockpots abstractly loneliest hibernators unknowing finitely telepathies loaners untidiest talers wearies togged broaches demobbed hymned bulldozes palish entailments semidesert outclass quilter easting subtropical roaching virologies recapitulate byre inoculative satinwood attractive apian"@en	"2007-10-10"^^xsd:date	bsbm-inst:Reviewer2	"Eyana-Aurelianus"		"3"^^xsd:integer	"3"^^xsd:integer	"7"^^xsd:integer
"noxiousness sidings ovular wastable maximize stoppling unwed folic wholely sleeping planetoids excepts laired purposefulness parlors"@en	"homeostases recuperates morganatic unrentable liquored ladyfinger suckled clerkish badged reproving coddler gossipers triunes fulvous bedeck farness undervalue acknowledged handles alighted asystematic copras dirtying titivate rappels bunts mesmerist curliest roughers levator spruced cursively chitlin psychoanalytical pagination stealths acidified brasiers cultist traitoress shirtfront cattiness forgivers jerkier amiableness dissimilarities commending apostrophes yellower inclusions mononucleosis jocularity serologically repetitions politicoes overbear odeons smilers station crossings misprize fizzed outweighs reweigh scrabblers trochoids tails gallamine splendorous nonseasonal belabour anguishes equivocalness purging datums vocably gastroscope conceitedness nobbling clubfoot reedit alarmingly"@en	"2007-12-24"^^xsd:date	bsbm-inst:Reviewer17	"Domiziana-Emilee"	"2"^^xsd:integer	"2"^^xsd:integer	"3"^^xsd:integer	"7"^^xsd:integer
"phenocopies themes exciters unrolling reprinted shorter uvular outlawed covenantor skeletons nonsurgical contraindicates stretching snarled teenagers"@en	"designee abstinently circulations abstractionism tastier ramming iodizer throngs unsolder parfaits comprized malaprops relicensed candles defamations bewitchments scholars vascularities tolerances dotier fourpenny callings honors plats proliferated monumentally scoping bakemeats broadaxes mullions booking beauticians tracts envelops coercers discos wakened guessed irrigable groped spacing limpers brassier dextro whiskies outargues concordantly cyclically pacesetters cranker shooflies tzetzes succumbs appropriating whaleboats taxonomists apricots interweaved youthens interregnal pennines exiguity nuncio zippers translator abutter hairstreak probatively soppier"@en	"2007-08-08"^^xsd:date	bsbm-inst:Reviewer8	"Linda-Nada"	"1"^^xsd:integer		"9"^^xsd:integer	
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 239, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1083, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 1033, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1028, in queryPart
    return self.querySlice(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 950, in querySlice
    query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1008, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 897, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1024, in queryPart
    return self.queryOrderBy(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 906, in queryOrderBy
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1004, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 827, in queryFilter
    clause = self.queryExpr(conn, part.expr, var_cf).expr()
  File "/rdflib_r2r/r2r_store.py", line 804, in queryExpr
    raise SparqlNotImplementedError(e)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_LANGMATCHES' Builtin_LANGMATCHES_Builtin_LANGMATCHES_{'arg1': Builtin_LANG_{'arg': rdflib.term.Variable('text'), '_vars': {rdflib.term.Variable('text')}}, 'arg2': rdflib.term.Literal('EN'), '_vars': {rdflib.term.Variable('text')}}

```