# R2RMLTC0016e
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0016e)
Table with datatypes, binary column

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://example.com/photo>' AS p,
          CAST('<' AS VARCHAR) || CAST('data:image/png;hex,' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST(hex("Patient"."Photo") AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS o,
          NULL AS g
   FROM "Patient"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('http://example.com/Patient' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Patient"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://xmlns.com/foaf/0.1/Person>' AS o,
                    NULL AS g
   FROM "Patient") AS anon_1
```

## Raw ouput triples
```
<http://example.com/Patient10> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFEBFC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient11> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFF3FC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient12> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFEBFC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

## Triple Diff
```diff
<http://example.com/Patient10> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFEBFC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient10> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient11> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFF3FC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient11> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.com/Patient12> <http://example.com/photo> <data:image/png;hex,89504E470D0A1A0A0000000D49484452000000050000000508060000008D6F26E50000001C4944415408D763F9FFFEBFC37F062005C3201284D031F18258CD04000EF535CBD18E0E1F0000000049454E44AE426082> .
<http://example.com/Patient12> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
```

SUCCES