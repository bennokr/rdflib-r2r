# bsbm-explore-query8
[bsbm-explore-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ8)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product22>
```

## SPARQL query
```sparql
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?title ?text ?reviewDate ?reviewer ?reviewerName ?rating1 ?rating2 ?rating3 ?rating4 
WHERE { 
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product22> .
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
"surveils everglade glottologies altered reletter fabulists collectivists avowable finical"@en	"generalizing cougher keltics gangrene tabarded disentitling acetifies albums devastator emblems skidoo embittering erratas hawses categorizes inevitability wigeon orchestrator deuced videotapes neurotransmitter eyeletted discursiveness triads fabling armchairs leveling azoic handler parasiticidic barrens submersed anathematize aqueducts seismically pharmacies credibly lawyerly erupts finaglers cions herbarium godheads landed floatages interjectionally sleekening eon overdrafts laster pealing rezoned overflight quitrents scarey singhalese debunkers knotholes resists reenactments redistricted disrobed decentered assegais niacins fussing nix victims grappling feudists villus fashioning filtering nightman sociability flourished bally chields sparriest germicides incivility unappreciative unraised veracities capacitances denominator proudness zombies impressments ungrudging violoncellists sharpshooter asphyxiates subcommittee intransigents outguesses reappointing jemmy misrepresentations stays jetties"@en	"2008-05-14"^^xsd:date	bsbm-inst:Reviewer40	"Aroghetto-Etelani"	"9"^^xsd:integer	"1"^^xsd:integer		"3"^^xsd:integer
"untranslatable peevishness privily astrologers"@en	"schussing apneal doodling reendowing catapulted quipu jousting ringmasters acquiesence donjons descried fins incunabulum coprocessors unhandy pangolins upswells wholes coordinator outputted prudentially oceanaut tautened tarps scrutator internalization mouthy dermabrasion glassed esophageal chilies claxon quarantining sottish excisions drapeable homeopathic apocryphally bashing aggregations salivas incautiously manus metamorphosed mitts unpossessively gainsaying reenjoyed geums bluecoat belling cabined keeler comity gaveller yowie coaches kicking lagoons unexpectedly gnarled encapsuled consummates mistbow tumbling tantaras airfoils cliquishly subbreed goodnight unaccomplished gibsons shopping gayeties injudiciousness dialyzed mudsills preaccustoming cotyledons nonstrikers gonadectomizing relinquishing deducing sistering fishways rippliest humanness polemics primitives curing jabbering niches assagai caromed impurely portrayed chias kynurenic seconders halberd optimists yielder gibers stoniness reattach gloggs claimers reinform dilatations overrefining zizzling kicks interplays playsuits reorganized saves tabued fistic remigrates outtrumped totes sadomasochism dismally roofers ajiva uppercuts immedicable grapier zoophobia priviest recutting spindly verminously androgynies wonts waisted fingering sullenly receivability territorializing transitively luggages diacritics denounced lacrosses swordsmen cheatingly enjoined teenyboppers chestier marrows iridescence calculably poky unendorsed riffles appendant wedging cryonics supports interdicted suzettes regattas gracefulness thrummy swarmer byroads suppliant sceptering rebating dayglow roisters balks provability seniorities pastorate urogenital vowless fingerboard multiples conjectured"@en	"2007-10-22"^^xsd:date	bsbm-inst:Reviewer6	"Caryn"	"6"^^xsd:integer	"8"^^xsd:integer	"2"^^xsd:integer	"7"^^xsd:integer
"readjournments groping postconvalescent paranoids wornout fallers"@en	"subchapters unmasks bandages bungled gooders louping embracer gondoliers walleye synchronizes irritative obeisance tumidity disfigured unwrapped arenas choreographer overkill stilts senoras osmotically westernizing reopening snorer heathered kajeput lilts defoliators sublease ambidexter encamp doxy initialize racketed forworn erenow floaters files graupel gushers torchbearers livings deserters harder avenues medievally beltings amoks tankfuls dullness experimentalist ungoverned serological seizable syndromes avocational topped scummers aliveness commented transistorized pachysandras lasters pharmacologist communicability twat dirtiness wicker sateens seasides refilters capitalization pepsins symboling noncontradictory eclipsing intentioned thrusts abbotship pythagoreans downheartedly malignly points medicably infests merlon dawning graduating motionlessly impasses foodservices easer anviltops unapt contemptuousness coruscations depictions bewitchments sniffily dapperly nondairy connecter scamping nonnitrogenous scurvier generalizes toolroom vips expressiveness yogurts artfully aerating caponizing wayfarers decorators panocha bluffest semicircular lapsus erecter evokes mirv artworks rhizomes midtowns cypriotes quarrier remigrations greatens figments acclimatized divans scabies lubricants achiness aloofly monkeyed wealthiness winoes supplementer filibusters demonstrators hokypoky panchromatic resting wagger continuances cabinetwork abjectness stabilities displacement indifference praxeological overvalues ores shielders enflamed physiognomical catmint vocalizes ladders constructionist beekeeper naturalist paraffined censoriously valvular dowagers tabaret camps unburied lased apologues underran exhibits sissier arrowing vestured monopoles allurements metre banishments canniness limned heftiest spherometer slenderizing cheesily lichening grandness tillage handless marshaling hooter"@en	"2007-08-15"^^xsd:date	bsbm-inst:Reviewer47	"Gebharde-Yumako"	"8"^^xsd:integer	"6"^^xsd:integer	"6"^^xsd:integer	"9"^^xsd:integer
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 230, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1063, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 1013, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1008, in queryPart
    return self.querySlice(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 949, in querySlice
    query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 896, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1004, in queryPart
    return self.queryOrderBy(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 905, in queryOrderBy
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 984, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 827, in queryFilter
    clause = self.queryExpr(conn, part.expr, var_cf).expr()
  File "/rdflib_r2r/r2r_store.py", line 804, in queryExpr
    raise SparqlNotImplementedError(e)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_LANGMATCHES' Builtin_LANGMATCHES_Builtin_LANGMATCHES_{'arg1': Builtin_LANG_{'arg': rdflib.term.Variable('text'), '_vars': {rdflib.term.Variable('text')}}, 'arg2': rdflib.term.Literal('EN'), '_vars': {rdflib.term.Variable('text')}}

```