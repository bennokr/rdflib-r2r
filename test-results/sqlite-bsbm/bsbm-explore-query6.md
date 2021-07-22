# bsbm-explore-query6
[bsbm-explore-query6](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ6)

## Random parameter sample
```
word1 = ie
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
	FILTER regex(?label, "ie")
}


```

## Goal results
```
bsbm-inst:Product25	"boundaries proselyted"
bsbm-inst:Product77	"mistaker impieties homeliest"
bsbm-inst:Product20	"caribous clients"
bsbm-inst:Product4	"feistiest horst keepsake"
bsbm-inst:Product88	"ghostiest anoraks mousses"
bsbm-inst:Product50	"cavie misleader"
bsbm-inst:Product67	"manliest polyethylene cullied"
bsbm-inst:Product6	"whistling usurers carried"
bsbm-inst:Product63	"defused botanies"
bsbm-inst:Product7	"pillions covenanting economies"
bsbm-inst:Product47	"swang sissies"
bsbm-inst:Product23	"crosier expwy snagged"
bsbm-inst:Product43	"manometries killjoys"
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
  File "/rdflib_r2r/r2r_store.py", line 878, in queryProject
    part_query, var_subform = self.queryPart(conn, part.p)
  File "/rdflib_r2r/r2r_store.py", line 962, in queryPart
    return self.queryFilter(conn, part)
  File "/rdflib_r2r/r2r_store.py", line 806, in queryFilter
    clause = self.queryExpr(conn, part.expr, var_cf).expr()
  File "/rdflib_r2r/r2r_store.py", line 783, in queryExpr
    raise SparqlNotImplementedError(e)
rdflib_r2r.r2r_store.SparqlNotImplementedError: Expr not implemented: 'Builtin_REGEX' Builtin_REGEX_Builtin_REGEX_{'text': rdflib.term.Variable('label'), 'pattern': rdflib.term.Literal('ie'), '_vars': {rdflib.term.Variable('label')}}

```