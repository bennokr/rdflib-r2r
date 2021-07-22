# DirectGraphTC0025
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0025)
Generation of triples from three tables, three primary keys, three foreign keys

```diff
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#ID> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#city> "Cambridge" .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#state> "MA" .
<http://example.com/base/Addresses/ID=18> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Addresses> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ID> "23"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#city> "Cambridge" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#manager> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#name> "accounting" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ref-manager> <http://example.com/base/People/ID=8> .
<http://example.com/base/Department/ID=23> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Department> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ID> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#addr> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptCity> "Cambridge" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptName> "accounting" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#fname> "Bob" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-addr> <http://example.com/base/Addresses/ID=18> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/People/ID=7> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#ID> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#fname> "Sue" .
<http://example.com/base/People/ID=8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptCity> "Cambridge" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptName> "accounting" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#project> "pencil survey" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-project;deptName;deptCity> _:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-worker> <http://example.com/base/People/ID=7> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#worker> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/TaskAssignments> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#deptCity> "Cambridge" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#deptName> "accounting" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#name> "pencil survey" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#deptCity> "Cambridge" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#deptName> "accounting" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#name> "eraser survey" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
```

SUCCES