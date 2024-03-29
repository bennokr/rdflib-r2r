# R2RMLTC0011b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0011b)
M to M relation, by using an additional Triples Map

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<http://example.com/student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://example.com/firstName>' AS p,
          "Student"."FirstName" AS o,
          NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/student/' || replace(replace(replace(replace(replace(replace(CAST("Student"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/lastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '<http://example.com/sport/' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/id>' AS p,
                    "Sport"."ID" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '<http://example.com/sport/' || replace(replace(replace(replace(replace(replace(CAST("Sport"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/description>' AS p,
                    "Sport"."Description" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '<http://example.com/student/' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/plays>' AS p,
                    '<http://example.com/sport/' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Student_Sport") AS anon_1
```

## Raw ouput triples
```
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
<http://example.com/sport/110> <http://example.com/id> "110" .
<http://example.com/sport/111> <http://example.com/description> "Football" .
<http://example.com/sport/111> <http://example.com/id> "111" .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
<http://example.com/sport/112> <http://example.com/id> "112" .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://example.com/plays> <http://example.com/sport/110> .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/112> .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://example.com/plays> <http://example.com/sport/111> .
```

## Triple Diff
```diff
<http://example.com/sport/110> <http://example.com/description> "Tennis" .
+ <http://example.com/sport/110> <http://example.com/id> "110" .
- <http://example.com/sport/110> <http://example.com/id> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/sport/111> <http://example.com/description> "Football" .
+ <http://example.com/sport/111> <http://example.com/id> "111" .
- <http://example.com/sport/111> <http://example.com/id> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/sport/112> <http://example.com/description> "Formula1" .
+ <http://example.com/sport/112> <http://example.com/id> "112" .
- <http://example.com/sport/112> <http://example.com/id> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/student/10> <http://example.com/firstName> "Venus" .
<http://example.com/student/10> <http://example.com/lastName> "Williams" .
<http://example.com/student/10> <http://example.com/plays> <http://example.com/sport/110> .
<http://example.com/student/11> <http://example.com/firstName> "Fernando" .
<http://example.com/student/11> <http://example.com/lastName> "Alonso" .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/111> .
<http://example.com/student/11> <http://example.com/plays> <http://example.com/sport/112> .
<http://example.com/student/12> <http://example.com/firstName> "David" .
<http://example.com/student/12> <http://example.com/lastName> "Villa" .
<http://example.com/student/12> <http://example.com/plays> <http://example.com/sport/111> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```