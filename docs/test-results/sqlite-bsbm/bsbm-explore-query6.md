# bsbm-explore-query6
[bsbm-explore-query6](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ6)

## Random parameter sample
```
word1 = manliest
```

## SPARQL query
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>

SELECT ?product ?label
WHERE {
	?product rdfs:label ?label .
    ?product rdf:type bsbm:Product .
	FILTER regex(?label, "manliest")
}


```

## Goal results
```
bsbm-inst:Product67	"manliest polyethylene cullied"
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
  File "/rdflib_r2r/r2r_store.py", line 897, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 1004, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 827, in queryFilter
    clause = self.queryExpr(conn, part.expr, var_cf).expr()
  File "/rdflib_r2r/r2r_store.py", line 804, in queryExpr
    raise SparqlNotImplementedError(e)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_REGEX' Builtin_REGEX_Builtin_REGEX_{'text': rdflib.term.Variable('label'), 'pattern': rdflib.term.Literal('manliest'), '_vars': {rdflib.term.Variable('label')}}

```