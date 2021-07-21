
# DirectGraphTC0012
Generation of direct graph from a database without primary keys

```diff
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#city> "London" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#fname> "Bob" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://example.com/base/Lives#lname> "Smith" .
_:cb1ea6538b6947f2054d9b36af8eee38fc9ab090ecc5f839eafa6d92df70fe61eb5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
- _:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#fname> "Bob" .
- _:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://example.com/base/IOUs#lname> "Smith" .
- _:cb21650a665ae41f6fa71adf668f84a44c399c8239fc0d008f357bb7a98e81dd0ec <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
+ _:cb2352e468f365818450dfb28ce4f6067332479ee184c82a1f84c1dd8203b93c7bf <http://example.com/base/IOUs#amount> "20.0" .
+ _:cb2352e468f365818450dfb28ce4f6067332479ee184c82a1f84c1dd8203b93c7bf <http://example.com/base/IOUs#fname> "Sue" .
+ _:cb2352e468f365818450dfb28ce4f6067332479ee184c82a1f84c1dd8203b93c7bf <http://example.com/base/IOUs#lname> "Jones" .
+ _:cb2352e468f365818450dfb28ce4f6067332479ee184c82a1f84c1dd8203b93c7bf <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
+ _:cb263251d239558de66032b72bd0676bfde4587f36266780e74bf76f340384dad7d <http://example.com/base/IOUs#amount> "30.0" .
+ _:cb263251d239558de66032b72bd0676bfde4587f36266780e74bf76f340384dad7d <http://example.com/base/IOUs#fname> "Bob" .
+ _:cb263251d239558de66032b72bd0676bfde4587f36266780e74bf76f340384dad7d <http://example.com/base/IOUs#lname> "Smith" .
+ _:cb263251d239558de66032b72bd0676bfde4587f36266780e74bf76f340384dad7d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
- _:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#fname> "Sue" .
- _:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://example.com/base/IOUs#lname> "Jones" .
- _:cb2b3842541ae926e256b3ee60a3e094429888a49654426cea42741869d5f1ad26b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#city> "London" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#fname> "Bob" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://example.com/base/Lives#lname> "Smith" .
_:cb2bed896f0badd3743b9f2c46a7a7eecccaca516a51648be4081139465fbf9c9ea <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#city> "Madrid" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#fname> "Sue" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://example.com/base/Lives#lname> "Jones" .
_:cb2cffeb8bd27a701982510435dd1126324d28ba46d7b207317c50c3abbc1850a6b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Lives> .
- _:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
- _:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#fname> "Bob" .
- _:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://example.com/base/IOUs#lname> "Smith" .
- _:cb2eac4049fd4a00de951ed4fda83e5a1c69b642b787795288431f5e107d4317c21 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
+ _:cb337987b5dbbb6f554e36acc2e92121ce14723fb3b1d3d2e0599b159af246158b2 <http://example.com/base/IOUs#amount> "30.0" .
+ _:cb337987b5dbbb6f554e36acc2e92121ce14723fb3b1d3d2e0599b159af246158b2 <http://example.com/base/IOUs#fname> "Bob" .
+ _:cb337987b5dbbb6f554e36acc2e92121ce14723fb3b1d3d2e0599b159af246158b2 <http://example.com/base/IOUs#lname> "Smith" .
+ _:cb337987b5dbbb6f554e36acc2e92121ce14723fb3b1d3d2e0599b159af246158b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```
