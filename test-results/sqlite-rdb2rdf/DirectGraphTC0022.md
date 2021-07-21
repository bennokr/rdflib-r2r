
# DirectGraphTC0022
Generation of triples from two tables, a primary key, a foreign key, references no primary keys

```diff
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A2" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A1" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> _:cb0 .
<http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
_:cb0 <http://example.com/base/Target#key1attr1> "K1A1" .
_:cb0 <http://example.com/base/Target#key1attr2> "K1A2" .
_:cb0 <http://example.com/base/Target#key2attr1> "K2A1" .
_:cb0 <http://example.com/base/Target#key2attr2> "K2A2" .
_:cb0 <http://example.com/base/Target#litattr1> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```
