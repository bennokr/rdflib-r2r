# R2RMLTC0006a
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#R2RMLTC0006a)
Long form of R2RML by using rr:constant in rr:subjectMap, rr:predicateMap, rr:objectMap and rr:graphMap

## Created SQL query
```sql
SELECT '<http://example.com/description>' AS p,
       '<http://example.com/BadStudent>' AS s,
       '"Bad Student"' AS o
```

## Raw ouput triples
```
<http://example.com/BadStudent> <http://example.com/description> "Bad Student" .
```

## Triple Diff
```diff
<http://example.com/BadStudent> <http://example.com/description> "Bad Student" .
```

SUCCES