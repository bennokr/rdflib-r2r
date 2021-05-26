"""
Run tests from [https://www.w3.org/TR/2012/NOTE-rdb2rdf-test-cases-20120814/]

Downloaded from [https://dvcs.w3.org/hg/rdb2rdf-tests/raw-file/default/rdb2rdf-ts.zip]
"""
import pytest
import pathlib
import logging
from typing import NamedTuple

import rdflib
from rdflib.namespace import RDF, Namespace
from rdflib.compare import to_isomorphic, graph_diff
from sqlalchemy import create_engine, text, engine as sqlengine

from rdflib_r2r.r2r_store import R2RStore, Mapping

test = Namespace("http://www.w3.org/2006/03/test-description#")
dcterms = Namespace("http://purl.org/dc/elements/1.1/")
rdb2rdftest = Namespace("http://purl.org/NET/rdb2rdf-test#")
base = Namespace("http://www.w3.org/2001/sw/rdb2rdf/test-cases/#")


class TestCase(NamedTuple):
    id: str
    db: sqlengine.Engine
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
        sql_script = path.joinpath(sql_fname).open().read()
        db = setup_engine()
        connection = db.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_script)
        except:
            try:
                cursor.executescript(sql_script)
            except Exception as e:
                raise Exception(f"Problem with {path}")
        finally:
            connection.close()
        # with db.connect() as conn:
        # conn.execute(text(sql_script))

        for testspec in g.objects(dbspec, rdb2rdftest.relatedTestCase):
            id = g.value(testspec, dcterms.identifier)
            if id:
                yield TestCase(
                    id=str(id),
                    db=db,
                    path=path,
                    meta=dict(g[testspec:]),
                )


def setup_engine():
    return create_engine("sqlite:///:memory:", echo=True, future=True)


PATHS = sorted(
    path
    for path in pathlib.Path(__file__).parent.joinpath("rdb2rdf-ts").iterdir()
    if path.name[0] != "."
)  # [:7]

TESTS = [
    testcase
    for path in PATHS
    for testcase in sorted(yield_database_testcases(path), key=lambda s: s.id)
]


@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
def test_rdb2rdf(testcase: TestCase):
    # Create mapped R2RStore
    mapping = None
    if rdb2rdftest.mappingDocument in testcase.meta:
        mapfile = testcase.path.joinpath(testcase.meta[rdb2rdftest.mappingDocument])
        fmt = rdflib.util.guess_format(str(mapfile))
        mapping = Mapping(rdflib.Graph().parse(str(mapfile), format=fmt))
    else:
        # Make direct mapping
        mapping = Mapping.from_db(testcase.db)

    g1 = rdflib.Graph(R2RStore(db=testcase.db, mapping=mapping))

    if testcase.meta[rdb2rdftest.hasExpectedOutput].toPython():
        outfile = testcase.path.joinpath(testcase.meta[rdb2rdftest.output])
        fmt = rdflib.util.guess_format(str(outfile))
        g2 = rdflib.Graph().parse(str(outfile), format=fmt)

        # logging.warn(('g1.contexts()', g1.contexts()))

        # l1 = list(g1)
        # g1 = rdflib.Graph()
        # for t in l1:
        #     g1.add(t)
        # s1 = g1.serialize(format="turtle")
        # for t in l1:
        #     logging.warn(("g1", t))
        # logging.warn(("g1", len(l1), s1))
        # logging.warn(("g2", len(list(g2)), g2.serialize(format="turtle")))

        iso1, iso2 = to_isomorphic(g1), to_isomorphic(g2)
        in_both, in_1, in_2 = graph_diff(iso1, iso2)

        def dump_nt_sorted(g):
            return sorted(g.serialize(format="nt").splitlines())

        logging.warn(("in_both", len(list(in_both)), dump_nt_sorted(in_both)))
        logging.warn(("in_1", len(list(in_1)), dump_nt_sorted(in_1)))
        logging.warn(("in_2", len(list(in_2)), dump_nt_sorted(in_2)))
        assert iso1 == iso2


def test_synthesis(module_results_df):
    df = module_results_df
    ids = df.testcase.apply(lambda x: x.id)
    df["link"] = (
        "[" + ids + "]" + "(https://www.w3.org/TR/rdb2rdf-test-cases/#" + ids + ")"
    )
    status_emoji = {
        "passed": "✅",
        "failed": "❌",
    }
    df["status"] = df["status"].apply(lambda s: status_emoji.get(s) + " " + s)
    with open("test-results.md", "w") as fw:
        print("# Test results\n", file=fw)
        print(df[["link", "status", "duration_ms"]].to_markdown(index=False), file=fw)
