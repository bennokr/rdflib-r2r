# DirectGraphTC0025
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0025)
Generation of triples from three tables, three primary keys, three foreign keys

## Created SQL query
```sql
SELECT anon_1.s AS s,
       anon_1.p AS p,
       anon_1.o AS o
FROM
  (SELECT '<Addresses/ID=' || replace(replace(replace(replace(replace(replace(CAST("Addresses"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
          '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
          '<http://example.com/base/Addresses>' AS o,
          NULL AS g
   FROM "Addresses"
   UNION ALL SELECT '<Addresses/ID=' || replace(replace(replace(replace(replace(replace(CAST("Addresses"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Addresses#ID>' AS p,
                    '"' || CAST(CAST("Addresses"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Addresses"
   UNION ALL SELECT '<Addresses/ID=' || replace(replace(replace(replace(replace(replace(CAST("Addresses"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Addresses#state>' AS p,
                    substr("Addresses".state || '  ', 1, 2) AS o,
                    NULL AS g
   FROM "Addresses"
   UNION ALL SELECT '<Addresses/ID=' || replace(replace(replace(replace(replace(replace(CAST("Addresses"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Addresses#city>' AS p,
                    "Addresses".city AS o,
                    NULL AS g
   FROM "Addresses"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Department>' AS o,
                    NULL AS g
   FROM "Department"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Department#manager>' AS p,
                    '"' || CAST(CAST("Department".manager AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Department"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Department#ID>' AS p,
                    '"' || CAST(CAST("Department"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Department"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Department#city>' AS p,
                    "Department".city AS o,
                    NULL AS g
   FROM "Department"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Department#ref-manager>' AS p,
                    '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "People" AS "People_ref",
        "Department"
   WHERE "Department"."manager" = "People_ref"."ID"
   UNION ALL SELECT '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/Department#name>' AS p,
                    "Department".name AS o,
                    NULL AS g
   FROM "Department"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/People>' AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#addr>' AS p,
                    '"' || CAST(CAST("People".addr AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#fname>' AS p,
                    "People".fname AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#ID>' AS p,
                    '"' || CAST(CAST("People"."ID" AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#ref-deptName;deptCity>' AS p,
                    '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Department" AS "Department_ref",
        "People"
   WHERE "People"."deptName" = "Department_ref"."name"
     AND "People"."deptCity" = "Department_ref"."city"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#ref-addr>' AS p,
                    '<Addresses/ID=' || replace(replace(replace(replace(replace(replace(CAST("Addresses_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Addresses" AS "Addresses_ref",
        "People"
   WHERE "People"."addr" = "Addresses_ref"."ID"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#deptName>' AS p,
                    "People"."deptName" AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/People#deptCity>' AS p,
                    "People"."deptCity" AS o,
                    NULL AS g
   FROM "People"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/Projects>' AS o,
                    NULL AS g
   FROM "Projects"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#name>' AS p,
                    "Projects".name AS o,
                    NULL AS g
   FROM "Projects"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#lead>' AS p,
                    '"' || CAST(CAST("Projects".lead AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "Projects"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#deptCity>' AS p,
                    "Projects"."deptCity" AS o,
                    NULL AS g
   FROM "Projects"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#deptName>' AS p,
                    "Projects"."deptName" AS o,
                    NULL AS g
   FROM "Projects"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#ref-lead>' AS p,
                    '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Projects",
        "People" AS "People_ref"
   WHERE "Projects"."lead" = "People_ref"."ID"
   UNION ALL SELECT '_:Projects#' || CAST(CAST("Projects".rowid AS VARCHAR) AS VARCHAR) AS s,
                    '<http://example.com/base/Projects#ref-deptName;deptCity>' AS p,
                    '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "Projects",
        "Department" AS "Department_ref"
   WHERE "Projects"."deptName" = "Department_ref"."name"
     AND "Projects"."deptCity" = "Department_ref"."city"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>' AS p,
                    '<http://example.com/base/TaskAssignments>' AS o,
                    NULL AS g
   FROM "TaskAssignments"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#worker>' AS p,
                    '"' || CAST(CAST("TaskAssignments".worker AS VARCHAR) AS VARCHAR) || '"^^<http://www.w3.org/2001/XMLSchema#integer>' AS o,
                    NULL AS g
   FROM "TaskAssignments"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#deptCity>' AS p,
                    "TaskAssignments"."deptCity" AS o,
                    NULL AS g
   FROM "TaskAssignments"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#ref-deptName;deptCity>' AS p,
                    '<Department/ID=' || replace(replace(replace(replace(replace(replace(CAST("Department_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "TaskAssignments",
        "Department" AS "Department_ref"
   WHERE "TaskAssignments"."deptName" = "Department_ref"."name"
     AND "TaskAssignments"."deptCity" = "Department_ref"."city"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#ref-project;deptName;deptCity>' AS p,
                    '_:Projects#' || CAST(CAST("Projects_ref".rowid AS VARCHAR) AS VARCHAR) AS o,
                    NULL AS g
   FROM "Projects" AS "Projects_ref",
        "TaskAssignments"
   WHERE "TaskAssignments"."project" = "Projects_ref"."name"
     AND "TaskAssignments"."deptName" = "Projects_ref"."deptName"
     AND "TaskAssignments"."deptCity" = "Projects_ref"."deptCity"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#ref-worker>' AS p,
                    '<People/ID=' || replace(replace(replace(replace(replace(replace(CAST("People_ref"."ID" AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS o,
                    NULL AS g
   FROM "People" AS "People_ref",
        "TaskAssignments"
   WHERE "TaskAssignments"."worker" = "People_ref"."ID"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#project>' AS p,
                    "TaskAssignments".project AS o,
                    NULL AS g
   FROM "TaskAssignments"
   UNION ALL SELECT '<TaskAssignments/worker=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".worker AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || ';project=' || replace(replace(replace(replace(replace(replace(CAST("TaskAssignments".project AS VARCHAR), ' ', '%20'), '/', '%2F'), '(', '%28'), ')', '%29'), ',', '%2C'), ':', '%3A') || '>' AS s,
                    '<http://example.com/base/TaskAssignments#deptName>' AS p,
                    "TaskAssignments"."deptName" AS o,
                    NULL AS g
   FROM "TaskAssignments") AS anon_1
```

