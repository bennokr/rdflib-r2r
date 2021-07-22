# bsbm-explore-query9
[link]([bsbm-explore-query9](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/#queryTripleQ9))


```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 181, in test_bsbm
    params = get_params(querytemplate)
  File "/tests/test_bsbm.py", line 160, in get_params
    params[pname] = sample_param(pname)
  File "/tests/test_bsbm.py", line 166, in sample_param
    domain = param_sets.get(tname) or param_sets[alt]
KeyError: 'ReviewXYZ'

```