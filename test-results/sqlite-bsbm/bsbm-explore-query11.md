# bsbm-explore-query11
[link]([bsbm-explore-query11](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ11))

## Random parameter sample
```
OfferXYZ = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType20>
```

## SPARQL query
```sparql
SELECT ?property ?hasValue ?isValueOf
WHERE {
  { <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType20> ?property ?hasValue }
  UNION
  { ?isValueOf ?property <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType20> }
}

```

## Goal results
```
dc:date	"2000-07-17"^^xsd:date	
rdfs:comment	"insurrectional bucking accommodations floors degaussing sisterhoods primogeniture stover contumelies fifteens atrociously flagellated microradiographically copes plexiglass fowled disincorporated braises mildly incompetencies virucide overembellishes perfectos dignities perdurability pryers overplaying monistic contraindicated trovers impulsed nulled stumper mackerels plentifully bullfight simpers toasting distributors"	
rdfs:label	"umbellate"	
rdf:type	bsbm:ProductType	
dc:publisher	bsbm-inst:StandardizationInstitution1	
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
  File "/rdflib_r2r/r2r_store.py", line 884, in queryProject
    cols = list(part_query.inner_columns)
AttributeError: 'CompoundSelect' object has no attribute 'inner_columns'

```