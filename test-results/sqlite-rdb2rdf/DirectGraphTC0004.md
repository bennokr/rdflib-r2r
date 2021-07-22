
# [DirectGraphTC0004](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0004)
Two column mapping, generation of a BlankNode subject

```diff
_:cb0 <http://example.com/base/Student_Sport#Sport> "Tennis" .
_:cb0 <http://example.com/base/Student_Sport#Student> "Venus" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

SUCCES

(also checking pattern queries afterwards: True)
