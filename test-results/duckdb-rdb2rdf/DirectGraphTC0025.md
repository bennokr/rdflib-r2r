# DirectGraphTC0025
[link](https://www.w3.org/TR/rdb2rdf-test-cases/#DirectGraphTC0025)
Generation of triples from three tables, three primary keys, three foreign keys



```
Traceback (most recent call last):
  File "/tests/util.py", line 45, in create_database
    cursor.execute(sql_script, (), None)
RuntimeError: Parser Error: syntax error at or near "FOREIGN"
LINE 55: 	FOREIGN KEY ("project", "deptName", "deptCity") REFERENCES "Projects"("name", "deptName", "deptCity"),
	FOREIGN KEY ("deptName", "deptCity") REFERENCES "Department"("name", "city"),
	FOREIGN KEY ("worker") REFERENCES "People"("ID")
);

INSERT INTO  "Projects" ("lead", "name",          "deptName",   "deptCity" )
                 VALUES (8,      'pencil survey', 'accounting', 'Cambridge');
INSERT INTO  "Projects" ("lead", "name",          "deptName",   "deptCity" )
                 VALUES (8,      'eraser survey', 'accounting', 'Cambridge');
INSERT INTO "TaskAssignments" ("worker", "project",       "deptName",   "deptCity" )
                       VALUES (7,        'pencil survey', 'accounting', 'Cambridge');              ...
         ^

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/util.py", line 49, in create_database
    cursor.executescript(sql_script)
TypeError: 'NoneType' object is not callable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tests/test_rdb2rdf.py", line 99, in test_rdb2rdf
    create_database(db, testcase.path, testcase.sql_fname)
  File "/tests/util.py", line 51, in create_database
    raise Exception(f"Problem with {path}: {e}")
Exception: Problem with /tests/rdb2rdf-ts/D025-3tables3primarykeys3foreignkeys: 'NoneType' object is not callable

```