# bsbm-explore-query11
[bsbm-explore-query11](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ11)

## Random parameter sample
```
OfferXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12>
```

## SPARQL query
```sparql
SELECT ?property ?hasValue ?isValueOf
WHERE {
  { <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12> ?property ?hasValue }
  UNION
  { ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType12> }
}

```

## Goal results
```
rdfs:comment	"superintendence egger sandworms dicotyledonous soliloquizing notcher teraphim meanders marines incandescence contortion pillaring cabmen scholium ensnarer tokyoites chichi conches disheartens tailcoats antecedently whitecomb forewing"	
dc:date	"2000-07-05"^^xsd:date	
rdf:type	bsbm:ProductType	
rdfs:label	"linguini repossession energize"	
dc:publisher	bsbm-inst:StandardizationInstitution1	
rdf:type		bsbm-inst:Product60
rdf:type		bsbm-inst:Product87
rdf:type		bsbm-inst:Product85
rdf:type		bsbm-inst:Product37
rdf:type		bsbm-inst:Product58
rdf:type		bsbm-inst:Product41
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
  File "/rdflib_r2r/r2r_store.py", line 880, in queryProject
    cols = list(part_query.inner_columns)
AttributeError: 'CompoundSelect' object has no attribute 'inner_columns'

```