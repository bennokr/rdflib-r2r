# R2RMLTC0016b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016b)
Table with datatypes: real and float

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://xmlns.com/foaf/0.1/Person>' AS o,
          NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/height>' AS p,
                    "Patient"."Height" AS o,
                    NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/weight>' AS p,
                    "Patient"."Weight" AS o,
                    NULL AS g
   FROM "Patient") AS anon_1
```

## Triple Diff
```diff
+ <http://example.com/Patient10> <http://example.com/height> "1.649999999999999911182158029987476766109466552734375"^^<http://www.w3.org/2001/XMLSchema#decimal> .
- <http://example.com/Patient10> <http://example.com/height> "1.65"^^<http://www.w3.org/2001/XMLSchema#double> .
+ <http://example.com/Patient10> <http://example.com/weight> "80.25"^^<http://www.w3.org/2001/XMLSchema#decimal> .
- <http://example.com/Patient10> <http://example.com/weight> "80.25"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
+ <http://example.com/Patient11> <http://example.com/height> "1.6999999999999999555910790149937383830547332763671875"^^<http://www.w3.org/2001/XMLSchema#decimal> .
- <http://example.com/Patient11> <http://example.com/height> "1.7"^^<http://www.w3.org/2001/XMLSchema#double> .
+ <http://example.com/Patient11> <http://example.com/weight> "70.219999999999998863131622783839702606201171875"^^<http://www.w3.org/2001/XMLSchema#decimal> .
- <http://example.com/Patient11> <http://example.com/weight> "70.22"^^<http://www.w3.org/2001/XMLSchema#double> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
- <http://example.com/Patient12> <http://example.com/height> "1.76"^^<http://www.w3.org/2001/XMLSchema#double> .
+ <http://example.com/Patient12> <http://example.com/height> "1.7600000000000000088817841970012523233890533447265625"^^<http://www.w3.org/2001/XMLSchema#decimal> .
- <http://example.com/Patient12> <http://example.com/weight> "90.31"^^<http://www.w3.org/2001/XMLSchema#double> .
+ <http://example.com/Patient12> <http://example.com/weight> "90.31000000000000227373675443232059478759765625"^^<http://www.w3.org/2001/XMLSchema#decimal> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

FAIL

```
Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 168, in test_rdb2rdf
    assert iso_made == iso_goal
AssertionError: assert <Graph identi...rphicGraph'>)> == <Graph identi...rphicGraph'>)>
  Use -v to get the full diff

```