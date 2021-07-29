# bsbm-explore-query11
[bsbm-explore-query11](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ11)

## Random parameter sample
```
OfferXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType11>
```

## SPARQL query
```sparql
SELECT ?property ?hasValue ?isValueOf
WHERE {
  { <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType11> ?property ?hasValue }
  UNION
  { ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType11> }
}

```

## Goal results
```
rdf:type		bsbm-inst:Product48
dc:date	"2000-06-22"^^xsd:date	
rdf:type		bsbm-inst:Product71
rdf:type		bsbm-inst:Product75
rdf:type		bsbm-inst:Product73
rdf:type		bsbm-inst:Product10
rdfs:label	"playacted"	
rdfs:subClassOf	bsbm-inst:ProductType3	
rdf:type	bsbm:ProductType	
dc:publisher	bsbm-inst:StandardizationInstitution1	
rdf:type		bsbm-inst:Product3
rdfs:comment	"squeegeed disappointed gabbled misunderstand deriving obituaries eulogist saboteur sward maintops preterit auricled reddened befuddles sidelights reexchanged soothingly conscripts tigrish broguery distributing unconventionalized kvetches fomentation habituation elmy obeisances birdied pseudonymous cabby copulae easels checker exchequers remodifies spatulate upload ceramist kakis infuriation upholsterer plumberies incipiencies"	
rdf:type		bsbm-inst:Product1
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 230, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1063, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 1013, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 898, in queryProject
    cols = list(part_query.inner_columns)
AttributeError: 'CompoundSelect' object has no attribute 'inner_columns'

```