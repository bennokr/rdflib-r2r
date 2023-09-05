# DirectGraphTC0011
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0011)
Many to Many relations

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Student_Sport>' AS o,
          NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ID_Sport>' AS p,
                    '"' || CAST(CAST("Student_Sport"."ID_Sport" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ref-ID_Student>' AS p,
                    '_:Student#' || CAST(CAST("Student_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student_Sport",
        "Student" AS "Student_ref"
   WHERE "Student_Sport"."ID_Student" = "Student_ref"."ID"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ID_Student>' AS p,
                    '"' || CAST(CAST("Student_Sport"."ID_Student" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student_Sport"
   UNION ALL SELECT '<Student_Sport/ID_Student=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Student" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';ID_Sport=' || replace(replace(replace(replace(replace(replace(CAST("Student_Sport"."ID_Sport" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Student_Sport#ref-ID_Sport>' AS p,
                    '_:Sport#' || CAST(CAST("Sport_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "Student_Sport",
        "Sport" AS "Sport_ref"
   WHERE "Student_Sport"."ID_Sport" = "Sport_ref"."ID"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Sport>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#ID>' AS p,
                    '"' || CAST(CAST("Sport"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '_:Sport#' || CAST(CAST("Sport".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Sport#Description>' AS p,
                    "Sport"."Description" AS o,
                    NULL AS g
   FROM "Sport"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Student>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#LastName>' AS p,
                    "Student"."LastName" AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#ID>' AS p,
                    '"' || CAST(CAST("Student"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Student"
   UNION ALL SELECT '_:Student#' || CAST(CAST("Student".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Student#FirstName>' AS p,
                    "Student"."FirstName" AS o,
                    NULL AS g
   FROM "Student") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> _:Sport#0 .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> _:Student#0 .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> _:Sport#1 .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> _:Student#1 .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> _:Sport#2 .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> _:Student#1 .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> _:Sport#1 .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> _:Student#2 .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
_:Sport#0 <http://example.com/base/Sport#Description> "Tennis" .
_:Sport#0 <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Sport#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
_:Sport#1 <http://example.com/base/Sport#Description> "Football" .
_:Sport#1 <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Sport#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
_:Sport#2 <http://example.com/base/Sport#Description> "Formula1" .
_:Sport#2 <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Sport#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
_:Student#0 <http://example.com/base/Student#FirstName> "Venus" .
_:Student#0 <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#0 <http://example.com/base/Student#LastName> "Williams" .
_:Student#0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:Student#1 <http://example.com/base/Student#FirstName> "Fernando" .
_:Student#1 <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#1 <http://example.com/base/Student#LastName> "Alonso" .
_:Student#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
_:Student#2 <http://example.com/base/Student#FirstName> "David" .
_:Student#2 <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Student#2 <http://example.com/base/Student#LastName> "Villa" .
_:Student#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
```

## Triple Diff
```diff
- <http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#Description> "Tennis" .
- <http://example.com/base/Sport/ID=110> <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#Description> "Football" .
- <http://example.com/base/Sport/ID=111> <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#Description> "Formula1" .
- <http://example.com/base/Sport/ID=112> <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Sport/ID=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#FirstName> "Venus" .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=10> <http://example.com/base/Student#LastName> "Williams" .
- <http://example.com/base/Student/ID=10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#FirstName> "Fernando" .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=11> <http://example.com/base/Student#LastName> "Alonso" .
- <http://example.com/base/Student/ID=11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#FirstName> "David" .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student/ID=12> <http://example.com/base/Student#LastName> "Villa" .
- <http://example.com/base/Student/ID=12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Sport> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ID_Student> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=110> .
+ <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Sport> _:cb6e1aa4c97a9b10b6b827c6a840a138009e3231113cc3aaf61f93fbda7a6abcd6 .
- <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=10> .
+ <http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://example.com/base/Student_Sport#ref-ID_Student> _:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb .
<http://example.com/base/Student_Sport/ID_Student=10;ID_Sport=110> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
+ <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> _:cb557c33a7da17af984a4839a93851ccdf4d15edbb98acd27977f648d699ac020 .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
+ <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Sport> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ID_Student> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=112> .
+ <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Sport> _:cb7b38033ef073fa88b1feafd875ee56b34ebff619b3960bef747e34b863cbf0c3 .
- <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=11> .
+ <http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://example.com/base/Student_Sport#ref-ID_Student> _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd .
<http://example.com/base/Student_Sport/ID_Student=11;ID_Sport=112> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Sport> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ID_Student> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
- <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> <http://example.com/base/Sport/ID=111> .
+ <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Sport> _:cb557c33a7da17af984a4839a93851ccdf4d15edbb98acd27977f648d699ac020 .
- <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> <http://example.com/base/Student/ID=12> .
+ <http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://example.com/base/Student_Sport#ref-ID_Student> _:cb0 .
<http://example.com/base/Student_Sport/ID_Student=12;ID_Sport=111> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student_Sport> .
+ _:cb0 <http://example.com/base/Student#FirstName> "David" .
+ _:cb0 <http://example.com/base/Student#ID> "12"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb0 <http://example.com/base/Student#LastName> "Villa" .
+ _:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://example.com/base/Student#FirstName> "Venus" .
+ _:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://example.com/base/Student#ID> "10"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://example.com/base/Student#LastName> "Williams" .
+ _:cb3f08ac56775877df5f632d4deef2d02b706557970c1e99ffa8a55661bb642ecb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd <http://example.com/base/Student#FirstName> "Fernando" .
+ _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd <http://example.com/base/Student#ID> "11"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd <http://example.com/base/Student#LastName> "Alonso" .
+ _:cb507694a67037aab92d1975098d507a125a10a527a190f6024b1ae22ab3d2cd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Student> .
+ _:cb557c33a7da17af984a4839a93851ccdf4d15edbb98acd27977f648d699ac020 <http://example.com/base/Sport#Description> "Football" .
+ _:cb557c33a7da17af984a4839a93851ccdf4d15edbb98acd27977f648d699ac020 <http://example.com/base/Sport#ID> "111"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb557c33a7da17af984a4839a93851ccdf4d15edbb98acd27977f648d699ac020 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
+ _:cb6e1aa4c97a9b10b6b827c6a840a138009e3231113cc3aaf61f93fbda7a6abcd6 <http://example.com/base/Sport#Description> "Tennis" .
+ _:cb6e1aa4c97a9b10b6b827c6a840a138009e3231113cc3aaf61f93fbda7a6abcd6 <http://example.com/base/Sport#ID> "110"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb6e1aa4c97a9b10b6b827c6a840a138009e3231113cc3aaf61f93fbda7a6abcd6 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
+ _:cb7b38033ef073fa88b1feafd875ee56b34ebff619b3960bef747e34b863cbf0c3 <http://example.com/base/Sport#Description> "Formula1" .
+ _:cb7b38033ef073fa88b1feafd875ee56b34ebff619b3960bef747e34b863cbf0c3 <http://example.com/base/Sport#ID> "112"^^<http://www.w3.org/2001/XMLSchema#integer> .
+ _:cb7b38033ef073fa88b1feafd875ee56b34ebff619b3960bef747e34b863cbf0c3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Sport> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 183, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get more diff

```