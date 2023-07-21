# R2RMLTC0002d
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0002d)
Two columns mapping, generation of a BlankNode subject by using a SQL Query that concatenates two columns

## Created SQL query
```sql
SELECT '<http://xmlns.com/foaf/0.1/name>' AS p,
       CAST('_:' AS VARCHAR) || CAST(anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".StudentId AS VARCHAR) AS s,
       anon_1."View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name" AS o
FROM
  (SELECT "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR".StudentId,
          "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR"."Name"
   FROM
     (SELECT ('Student' || "ID") AS StudentId ,
             "ID" ,
             "Name"
      FROM "Student") AS "View_NB2HI4B2F4XWK6DBNVYGYZJOMNXW2L3CMFZWKL2UOJUXA3DFONGWC4BR") AS anon_1
```

## Raw ouput triples
```
_:Student10 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

## Triple Diff
```diff
_:cb0 <http://xmlns.com/foaf/0.1/name> "Venus" .
```

SUCCES