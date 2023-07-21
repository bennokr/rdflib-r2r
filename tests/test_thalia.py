"""
Test Harness for the Assessment of Legacy information Integration Approaches (THALIA)

https://www.w3.org/wiki/TaskForces/CommunityProjects/LinkingOpenData/THALIATestbed

https://www.openlinksw.com/scripts/sql/virtuoso/thalia_sql_to_rdf_views_generation.sql
"""

import logging
import pathlib
from typing import NamedTuple
import pytest

import rdflib
from rdflib.namespace import RDF, Namespace


from util import setup_engine, create_database
from rdflib_r2r import R2RStore, R2RMapping

test = Namespace("http://www.w3.org/2006/03/test-description#")
dcterms = Namespace("http://purl.org/dc/elements/1.1/")


class TestCase(NamedTuple):
    id: str
    sql_fname: str
    rdf_fname: str
    path: pathlib.Path
    query: str
    meta: dict


TestCase.__test__ = False

def fix_query(query):
    query = query.replace(', ?', ' ?')
    query = query.replace('\thasLecture', ':hasLecture')
    query = query.replace(':hasInstructor ?instructor\n', ':hasInstructor ?instructor;\n')
    query = query.replace('skos:subject <http://purl.org/subject/thalia/Databases>\n', 'skos:subject <http://purl.org/subject/thalia/Databases>;\n')
    
    
    return query


def parse_queries(path):
    lines = open(path.joinpath("queries.sparql")).read().splitlines()
    prefixes = [l for l in lines if l.startswith("PREFIX")]
    parts_idx = [i for i, l in enumerate(lines) if l.startswith("Query")]
    for i, pi in enumerate(parts_idx):
        part = lines[pi : (parts_idx[i + 1] if i + 1 < len(parts_idx) else None)]
        querylines = part[part.index("<SPARQL>") + 1 : part.index("</SPARQL>")]
        query = "\n".join(prefixes + querylines)
        query = fix_query(query)
        if 'TODO' in query:
            continue

        yield TestCase(
            id=f"THALIA-{i:02d}",
            sql_fname="benchmark-schema.sql",
            rdf_fname="benchmark-examples.rdf",
            path=path,
            query=query,
            meta={dcterms.title: lines[pi]},
        )

def fix_benchmark(fname):
    """Fix benchmark RDF file """
    import xml.etree.ElementTree as ET

    ns = dict([node for _, node in ET.iterparse(fname, events=['start-ns'])])
    for k,v in ns.items():
        ET.register_namespace(k, v)
    root = ET.parse(fname).getroot()

    # Fix lecture events by creating new event entity
    for lec in root.findall('.//hasLecture', ns):
        e = ET.Element("event:Event")
        e.text = lec.text
        for child in lec:
            e.append(child)
        lec.clear()
        lec.text = e.text
        lec.append(e)
    
    # Fix dates by moving datetime descriptions
    for t in root.findall('.//time:inDateTime', ns):
        if len(t) > 1:
            dt = t.find('time:DateTimeDescription', ns)
            for c in list(t):
                if c != dt:
                    t.remove(c)
                    dt.append(c)

    return ET.tostring(root).decode()

TESTS = list(parse_queries(pathlib.Path("tests/THALIA")))


@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
@pytest.mark.parametrize("engine_name", ["sqlite", "duckdb"])
def test_thalia(testcase: TestCase, engine_name: str):
    # Create database
    db = setup_engine(engine_name)
    create_database(db, testcase.path, testcase.sql_fname)

    mapping = None
    g_made = rdflib.Graph(R2RStore(db=db, mapping=mapping))

    fname_goal = str(testcase.path.joinpath(testcase.rdf_fname))
    g_goal = rdflib.Graph().parse(data = fix_benchmark(fname_goal), format='xml')
    
    logging.warn(testcase.query)

    a_goal = sorted(g_goal.query(testcase.query))

    logging.warn(a_goal)

    assert not a_goal
