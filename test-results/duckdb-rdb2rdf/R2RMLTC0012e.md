# R2RMLTC0012e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012e)
Default mapping

```diff
_:cb0 <http://example.com/base/IOUs#city> "Madrid" .
_:cb0 <http://example.com/base/IOUs#fname> "Sue" .
_:cb0 <http://example.com/base/IOUs#lname> "Jones" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
+ _:cb149a844af41e864f12d3fd7648b7ddb8065710f6015600538f4a7292d5f870e83 <http://example.com/base/IOUs#amount> "30.0" .
+ _:cb149a844af41e864f12d3fd7648b7ddb8065710f6015600538f4a7292d5f870e83 <http://example.com/base/IOUs#fname> "Bob" .
+ _:cb149a844af41e864f12d3fd7648b7ddb8065710f6015600538f4a7292d5f870e83 <http://example.com/base/IOUs#lname> "Smith" .
+ _:cb149a844af41e864f12d3fd7648b7ddb8065710f6015600538f4a7292d5f870e83 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#amount> "20.0" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#fname> "Sue" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://example.com/base/IOUs#lname> "Jones" .
+ _:cb55ae6cf264f32dea64f64eb5630b23b2355857174d00dcbf4787143b30960c8d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#fname> "Sue" .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#lname> "Jones" .
- _:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#city> "London" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#fname> "Bob" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://example.com/base/IOUs#lname> "Smith" .
_:cbd8f7ce9a2deccf7c61af1974929a41f8165a89580a01238c423337a9b4b7bab7 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
- _:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#fname> "Bob" .
- _:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://example.com/base/IOUs#lname> "Smith" .
- _:cbfcd3cdf15ad17d859bc25b107d516065b9b13f9d6fb7ffb78cebb0860f5731f2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```

FAIL
```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 160, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get the full diff

```