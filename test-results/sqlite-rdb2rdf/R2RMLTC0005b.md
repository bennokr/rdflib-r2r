# R2RMLTC0005b
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0005b)
Default mapping

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT CAST('_:' AS VARCHAR) || CAST("IOUs".fname AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs".lname AS VARCHAR) AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/IOUs>' AS o,
          NULL AS g
   FROM "IOUs"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("IOUs".fname AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs".lname AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#lname>' AS p,
                    "IOUs".lname AS o,
                    NULL AS g
   FROM "IOUs"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("IOUs".fname AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs".lname AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#amount>' AS p,
                    "IOUs".amount AS o,
                    NULL AS g
   FROM "IOUs"
   UNION ALL SELECT CAST('_:' AS VARCHAR) || CAST("IOUs".fname AS VARCHAR) || CAST('_' AS VARCHAR) || CAST("IOUs".lname AS VARCHAR) AS s,
                    '<http://example.com/base/IOUs#fname>' AS p,
                    "IOUs".fname AS o,
                    NULL AS g
   FROM "IOUs") AS anon_1
```

## Triple Diff
```diff
_:cb0 <http://example.com/base/IOUs#amount> "30.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cb0 <http://example.com/base/IOUs#fname> "Bob" .
_:cb0 <http://example.com/base/IOUs#lname> "Smith" .
_:cb0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#amount> "20.0"^^<http://www.w3.org/2001/XMLSchema#double> .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#fname> "Sue" .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://example.com/base/IOUs#lname> "Jones" .
_:cbd4044ba4dd2d83cac23a0bf151b400a89968b26444a5096b22aac2b8541d1739 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/IOUs> .
```

SUCCES