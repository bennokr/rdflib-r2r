# bsbm-explore-query6
[link]([bsbm-explore-query6](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ6))

## Random parameter sample
```
word1 = fen
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
	FILTER regex(?label, "fen")
}


```

## Goal results
```
bsbm-inst:Product95	"edgers defensiveness"
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
  File "/rdflib_r2r/r2r_store.py", line 882, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 966, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 810, in queryFilter
    clause = self.queryExpr(conn, part.expr, var_cf).expr()
  File "/rdflib_r2r/r2r_store.py", line 787, in queryExpr
    raise SparqlNotImplementedError(e)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_REGEX' Builtin_REGEX_Builtin_REGEX_{'text': rdflib.term.Variable('label'), 'pattern': rdflib.term.Literal('fen'), '_vars': {rdflib.term.Variable('label')}}

```