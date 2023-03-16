# DirectGraphTC0010
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0010)
Generation of direct graph for table names with spaces

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Country%20Info>' AS o,
          NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Name>' AS p,
                    "Country Info"."Name" AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#ISO%203166>' AS p,
                    "Country Info"."ISO 3166" AS o,
                    NULL AS g
   FROM "Country Info"
   UNION ALL SELECT CAST('<' AS VARCHAR) || CAST('Country%20Info/Country%20Code=' AS VARCHAR) || replace(replace(replace(replace(replace(replace(CAST("Country Info"."Country Code" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || CAST('>' AS VARCHAR) AS s,
                    '<http://example.com/base/Country%20Info#Country%20Code>' AS p,
                    CAST('"' AS VARCHAR) || CAST(CAST("Country Info"."Country Code" AS VARCHAR) AS VARCHAR) || CAST('"^^<http://www.w3.org/2001/XMLSchema#integer>' AS VARCHAR) AS o,
                    NULL AS g
   FROM "Country Info") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#ISO%203166> "BO" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#ISO%203166> "IE" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Name> "Ireland" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#ISO%203166> "MF" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
```

## Triple Diff
```diff
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Country%20Code> "1"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#ISO%203166> "BO" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://example.com/base/Country%20Info#Name> "Bolivia, Plurinational State of" .
<http://example.com/base/Country%20Info/Country%20Code=1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Country%20Code> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#ISO%203166> "IE" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://example.com/base/Country%20Info#Name> "Ireland" .
<http://example.com/base/Country%20Info/Country%20Code=2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Country%20Code> "3"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#ISO%203166> "MF" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://example.com/base/Country%20Info#Name> "Saint Martin (French part)" .
<http://example.com/base/Country%20Info/Country%20Code=3> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Country%20Info> .
```

SUCCES