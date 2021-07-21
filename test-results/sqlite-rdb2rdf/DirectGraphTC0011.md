
# DirectGraphTC0011
Many to Many relations

```diff
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#Description> "Tennis" .
<http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#Description> "Football" .
<http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#Description> "Formula1" .
<http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#FirstName> "Venus" .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10> <http://example.com/base/Student#LastName> "Williams" .
<http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=11> <http://example.com/base/Student#LastName> "Alonso" .
<http://example.com/base/Student/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#FirstName> "David" .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=12> <http://example.com/base/Student#LastName> "Villa" .
<http://example.com/base/Student/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=110> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=10> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=112> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=12> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```