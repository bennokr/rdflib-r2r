# bsbm-explore-query11
[bsbm-explore-query11](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ11)

## Random parameter sample
```
OfferXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6>
```

## SPARQL query
```sparql
SELECT ?property ?hasValue ?isValueOf
WHERE {
  { <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6> ?property ?hasValue }
  UNION
  { ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType6> }
}

```

## Goal results
```
rdfs:subClassOf	bsbm-inst:ProductType2	
rdfs:comment	"shucker claviers haggles chorusses nonagons logrolls mathematically intradermal echoed grassier helmeted bristles gonging smidgen flunker atonements bestializes briefness vulgo discounter marooning sheaving neutralizations attains reconsiders glaceed lavers notified malevolently compensations lycanthropies rebroadcasting obliviously sunup arrestee tireless gayer interlinear backlogged encephala chronologist helplessly"	
dc:publisher	bsbm-inst:StandardizationInstitution1	
rdfs:label	"huffiest tougheners interfering"	
dc:date	"2000-06-28"^^xsd:date	
rdf:type	bsbm:ProductType	
rdf:type		bsbm-inst:Product13
rdf:type		bsbm-inst:Product95
rdf:type		bsbm-inst:Product55
rdf:type		bsbm-inst:Product19
rdf:type		bsbm-inst:Product12
rdf:type		bsbm-inst:Product84
rdf:type		bsbm-inst:Product18
rdf:type		bsbm-inst:Product11
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 212, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1038, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 963, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 877, in queryProject
    cols = list(part_query.inner_columns)
AttributeError: 'CompoundSelect' object has no attribute 'inner_columns'

```