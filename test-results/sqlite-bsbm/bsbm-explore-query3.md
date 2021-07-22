# bsbm-explore-query3
[bsbm-explore-query3](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ3)

## Random parameter sample
```
ProductFeature1 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature749>
ProductFeature2 = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature169>
y = "491"^^<http://www.w3.org/2001/XMLSchema#integer>
x = "58"^^<http://www.w3.org/2001/XMLSchema#integer>
ProductType = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType17>
```

## SPARQL query
```sparql
PREFIX bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?product ?label
WHERE {
    ?product rdfs:label ?label .
    ?product a <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductType17> .
	?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature749> .
	?product bsbm:productPropertyNumeric1 ?p1 .
	FILTER ( ?p1 > "58"^^<http://www.w3.org/2001/XMLSchema#integer> ) 
	?product bsbm:productPropertyNumeric3 ?p3 .
	FILTER (?p3 < "491"^^<http://www.w3.org/2001/XMLSchema#integer> )
    OPTIONAL { 
        ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature169> .
        ?product rdfs:label ?testVar }
    FILTER (!bound(?testVar)) 
}
ORDER BY ?label
LIMIT 10


```

## Goal results
```
bsbm-inst:Product6	"whistling usurers carried"
```


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 212, in test_bsbm
    sql_query = graph_rdb.store.getSQL(query)
  File "/rdflib_r2r/r2r_store.py", line 1038, in getSQL
    query, var_subform = self.queryPart(conn, queryobj.algebra)
  File "/rdflib_r2r/r2r_store.py", line 988, in queryPart
    return self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 983, in queryPart
    return self.querySlice(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 924, in querySlice
    query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 963, in queryPart
    return self.queryProject(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 875, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 979, in queryPart
    return self.queryOrderBy(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 884, in queryOrderBy
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 959, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 786, in queryFilter
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 985, in queryPart
    return self.queryLeftJoin(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 933, in queryLeftJoin
    query2, var_subform2 = self.queryPart(conn, part.p2)
  File "/rdflib_r2r/r2r_store.py", line 957, in queryPart
    return self.queryBGP(conn, part.triples)
  File "/rdflib_r2r/r2r_store.py", line 670, in queryBGP
    pat_query, subforms = self.queryPattern(metadata, pat, restriction)
  File "/rdflib_r2r/r2r_store.py", line 552, in queryPattern
    raise Exception(f"Didn't get tmaps for {pattern} from {restrict_tmaps}!")
Exception: Didn't get tmaps for (None, rdflib.term.URIRef('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/productFeature'), rdflib.term.URIRef('http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature169')) from {rdflib.term.URIRef('http://example.com/base/#ProductFeature')}!

```