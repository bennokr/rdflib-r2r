
# [DirectGraphTC0005](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0005)
Generation of BlankNodes from duplicate tuples

```diff
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#fname> "Bob" .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#lname> "Smith" .
_:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#fname> "Sue" .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#lname> "Jones" .
_:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#fname> "Bob" .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#lname> "Smith" .
_:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```

SUCCES

(also checking pattern queries afterwards: True)