## Raw ouput triples
```
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#ID> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#city> "Cambridge" .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#state> "MA" .
<http://example.com/base/Addresses/ID=18> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Addresses> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ID> "23"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#city> "Cambridge" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#manager> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#name> "accounting" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ref-manager> <http://example.com/base/People/ID=8> .
<http://example.com/base/Department/ID=23> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Department> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ID> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#addr> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptCity> "Cambridge" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptName> "accounting" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#fname> "Bob" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-addr> <http://example.com/base/Addresses/ID=18> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/People/ID=7> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#ID> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#fname> "Sue" .
<http://example.com/base/People/ID=8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptCity> "Cambridge" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptName> "accounting" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#project> "pencil survey" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-project;deptName;deptCity> _:Projects#1 .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-worker> <http://example.com/base/People/ID=7> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#worker> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/TaskAssignments> .
_:Projects#1 <http://example.com/base/Projects#deptCity> "Cambridge" .
_:Projects#1 <http://example.com/base/Projects#deptName> "accounting" .
_:Projects#1 <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Projects#1 <http://example.com/base/Projects#name> "pencil survey" .
_:Projects#1 <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:Projects#1 <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:Projects#1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
_:Projects#2 <http://example.com/base/Projects#deptCity> "Cambridge" .
_:Projects#2 <http://example.com/base/Projects#deptName> "accounting" .
_:Projects#2 <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:Projects#2 <http://example.com/base/Projects#name> "eraser survey" .
_:Projects#2 <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:Projects#2 <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:Projects#2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
```

## Triple Diff
```diff
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#ID> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#city> "Cambridge" .
<http://example.com/base/Addresses/ID=18> <http://example.com/base/Addresses#state> "MA" .
<http://example.com/base/Addresses/ID=18> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Addresses> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ID> "23"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#city> "Cambridge" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#manager> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#name> "accounting" .
<http://example.com/base/Department/ID=23> <http://example.com/base/Department#ref-manager> <http://example.com/base/People/ID=8> .
<http://example.com/base/Department/ID=23> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Department> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ID> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#addr> "18"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptCity> "Cambridge" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#deptName> "accounting" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#fname> "Bob" .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-addr> <http://example.com/base/Addresses/ID=18> .
<http://example.com/base/People/ID=7> <http://example.com/base/People#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/People/ID=7> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#ID> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/People/ID=8> <http://example.com/base/People#fname> "Sue" .
<http://example.com/base/People/ID=8> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/People> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptCity> "Cambridge" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#deptName> "accounting" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#project> "pencil survey" .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-project;deptName;deptCity> _:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#ref-worker> <http://example.com/base/People/ID=7> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://example.com/base/TaskAssignments#worker> "7"^^<http://www.w3.org/2001/XMLSchema#integer> .
<http://example.com/base/TaskAssignments/worker=7;project=pencil%20survey> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/TaskAssignments> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#deptCity> "Cambridge" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#deptName> "accounting" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#name> "pencil survey" .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:cb117880a2c3bf9b9abfe5341ae500b5922ce0e7da9402b0cb1b68fcab7243ae9cd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#deptCity> "Cambridge" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#deptName> "accounting" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#lead> "8"^^<http://www.w3.org/2001/XMLSchema#integer> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#name> "eraser survey" .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#ref-deptName;deptCity> <http://example.com/base/Department/ID=23> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://example.com/base/Projects#ref-lead> <http://example.com/base/People/ID=8> .
_:cb12eb4fe3bd5291acd055109f01bd0be164e00796027f06baf87339b68b3e7b20a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.com/base/Projects> .
```

SUCCES