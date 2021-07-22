# bsbm-explore-query9 
```
Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 179, in test_bsbm
    params = get_params(querytemplate)
  File "/tests/test_bsbm.py", line 158, in get_params
    params[pname] = sample_param(pname)
  File "/tests/test_bsbm.py", line 164, in sample_param
    domain = param_sets.get(tname) or param_sets[alt]
KeyError: 'ReviewXYZ'

```