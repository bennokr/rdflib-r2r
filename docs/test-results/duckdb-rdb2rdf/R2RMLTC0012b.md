# R2RMLTC0012b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0012b)
Duplicate tuples generate same blank node

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '_:' || CAST("IOUs"."fname" AS VARCHAR) || '_' || CAST("IOUs"."lname" AS VARCHAR) AS s,
          '<http://xmlns.com/foaf/0.1/name>' AS p,
          CAST("IOUs"."fname" AS VARCHAR) || ' ' || CAST("IOUs"."lname" AS VARCHAR) AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT '_:' || CAST("Lives"."fname" AS VARCHAR) || '_' || CAST("Lives"."lname" AS VARCHAR) AS s,
                    '<http://example.com/city>' AS p,
                    "Lives"."city" AS o,
                    NULL AS g
   FROM "Lives") AS anon_1
```

## Raw ouput triples
```
_:Bob_Smith <http://example.com/city> "London" .
_:Bob_Smith <http://example.com/city> "London" .
_:Bob_Smith <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Bob_Smith <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
_:Sue_Jones <http://example.com/city> "Madrid" .
_:Sue_Jones <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
```

## Triple Diff
```diff
_:cb0 <http://example.com/city> "Madrid" .
_:cb0 <http://xmlns.com/foaf/0.1/name> "Sue Jones" .
_:cb73b70e4b2d26b1f7c8474f47e210a488b7d883818a502afd8c76cc8b1facee20 <http://example.com/city> "London" .
_:cb73b70e4b2d26b1f7c8474f47e210a488b7d883818a502afd8c76cc8b1facee20 <http://xmlns.com/foaf/0.1/name> "Bob Smith" .
```

SUCCES