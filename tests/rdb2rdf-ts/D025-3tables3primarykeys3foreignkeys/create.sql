CREATE TABLE "Addresses" (
	"ID" INT PRIMARY KEY,
	"city" VARCHAR(10),
	"state" CHAR(2)
);

CREATE TABLE "Department" (
	"ID" INT PRIMARY KEY,
	"name" VARCHAR(50),
	"city" VARCHAR(50),
	-- "manager" INT,
	UNIQUE ("name", "city")
);

CREATE TABLE "People" (
	"ID" INT PRIMARY KEY,
	"fname" VARCHAR(10),
	"addr" INT,
	"deptName" VARCHAR(50),
	"deptCity" VARCHAR(50),
	FOREIGN KEY ("addr") REFERENCES "Addresses"("ID"),
	FOREIGN KEY("deptName", "deptCity") REFERENCES "Department"("name", "city")
);

ALTER TABLE "Department" ADD "manager" INT REFERENCES "People"("ID");

INSERT INTO "Addresses" ("ID", "city",      "state")
                 VALUES (18,   'Cambridge', 'MA');

INSERT INTO "People" ("ID", "fname", "addr", "deptName", "deptCity" )
              VALUES (8,    'Sue',   NULL,   NULL,       NULL);

INSERT INTO "Department" ("ID", "name",       "city",      "manager")
                  VALUES (23,   'accounting', 'Cambridge', 8);

INSERT INTO "People" ("ID", "fname", "addr", "deptName",   "deptCity" )
              VALUES (7,    'Bob',   18,     'accounting', 'Cambridge');
              
CREATE TABLE "Projects" (
	"lead" INT,
	"name" VARCHAR(50),  
	"deptName" VARCHAR(50), 
	"deptCity" VARCHAR(50),
	UNIQUE ("lead", "name"),
	UNIQUE ("name", "deptName", "deptCity"),
	FOREIGN KEY ("deptName", "deptCity") REFERENCES "Department"("name", "city"),
	FOREIGN KEY ("lead") REFERENCES "People"("ID")
);
CREATE TABLE "TaskAssignments" (
	"worker" INT,
	"project" VARCHAR(50), 
	"deptName" VARCHAR(50), 
	"deptCity" VARCHAR(50),
	PRIMARY KEY ("worker", "project")
	FOREIGN KEY ("project", "deptName", "deptCity") REFERENCES "Projects"("name", "deptName", "deptCity"),
	FOREIGN KEY ("deptName", "deptCity") REFERENCES "Department"("name", "city"),
	FOREIGN KEY ("worker") REFERENCES "People"("ID")
);

INSERT INTO  "Projects" ("lead", "name",          "deptName",   "deptCity" )
                 VALUES (8,      'pencil survey', 'accounting', 'Cambridge');
INSERT INTO  "Projects" ("lead", "name",          "deptName",   "deptCity" )
                 VALUES (8,      'eraser survey', 'accounting', 'Cambridge');
INSERT INTO "TaskAssignments" ("worker", "project",       "deptName",   "deptCity" )
                       VALUES (7,        'pencil survey', 'accounting', 'Cambridge');              