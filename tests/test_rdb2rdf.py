"""
Run tests from [https://www.w3.org/TR/2012/NOTE-rdb2rdf-test-cases-20120814/]

Downloaded from [https://dvcs.w3.org/hg/rdb2rdf-tests/raw-file/default/rdb2rdf-ts.zip]
"""

import pathlib
import logging
from typing import NamedTuple
import re
import base64

import pytest
import rdflib
from rdflib.namespace import RDF, Namespace
from rdflib.compare import to_isomorphic, graph_diff
from rdflib.util import from_n3
from sqlalchemy import create_engine, text, engine as sqlengine

from rdflib_r2r.r2r_store import R2RStore, Mapping

test = Namespace("http://www.w3.org/2006/03/test-description#")
dcterms = Namespace("http://purl.org/dc/elements/1.1/")
rdb2rdftest = Namespace("http://purl.org/NET/rdb2rdf-test#")
base = Namespace("http://www.w3.org/2001/sw/rdb2rdf/test-cases/#")


class TestCase(NamedTuple):
    id: str
    sql_fname: str
    path: pathlib.Path
    meta: dict


TestCase.__test__ = False


def yield_database_testcases(path: pathlib.Path):
    logging.warn("Running w3c rdb2rdf test '%s'.", path.name)
    manifest_file = str(path.joinpath("manifest.ttl"))

    g = rdflib.Graph()
    g.parse(manifest_file, format="ttl")
    # Get test databases
    for dbspec in g[: RDF.type : rdb2rdftest.DataBase]:
        logging.warn("Loading DB: '%s'", g.value(dbspec, dcterms.title))
        sql_fname = g.value(dbspec, rdb2rdftest.sqlScriptFile)

        for testspec in g.objects(dbspec, rdb2rdftest.relatedTestCase):
            id = g.value(testspec, dcterms.identifier)
            if id:
                marks = []
                if not g.value(testspec, rdb2rdftest.hasExpectedOutput).toPython():
                    marks.append(pytest.mark.xfail)
                yield pytest.param(
                    TestCase(
                        id=str(id),
                        sql_fname=sql_fname,
                        path=path,
                        meta=dict(g[testspec:]),
                    ),
                    id=str(id),
                    marks=marks,
                )


def setup_engine(name):
    if name == "sqlite":
        import sqlite3

        sqlite3.register_adapter(bool, int)
        sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))

        return create_engine(
            "sqlite:///:memory:",
            echo=True,
            future=True,
            connect_args={
                "detect_types": sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
            },
            native_datetime=True,
        )
    
    if name == "duckdb":
        return create_engine("duckdb:///:memory:", connect_args={
            'read_only':False
        })

def create_database(db, path, sql_fname):
    sql_script = path.joinpath(sql_fname).open().read()
    connection = db.raw_connection()
    logging.warn(connection.connection)
    try:
        connection.execute(sql_script, (), None)
    except Exception as e:
        logging.warn(e)
        try:
            cursor = connection.cursor()
            cursor.execute(sql_script)
        except Exception as e:
            logging.warn(e)
            try:
                cursor = connection.cursor()
                cursor.executescript(sql_script)
            except Exception as e:
                raise Exception(f"Problem with {path}: {e}")
    finally:
        connection.close()

PATHS = sorted(
    path
    for path in pathlib.Path(__file__).parent.joinpath("rdb2rdf-ts").iterdir()
    if path.name[0] != "."
)

TESTS = [
    testcase
    for path in PATHS
    for testcase in sorted(yield_database_testcases(path), key=lambda s: s.id)
]


@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
@pytest.mark.parametrize("engine_name", ["sqlite", "duckdb"])
# @pytest.mark.parametrize("engine_name", ["duckdb"])
def test_rdb2rdf(testcase: TestCase, engine_name: str):
    # Create database
    db = setup_engine(engine_name)
    create_database(db, testcase.path, testcase.sql_fname)

    # Create mapped R2RStore
    mapping = None
    if rdb2rdftest.mappingDocument in testcase.meta:
        mapfile = testcase.path.joinpath(testcase.meta[rdb2rdftest.mappingDocument])
        fmt = rdflib.util.guess_format(str(mapfile))
        mapping = Mapping(rdflib.Graph().parse(str(mapfile), format=fmt))
    else:
        # Make direct mapping
        mapping = Mapping.from_db(db)

    g_made = rdflib.Graph(R2RStore(db=db, mapping=mapping))

    outfile = testcase.path.joinpath(testcase.meta[rdb2rdftest.output])
    fmt = rdflib.util.guess_format(str(outfile))
    if fmt == "nquads":
        rx = re.compile(r"([^ ]+) ([^ ]+) (.+?) ?(?: (<[^>]+>))? \.$")
        g_goal = rdflib.ConjunctiveGraph()
        for li, l in enumerate(open(outfile).read().splitlines()):
            if l.strip():
                m = rx.match(l.strip())
                if m:
                    g_goal.add(tuple(from_n3(n) for n in m.groups()))
                else:
                    logging.warn(f"bad nquads line {li} in {outfile}: {l}")
        logging.warn(("g_goal", type(g_goal), len(list(g_goal)), list(g_goal)))
    else:
        g_goal = rdflib.Graph().parse(str(outfile), format=fmt)
        logging.warn(
            (
                "g_goal",
                type(g_goal),
                len(list(g_goal)),
                g_goal.serialize(format="turtle"),
            )
        )

    # l1 = list(g_made)
    # g_made = rdflib.Graph()
    # for t in l1:
    #     g_made.add(t)
    # s1 = g_made.serialize(format="turtle")
    # for t in l1:
    #     logging.warn(("g_made", t))
    # logging.warn(("g_made", len(l1), s1))
    # logging.warn(("g_goal", len(list(g_goal)), g_goal.serialize(format="turtle")))

    iso_made, iso_goal = to_isomorphic(g_made), to_isomorphic(g_goal)
    in_both, in_made, in_goal = graph_diff(iso_made, iso_goal)

    def dump_nt_sorted(g):
        return sorted(g.serialize(format="nt").strip().splitlines())

    for li, line in enumerate(dump_nt_sorted(in_both)):
        logging.warn(f"in_both {li}/{len(list(in_both))}: {line}")
    for li, line in enumerate(dump_nt_sorted(in_made)):
        logging.warn(f"in_made {li}/{len(list(in_made))}: {line}")
    for li, line in enumerate(dump_nt_sorted(in_goal)):
        logging.warn(f"in_goal {li}/{len(list(in_goal))}: {line}")
    assert iso_made == iso_goal


def test_synthesis(module_results_df):
    df = module_results_df
    ids = df.testcase.apply(lambda x: x.id)
    df["link"] = (
        "[" + ids + "]" + "(https://www.w3.org/TR/rdb2rdf-test-cases/#" + ids + ")"
    )
    df["title"] = df.testcase.apply(lambda x: x.meta.get(dcterms.title))
    status_emoji = {
        "passed": "✅",
        "failed": "❌",
        "xfailed": "🔆",
        "xpassed": "❗️",
    }
    logging.warn(("statuses", set(df["status"])))
    df["status"] = df["status"].apply(lambda s: status_emoji.get(s, "") + " " + s)
    with open("test-results.md", "w") as fw:
        print("# Test results\n", file=fw)
        df = df[["engine_name", "link", "status", "duration_ms", "title"]]
        print(df.to_markdown(index=False), file=fw)
