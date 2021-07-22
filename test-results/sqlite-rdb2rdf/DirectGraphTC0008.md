
# [DirectGraphTC0008](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0008)
Generation of direct graph from a table with composite primary key

```diff
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Name> "Venus Williams" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://example.com/base/Student#Sport> "Tennis" .
<http://example.com/base/Student/ID=10;Name=Venus%20Williams> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

SUCCES

(also checking pattern queries afterwards: True)
