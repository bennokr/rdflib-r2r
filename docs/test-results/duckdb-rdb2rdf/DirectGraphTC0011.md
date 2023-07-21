# DirectGraphTC0011
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0011)
Many to Many relations

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Student_Sport/ID_Student=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID_Sport=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student_Sport>' AS o,
          NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student_Sport/ID_Student=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID_Sport=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student_Sport#ID_Sport>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student_Sport"."ID_Sport" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student_Sport/ID_Student=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID_Sport=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student_Sport#ID_Student>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student_Sport"."ID_Student" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Sport>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#Description>' AS p,
                    "Sport"."Description" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Sport/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Sport"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Student>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#FirstName>' AS p,
                    "Student"."FirstName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Student/ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST(';ID=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Student#LastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Sport/ID=110;ID=110> <http://example.com/base/Sport#Description> "Tennis" .
<http://example.com/base/Sport/ID=110;ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=110;ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=111;ID=111> <http://example.com/base/Sport#Description> "Football" .
<http://example.com/base/Sport/ID=111;ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=111;ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Sport/ID=112;ID=112> <http://example.com/base/Sport#Description> "Formula1" .
<http://example.com/base/Sport/ID=112;ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Sport/ID=112;ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
<http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#FirstName> "Venus" .
<http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#LastName> "Williams" .
<http://example.com/base/Student/ID=10;ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
<http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#LastName> "Alonso" .
<http://example.com/base/Student/ID=11;ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#FirstName> "David" .
<http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#LastName> "Villa" .
<http://example.com/base/Student/ID=12;ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

## Triple Diff
```diff
+ <http://example.com/base/Sport/ID=110;ID=110> <http://example.com/base/Sport#Description> "Tennis" .
+ <http://example.com/base/Sport/ID=110;ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Sport/ID=110;ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#Description> "Tennis" .
- <http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
+ <http://example.com/base/Sport/ID=111;ID=111> <http://example.com/base/Sport#Description> "Football" .
+ <http://example.com/base/Sport/ID=111;ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Sport/ID=111;ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#Description> "Football" .
- <http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
+ <http://example.com/base/Sport/ID=112;ID=112> <http://example.com/base/Sport#Description> "Formula1" .
+ <http://example.com/base/Sport/ID=112;ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Sport/ID=112;ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#Description> "Formula1" .
- <http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
+ <http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#FirstName> "Venus" .
+ <http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Student/ID=10;ID=10> <http://example.com/base/Student#LastName> "Williams" .
+ <http://example.com/base/Student/ID=10;ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#FirstName> "Venus" .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#LastName> "Williams" .
- <http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ <http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
+ <http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Student/ID=11;ID=11> <http://example.com/base/Student#LastName> "Alonso" .
+ <http://example.com/base/Student/ID=11;ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#LastName> "Alonso" .
- <http://example.com/base/Student/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ <http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#FirstName> "David" .
+ <http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ <http://example.com/base/Student/ID=12;ID=12> <http://example.com/base/Student#LastName> "Villa" .
+ <http://example.com/base/Student/ID=12;ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#FirstName> "David" .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#LastName> "Villa" .
- <http://example.com/base/Student/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=110> .
- <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=10> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=112> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
- <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=12> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 174, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```