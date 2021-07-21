
# DirectGraphTC0023
Generation of triples for two tables, two primary keys, two foreign keys, references to a key other than primary key

```diff
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ID> "1100"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrA> "K2A2" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#attrB> "K2A1" .
<http://example.com/base/Source/ID=1100> <http://example.com/base/Source#ref-attrA;attrB> <http://example.com/base/Target/PK=1010> .
<http://example.com/base/Source/ID=1100> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Source> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#PK> "1010"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr1> "K1A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key1attr2> "K1A2" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr1> "K2A1" .
<http://example.com/base/Target/PK=1010> <http://example.com/base/Target#key2attr2> "K2A2" .
<http://example.com/base/Target/PK=1010> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Target> .
```