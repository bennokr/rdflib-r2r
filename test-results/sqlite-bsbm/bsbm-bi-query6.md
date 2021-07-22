# bsbm-bi-query6
[bsbm-bi-query6](http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BusinessIntelligenceUseCase/index.html#queryTripleQ6)

## Random parameter sample
```
Producer = <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3>
```

## SPARQL query
```sparql
  prefix bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
  prefix bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
  prefix rev: <http://purl.org/stuff/rev#>
  prefix xsd: <http://www.w3.org/2001/XMLSchema#>

  Select ?reviewer (avg(xsd:float(?score)) As ?reviewerAvgScore)
  {
    { Select (avg(xsd:float(?score)) As ?avgScore)
      {
        ?product bsbm:producer <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3> .
        ?review bsbm:reviewFor ?product .
        { ?review bsbm:rating1 ?score . } UNION
        { ?review bsbm:rating2 ?score . } UNION
        { ?review bsbm:rating3 ?score . } UNION
        { ?review bsbm:rating4 ?score . }
      }
    }
    ?product bsbm:producer <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer3> .
    ?review bsbm:reviewFor ?product .
    ?review rev:reviewer ?reviewer .
    { ?review bsbm:rating1 ?score . } UNION
    { ?review bsbm:rating2 ?score . } UNION
    { ?review bsbm:rating3 ?score . } UNION
    { ?review bsbm:rating4 ?score . }
  }
  Group By ?reviewer
  Having (avg(xsd:float(?score)) > min(?avgScore) * 1.5)

```

## Goal results
```
bsbm-inst:Reviewer40	"9.0"^^xsd:double
```

## Created SQL query
```sql
SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr_1 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS reviewer,
       avg(CAST(anon_2.score AS FLOAT)) AS "reviewerAvgScore"
FROM
  (SELECT anon_3.avg_1 AS avg_1,
          anon_4.nr AS nr,
          anon_4.nr_2 AS nr_2,
          anon_4.nr_1 AS nr_1
   FROM
     (SELECT avg(CAST(anon_5.score AS FLOAT)) AS avg_1
      FROM
        (SELECT anon_6.review AS review,
                anon_6.score AS score
         FROM
           (SELECT anon_7.review AS review,
                   anon_7.score AS score
            FROM
              (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_8.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                      anon_8.rating1 AS score
               FROM
                 (SELECT anon_9.nr AS nr,
                         anon_9.rating1 AS rating1
                  FROM
                    (SELECT review.nr AS nr,
                            review.rating1 AS rating1
                     FROM review) AS anon_9) AS anon_8
               UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_10.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                                anon_10.rating2 AS score
               FROM
                 (SELECT anon_11.nr AS nr,
                         anon_11.rating2 AS rating2
                  FROM
                    (SELECT review.nr AS nr,
                            review.rating2 AS rating2
                     FROM review) AS anon_11) AS anon_10) AS anon_7
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_12.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                             anon_12.rating3 AS score
            FROM
              (SELECT anon_13.nr AS nr,
                      anon_13.rating3 AS rating3
               FROM
                 (SELECT review.nr AS nr,
                         review.rating3 AS rating3
                  FROM review) AS anon_13) AS anon_12) AS anon_6
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_14.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                          anon_14.rating4 AS score
         FROM
           (SELECT anon_15.nr AS nr,
                   anon_15.rating4 AS rating4
            FROM
              (SELECT review.nr AS nr,
                      review.rating4 AS rating4
               FROM review) AS anon_15) AS anon_14) AS anon_5,

        (SELECT anon_17.nr AS nr,
                anon_17.nr_3 AS nr_3
         FROM
           (SELECT review.nr AS nr,
                   product.nr AS nr_3
            FROM review,
                 product
            WHERE "review".product = "product".nr) AS anon_17,

           (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                   '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                   '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                   NULL AS g
            FROM product,
                 producer
            WHERE "nr" = '3'
              AND "product".producer = "producer".nr
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                             NULL AS g
            FROM offer,
                 producer
            WHERE "nr" = '3'
              AND "offer".producer = "producer".nr
            UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                             '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                             '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                             NULL AS g
            FROM review,
                 producer
            WHERE "nr" = '3'
              AND "review".producer = "producer".nr) AS anon_18
         WHERE '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_17.nr_3 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_18.s) AS anon_16
      WHERE '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_16.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_5.review) AS anon_3,

     (SELECT anon_19.nr AS nr,
             anon_19.nr_2 AS nr_2,
             anon_20.nr_1 AS nr_1
      FROM
        (SELECT review.nr AS nr,
                product.nr AS nr_2
         FROM review,
              product
         WHERE "review".product = "product".nr) AS anon_19,

        (SELECT review.nr AS nr,
                person.nr AS nr_1
         FROM review,
              person
         WHERE "review".person = "person".nr) AS anon_20,

        (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                NULL AS g
         FROM product,
              producer
         WHERE "nr" = '3'
           AND "product".producer = "producer".nr
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer' || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                          '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM offer,
              producer
         WHERE "nr" = '3'
           AND "offer".producer = "producer".nr
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                          '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p,
                          '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer' || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                          NULL AS g
         FROM review,
              producer
         WHERE "nr" = '3'
           AND "review".producer = "producer".nr) AS anon_21
      WHERE anon_19.nr = anon_20.nr
        AND '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product' || replace(replace(replace(replace(replace(replace(CAST(anon_19.nr_2 AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_21.s) AS anon_4) AS anon_1,

  (SELECT anon_22.review AS review,
          anon_22.score AS score
   FROM
     (SELECT anon_23.review AS review,
             anon_23.score AS score
      FROM
        (SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_24.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                anon_24.rating1 AS score
         FROM
           (SELECT anon_25.nr AS nr,
                   anon_25.rating1 AS rating1
            FROM
              (SELECT review.nr AS nr,
                      review.rating1 AS rating1
               FROM review) AS anon_25) AS anon_24
         UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_26.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                          anon_26.rating2 AS score
         FROM
           (SELECT anon_27.nr AS nr,
                   anon_27.rating2 AS rating2
            FROM
              (SELECT review.nr AS nr,
                      review.rating2 AS rating2
               FROM review) AS anon_27) AS anon_26) AS anon_23
      UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_28.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                       anon_28.rating3 AS score
      FROM
        (SELECT anon_29.nr AS nr,
                anon_29.rating3 AS rating3
         FROM
           (SELECT review.nr AS nr,
                   review.rating3 AS rating3
            FROM review) AS anon_29) AS anon_28) AS anon_22
   UNION ALL SELECT '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_30.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS review,
                    anon_30.rating4 AS score
   FROM
     (SELECT anon_31.nr AS nr,
             anon_31.rating4 AS rating4
      FROM
        (SELECT review.nr AS nr,
                review.rating4 AS rating4
         FROM review) AS anon_31) AS anon_30) AS anon_2
WHERE '<' || 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review' || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' = anon_2.review
GROUP BY anon_1.nr_1
HAVING avg(CAST(anon_2.score AS FLOAT)) > (min(anon_1.avg_1) * 1.5)
```


```
Traceback (most recent call last):
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: ambiguous column name: nr

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tests/test_bsbm.py", line 215, in test_bsbm
    made = tuple(graph_rdb.query(query))
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/query.py", line 254, in __len__
    return len(self.bindings)
  File "/opt/miniconda3/lib/python3.8/site-packages/rdflib/query.py", line 185, in _get_bindings
    self._bindings += list(self._genbindings)
  File "/rdflib_r2r/sparql_op.py", line 21, in freeze_bindings
    for bindings in res:
  File "/rdflib_r2r/r2r_store.py", line 1002, in exec
    results = conn.execute(query)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/future/engine.py", line 280, in execute
    return self._execute_20(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1582, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/sql/elements.py", line 324, in _execute_on_connection
    return connection._execute_clauseelement(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1451, in _execute_clauseelement
    ret = self._execute_context(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1813, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1994, in _handle_dbapi_exception
    util.raise_(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/util/compat.py", line 207, in raise_
    raise exception
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/base.py", line 1770, in _execute_context
    self.dialect.do_execute(
  File "/opt/miniconda3/lib/python3.8/site-packages/sqlalchemy/engine/default.py", line 717, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) ambiguous column name: nr
[SQL: SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr_1 AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS reviewer, avg(CAST(anon_2.score AS FLOAT)) AS "reviewerAvgScore" 
FROM (SELECT anon_3.avg_1 AS avg_1, anon_4.nr AS nr, anon_4.nr_2 AS nr_2, anon_4.nr_1 AS nr_1 
FROM (SELECT avg(CAST(anon_5.score AS FLOAT)) AS avg_1 
FROM (SELECT anon_6.review AS review, anon_6.score AS score 
FROM (SELECT anon_7.review AS review, anon_7.score AS score 
FROM (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_8.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_8.rating1 AS score 
FROM (SELECT anon_9.nr AS nr, anon_9.rating1 AS rating1 
FROM (SELECT review.nr AS nr, review.rating1 AS rating1 
FROM review) AS anon_9) AS anon_8 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_10.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_10.rating2 AS score 
FROM (SELECT anon_11.nr AS nr, anon_11.rating2 AS rating2 
FROM (SELECT review.nr AS nr, review.rating2 AS rating2 
FROM review) AS anon_11) AS anon_10) AS anon_7 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_12.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_12.rating3 AS score 
FROM (SELECT anon_13.nr AS nr, anon_13.rating3 AS rating3 
FROM (SELECT review.nr AS nr, review.rating3 AS rating3 
FROM review) AS anon_13) AS anon_12) AS anon_6 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_14.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_14.rating4 AS score 
FROM (SELECT anon_15.nr AS nr, anon_15.rating4 AS rating4 
FROM (SELECT review.nr AS nr, review.rating4 AS rating4 
FROM review) AS anon_15) AS anon_14) AS anon_5, (SELECT anon_17.nr AS nr, anon_17.nr_3 AS nr_3 
FROM (SELECT review.nr AS nr, product.nr AS nr_3 
FROM review, product 
WHERE "review".product = "product".nr) AS anon_17, (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM product, producer 
WHERE "nr" = ? AND "product".producer = "producer".nr UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM offer, producer 
WHERE "nr" = ? AND "offer".producer = "producer".nr UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM review, producer 
WHERE "nr" = ? AND "review".producer = "producer".nr) AS anon_18 
WHERE ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_17.nr_3 AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = anon_18.s) AS anon_16 
WHERE ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_16.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = anon_5.review) AS anon_3, (SELECT anon_19.nr AS nr, anon_19.nr_2 AS nr_2, anon_20.nr_1 AS nr_1 
FROM (SELECT review.nr AS nr, product.nr AS nr_2 
FROM review, product 
WHERE "review".product = "product".nr) AS anon_19, (SELECT review.nr AS nr, person.nr AS nr_1 
FROM review, person 
WHERE "review".person = "person".nr) AS anon_20, (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(product.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM product, producer 
WHERE "nr" = ? AND "product".producer = "producer".nr UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(offer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM offer, producer 
WHERE "nr" = ? AND "offer".producer = "producer".nr UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(review.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS s, '<http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/producer>' AS p, ? || ? || replace(replace(replace(replace(replace(replace(CAST(producer.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS o, NULL AS g 
FROM review, producer 
WHERE "nr" = ? AND "review".producer = "producer".nr) AS anon_21 
WHERE anon_19.nr = anon_20.nr AND ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_19.nr_2 AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = anon_21.s) AS anon_4) AS anon_1, (SELECT anon_22.review AS review, anon_22.score AS score 
FROM (SELECT anon_23.review AS review, anon_23.score AS score 
FROM (SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_24.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_24.rating1 AS score 
FROM (SELECT anon_25.nr AS nr, anon_25.rating1 AS rating1 
FROM (SELECT review.nr AS nr, review.rating1 AS rating1 
FROM review) AS anon_25) AS anon_24 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_26.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_26.rating2 AS score 
FROM (SELECT anon_27.nr AS nr, anon_27.rating2 AS rating2 
FROM (SELECT review.nr AS nr, review.rating2 AS rating2 
FROM review) AS anon_27) AS anon_26) AS anon_23 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_28.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_28.rating3 AS score 
FROM (SELECT anon_29.nr AS nr, anon_29.rating3 AS rating3 
FROM (SELECT review.nr AS nr, review.rating3 AS rating3 
FROM review) AS anon_29) AS anon_28) AS anon_22 UNION ALL SELECT ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_30.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? AS review, anon_30.rating4 AS score 
FROM (SELECT anon_31.nr AS nr, anon_31.rating4 AS rating4 
FROM (SELECT review.nr AS nr, review.rating4 AS rating4 
FROM review) AS anon_31) AS anon_30) AS anon_2 
WHERE ? || ? || replace(replace(replace(replace(replace(replace(CAST(anon_1.nr AS VARCHAR), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?), ?, ?) || ? = anon_2.review GROUP BY anon_1.nr_1 
HAVING avg(CAST(anon_2.score AS FLOAT)) > (min(anon_1.avg_1) * ?)]
[parameters: ('<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Reviewer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Offer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Producer', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '3', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Product', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', '<', 'http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/Review', ' ', '%20', '/', '%2F', '(', '%28', ')', '%29', ',', '%2C', ':', '%3A', '>', 1.5)]
(Background on this error at: http://sqlalche.me/e/14/e3q8)

```