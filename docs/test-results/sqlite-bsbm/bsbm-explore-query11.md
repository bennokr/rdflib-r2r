# bsbm-explore-query11
[bsbm-explore-query11](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ11)

## Random parameter sample
```
OfferXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9>
```

## SPARQL query
```sparql
SELECT ?property ?hasValue ?isValueOf
WHERE {
  { <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> ?property ?hasValue }
  UNION
  { ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType9> }
}

```

## Goal results
```
dc:date	"2000-06-29"^^xsd:date	
rdf:type		bsbm-inst:Product86
rdfs:subClassOf	bsbm-inst:ProductType2	
rdf:type	bsbm:ProductType	
rdfs:comment	"redeposit stepping aidmen baccarats rearms invasiveness foemen inkstand aircrew bravadoes necking enlivenment discolorations pillaging dispossessed pocketknives upsweeps monosyllables slitted secularized visualizer rescheduled graters sheepish airframes ninepin virulence ramshackle packthreads batiste"	
rdf:type		bsbm-inst:Product9
rdf:type		bsbm-inst:Product56
rdf:type		bsbm-inst:Product51
rdf:type		bsbm-inst:Product29
dc:publisher	bsbm-inst:StandardizationInstitution1	
rdf:type		bsbm-inst:Product30
rdf:type		bsbm-inst:Product100
rdfs:label	"weapons zeals"	
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 239, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1083, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 1033, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1008, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 899, in queryProject
    cols = list(part_query.inner_columns)
AttributeError: 'CompoundSelect' object has no attribute 'inner_columns'

```