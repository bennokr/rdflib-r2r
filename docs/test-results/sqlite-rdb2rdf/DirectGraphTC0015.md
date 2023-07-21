# DirectGraphTC0015
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0015)
Generation of direct graph from multi-column primary keys

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Country/Code=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Lan=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Lan" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Country>' AS o,
          NULL AS g
   FROM "Country"
   UNION ALL SELECT '<Country/Code=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Lan=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Lan" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Country#Code>' AS p,
                    "Country"."Code" AS o,
                    NULL AS g
   FROM "Country"
   UNION ALL SELECT '<Country/Code=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Lan=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Lan" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Country#Lan>' AS p,
                    "Country"."Lan" AS o,
                    NULL AS g
   FROM "Country"
   UNION ALL SELECT '<Country/Code=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';Lan=' || replace(replace(replace(replace(replace(replace(CAST("Country"."Lan" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Country#Name>' AS p,
                    "Country"."Name" AS o,
                    NULL AS g
   FROM "Country") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Code> "BO" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Lan> "EN" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Name> "Bolivia, Plurinational State of" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Code> "BO" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Lan> "ES" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Name> "Estado Plurinacional de Bolivia" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Code> "IE" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Lan> "EN" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Name> "Ireland" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Code> "IE" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Lan> "ES" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Name> "Irlanda" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
```

## Triple Diff
```diff
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Code> "BO" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Lan> "EN" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://example.com/base/Country#Name> "Bolivia, Plurinational State of" .
<http://example.com/base/Country/Code=BO;Lan=EN> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Code> "BO" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Lan> "ES" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://example.com/base/Country#Name> "Estado Plurinacional de Bolivia" .
<http://example.com/base/Country/Code=BO;Lan=ES> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Code> "IE" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Lan> "EN" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://example.com/base/Country#Name> "Ireland" .
<http://example.com/base/Country/Code=IE;Lan=EN> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Code> "IE" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Lan> "ES" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://example.com/base/Country#Name> "Irlanda" .
<http://example.com/base/Country/Code=IE;Lan=ES> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country> .
```

SUCCES