# bsbm-explore-query8
[bsbm-explore-query8](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ8)

## Random parameter sample
```
ProductXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product83>
```

## SPARQL query
```sparql
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?title ?text ?reviewDate ?reviewer ?reviewerName ?rating1 ?rating2 ?rating3 ?rating4 
WHERE { 
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product83> .
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
"pruning moltenly attacked firming underskirt argots slabber syncs stockcars acquiescing"@en	"shaggily proclaimers billed defuze ghettoizing nudeness wantoned carbonized taximan bemired lattices ludicrousness aeroplane unobtruding allotropically tanto washcloths confab flirtingly lungee irrepatriable seafaring bicycler indispositions welcomes intermeshing convexes whoppers attainers hiltless fruiting quarterlies prehardens empoisoned stiffly formful straightener coverts actuated reckonings vituperate weightlessness assizes pewees malines psychosexually nematode violations petioles brigades primogenitors centralizes persevering knots weltering impregnated megabits overpower parches apathies woozier memories creamer chinbone loos gabbers snoutish slalomed waddings shears bolled pistache disclaimant impactors leaner brittleness shawnees ruggedly redrew swiftest surveying rapscallions remarkableness ardently oscillogram submental louden mademoiselle betels sympathize contumely bachelorhood reveled claque reshaper trigonometric viewfinder impearl relinquishing hedonically observed openendedness refreshingly mistrustfulness overcurious incriminated having distichs hierophants assembler shies highbrows sands festoons sodas deceits flounders miaoued whimsical participation regathering boomed aerological gruesomest alluringly forenoons elastics generalizations drupelet"@en	"2008-05-31"^^xsd:date	bsbm-inst:Reviewer39	"Toson-Seki"	"6"^^xsd:integer	"5"^^xsd:integer		"4"^^xsd:integer
"midbody eroticist reproaches preordain monograms recrossed trembly valerians sinuses phalanges"@en	"deserves niacins desalinizes digestant piastre forefeet woolsack hectors beadworks semivoluntary poisoned monistic jousters counteroffer climactically homilies homosexuals trumpeter reverberating gipsy ovally misinstruction iteming outsold hangs geniuses unsettles sparks postulates disemploys prefabricates crofters zyzzyva trails wackier auditing affrayer saliently mayhemming saboteurs pule perpetrating netsukes multiracial schisms polishing irreparably entanglers buffaloing lightheartedness rewind chirpier reciprocative correlatable underrating gleba precipitated tieclasp aureoled pietisms cancers nonagricultural subrules puttee reacclimated versos mollified clarioned helpmeets yellowbellied unsystematically shrouds renegades slurring caddie programable capsizing riband sings versemen"@en	"2008-04-07"^^xsd:date	bsbm-inst:Reviewer24	"Danja-Hroswitha"		"8"^^xsd:integer	"7"^^xsd:integer	"9"^^xsd:integer
"spells tinters atmospherical trainer schmoe prodemocratic pusillanimously"@en	"monogamies shooflies remover nondestructively stevedores redrilled contoured estimators crummier buttered travestied easting nappers cannalling advisability bigamies latchets misrules crotchets tantrums groovy fouling transmutes catamarans harvester unbalance swansdown freakier explainable triangulated compassionately malodorously surpriser brawlier redirected procuration unprovable calorimeters pitier resurrecting croppers vanisher profanity articulating rouged spurreys mas dictronics traditionalists brayer invocations adventured distributively compeller wombier beavering stifling pylons honeymooned slaps amphoras dicer undiffused chieftaincies masculinized lazarette displeasing mullens undemonstrable pisa reciprocally carafe satirizes squabbled pressures gainable puns bastardies proctological chopper qualifiers focusers misdefined verged daringly socialite pedestals bibliotherapist rials supercomputer fishtailed biparted snoopily militias jingliest veiny coolers domestically masculinity platoons legitimism reerects hazelnuts nonaligned precondition vaccination terce reconstructing macaronies daintiest workaholism boxfish phaseal scathed mycologist commercials excretes postludes boohoos soapless timed burnouts comptrollers seabirds nihilistic reencountered dialoguing interlocutrice personable steeply groundlessly hempweeds maleficently drainers myopias outranges pappies spectacularly cardinals restrengthen amoebean obstructors possibler miscall quinols endamages hoaxed malleably effeminately wormer immerses relying myrmidons sketcher berliners drifts crossing ferrotypes thwacked assuring unrecoverable perfecting leasable disconcerted wannest"@en	"2008-03-30"^^xsd:date	bsbm-inst:Reviewer37	"Sepat-Jelizaveta"	"8"^^xsd:integer		"10"^^xsd:integer	
"gunsmith overclouds mandrills handshaking functionality"@en	"breeziest stuffiness transpiring whiplashes prattler heartsick carryall extirpating transitively oldish disproof vaunted tierces wardrobes stones rarify boarded loyalism overpowerful bowwow vagrants godlier seigneurage appended fluted reapportions cabanas dados sangh immunized doffing linier surmised slighter reformed enthronement chirked oddly denting wandering legitimizer playwrights blames inequities bucktails interdictor modernist cheekier splayfooted sombrely totting bludgeoning ripener sconce ingeniousness touchable reapportioning rampageous dehydrogenation huffiest shysters resubscribed tariffs glycemia captiously legalities evictions fornicates omnicompetent salespersons pyorrheas homemaking isoprene dilation sensiblest veganism corbels"@en	"2008-03-10"^^xsd:date	bsbm-inst:Reviewer44	"Ignacia"		"2"^^xsd:integer	"7"^^xsd:integer	
"rubberize looted whipcords sculk venomously offense mammals latitudinarian substantiation interplays philatelist unshackling mustered frugalities semicircle"@en	"battles neutered fagoter bandages resting ceramist hulks beseemed ontological stymies cosmetologists feudalist sketched sculker magnetometer belting correspondingly behemoths foreknowledge lymphs sambas hoariness arraigns centered tactoid deterrence epeeists unstrap plebs scripts beadily fruitages consistorial nonpayment vendibly biodegradability peskiest endways embroiderer colonizers scatologic forced hawknose coulees unhappiness syrups denigrating microfilmer sprightliest pended coatroom despised unpolitic relets muteness devotional reinvents obtrudes recapture guardrail bafflements vocalizers unilaterally reproduces jackroll lory hermetical sunback eclampsia cerebrospinal battened subjugates mimickers forebye iambuses symptomatological mumper clubhouses seashell aeroliths snowcaps decried knickers eternized lecherously scurfiest messianic affectedness middling postholes corroding queens thermosphere neatly bandannas pingrasses necrotically parring individually aswarm liberating catheterizes semipros nickered scrotal helmets decked discolored moil bactericide chills creakier crumpets tooting jugulates airwave depressants showcasing pedigrees dyslexic amender acuteness defecter colluded calumniating repeopling alluded thefts stereoscopic retreaded celerities overshadow fusils fumigated czaritza autogenesis prompted arteriocapillary somniloquist omens seascout swathers subtraction miseducate featherless ignitions vasopressin precleans caesium corner supersaturates sculptresses popishly marmosets adventuresome backwards selfishly temporizing astroid navigation radiators compounds enumerates palmettos moonshine ninepins underemployment noninflammatory stakeouts splendorous humbling dependently hobbledehoys solubilized manganous forebearing antidotes ricked wheyey ushering ilks satyriases braes plunderer atropism tarpapered dissuader criticized beckons heavers volcanologists remarking romanizes"@en	"2008-03-07"^^xsd:date	bsbm-inst:Reviewer23	"Analeigh-Oda"				"3"^^xsd:integer
"annotatively sorters copyreader nonhereditary sensuously nuncupative despotisms predated ungrudgingly gyromagnetic perceptions predestining"@en	"minority instigated lingeries heedfulness kebob swifts dinghies countries disjoined reconstructed stingier borated beechnut deckers cakewalks devilries misquotation stormily ceremonialist flews elusory consulships vultures lubricator adiposities baldricks eoliths laude sprinted selvages soupcons loosed liturgical fissility hatching practicability unexperienced matriculations itchings reemphasizing concertized stammered bathyspheres chorea mimer grits legitimizer writing comeliness chattered tarde wastable pronationalist magnetizers pentalogies elusion fobbed subdirectories mouldered teensier pounders overwriting cartoned eyehole posingly morsels sinusitis underarm charbroil francs pettiest molester confutation mongst converts proboycott vivified treaders shined undaunted radioed plonk sphericity overstay poplins palliations casuistries uncircumstantialy turgors runways explications dampener unwrap questors weighter reactivity aromatically tiddlywinks wanderer sidekick speckles stippling rubbers analgesics frags apostasies tupping donative blandished semilegal equivocacy tanglier petitionee glassily ferrums dangles piercingly"@en	"2008-03-05"^^xsd:date	bsbm-inst:Reviewer26	"Autolycus-Christy"	"3"^^xsd:integer		"6"^^xsd:integer	"4"^^xsd:integer
"djin menstruates clamping aromas tousled trysts flops disestablish prospers"@en	"logwood ruralist subminiaturizes ganevs unsocial backdrops shrinking pharm careens fooling wager crammed contused burdens leered halloos durables sprinkling coalsack estoppel heightens covings southwesterners cuddies buddies superegos hockeys basher atonies lappets nonirritating augends impearls expiator squads chining pleasureful exterminated immersing fluking sexagenarians tensed scarfing chronologically premies deadlocks importations provinces cuckooing fusspots darvon chinked colonizers tabarded yawps embosser tabletting reddishness donations creasing killed wrapt rondeau versional screamer pulchritudinous isthmus mammas tupping abrogation severers mullioned piercers raining valvar thumbtacking baritones attractively oars dressmaking cayenned chubbily rigorousness flyspecks symmetrical fledging gally spindling drossy hedonic stupidly provisoes subcutaneously ethnologist cauliflowers coinhering pattypan esquiring commiserative audiophile unmarrying tams homesickness peatier pettifoggery sonatine felled tracks influents golliwogs scuffed estranging currentness occultly scrods negotiants unmeaning klatches recouping incompliance herring opens nonresidual summa quashed wifeliest holdable believers militarizes hallucinoses unoffensively upholsteries proteinaceous urinogenital corrugation concelebrates discing blenchers dreariness haplessness prefigures shoppes"@en	"2008-02-22"^^xsd:date	bsbm-inst:Reviewer27	"Constantin-Vasilis"	"3"^^xsd:integer	"5"^^xsd:integer	"8"^^xsd:integer	"4"^^xsd:integer
"clubby forehandedly reeky magnificoes pawing"@en	"smears novella cyclizing matricide condominiums penner conspires muffs checkers greedier bestrews immixes damages svelter coxswains aesthetics fondu legalists undernourished inexactly chancering monitored brothels illusiveness arraigned polypod imperturbably pasta mottoes reglue unexpressed chieftaincies lathes couplers interlaces pilaf faithing reverberator asymptotes clavicular welshers clemency drapers comfit autoregulatory countenances waxed avianize frumenty materialism kyat viciously dittoes eskimos ovolo vileness incapabilities hominid edibility hosed pellets inveterately vaporization jerkier synchronization apoplexies unspecific balsamed hypnotized auditors impressments roentgenometry encounterer dogsbodies sounds antiquates maoism patriarchies incorrigibility procapitalists swellheaded cordwood electrotheraputically hams swedes taupe soldering"@en	"2007-11-30"^^xsd:date	bsbm-inst:Reviewer13	"Inka-Shunsho"	"6"^^xsd:integer		"7"^^xsd:integer	"5"^^xsd:integer
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 212, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1041, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 991, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 986, in queryPart
    return self.querySlice(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 927, in querySlice
    query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 966, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 878, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 982, in queryPart
    return self.queryOrderBy(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 887, in queryOrderBy
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 962, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 786, in queryFilter
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 935, in queryLeftJoin
    query1, var_subform1 = self.queryPart(conn, part.p1)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 935, in queryLeftJoin
    query1, var_subform1 = self.queryPart(conn, part.p1)
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
sqlalchemy.exc.ArgumentError: Join target, typically a FROM expression, or ORM relationship attribute expected, got <sqlalchemy.sql.selectable.Select object at 0x7f95e2208c10>.

```