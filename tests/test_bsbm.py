"""
Run tests from [https://www.w3.org/TR/2012/NOTE-rdb2rdf-test-cases-20120814/]

Downloaded from [https://dvcs.w3.org/hg/rdb2rdf-tests/raw-file/default/rdb2rdf-ts.zip]
"""

import pathlib
import logging
import re
import pathlib
from typing import NamedTuple
import random

import pytest
import rdflib
from rdflib.namespace import RDF, Namespace
from rdflib.compare import to_isomorphic, graph_diff
from rdflib.util import from_n3

from util import setup_engine, create_database
from rdflib_r2r import R2RStore, R2RMapping, optimize_sparql, reset_sparql
from sqlalchemy.engine import Engine


dcterms = Namespace("http://purl.org/dc/elements/1.1/")
review = Namespace("http://purl.org/stuff/rev#Review")
bsbm = Namespace("http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/")

PATH = pathlib.Path("tests/BSBM")

@pytest.fixture(scope="module")
def path():
    return PATH


class TestCase(NamedTuple):
    id: str
    querytemplate: str
    params: dict
    meta: dict


TestCase.__test__ = False


@pytest.fixture(scope="module")
def dbs(path: pathlib.Path):
    dbs = {}
    for engine_name in ["sqlite", "duckdb"]:
        # Create database
        db = setup_engine(engine_name)
        fnames = [t.name for t in path.joinpath("dataset").glob("*.sql")]
        create_database(db, path.joinpath("dataset"), *fnames)
        dbs[engine_name] = db
    return dbs

def yield_testcases(path: pathlib.Path):

    qpath = path.joinpath("queries")
    for t in ["bi", "explore"]:
        tpath = qpath.joinpath(t)
        for d in sorted(tpath.glob("query*desc.txt")):
            params = dict(l.split('=') for l in open(d).read().splitlines()[2:])

            name, _, _ = d.name.partition("desc")
            querytemplate = tpath.joinpath(name + ".txt").open().read()

            id = f"bsbm-{t}-{name}"

            yield pytest.param(
                TestCase(
                    id=str(id),
                    querytemplate=querytemplate,
                    params=params,
                    meta={},
                ),
                id=str(id),
            )
 
def get_param_sets(path, graph):
    return {
        'ProductFeatureURI': set(graph[ : RDF.type : bsbm.ProductFeature]),
        'ProductURI': set(graph[ : RDF.type : bsbm.Product]),
        'ProductTypeURI': set(graph[ : RDF.type : bsbm.ProductType]),
        'ProductPropertyNumericValue': [rdflib.Literal(d) for d in range(1,500)],
        'OfferURI': set(graph[ : RDF.type : bsbm.ProductType]),
        'CurrentDate': set(d for _, d in graph[ : bsbm.validTo : ]),
        'ReviewURI': set(graph[ : RDF.type : review.Review]),
        'Dictionary1': [
            rdflib.Literal(w)
            for w in path.joinpath('titlewords.txt').open().read().splitlines()
        ],
        'CountryURI': set(d for _, d in graph[ : bsbm.country : ]),
    }

TESTS = list(yield_testcases(PATH))

@pytest.fixture()
def dbecho(pytestconfig):
    return pytestconfig.getoption("dbecho")

@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
@pytest.mark.parametrize("dbname", ["sqlite", "duckdb"])
def test_bsbm(testcase: TestCase, dbname: str, path, dbs):

    db = dbs[dbname]

    mapping = R2RMapping(rdflib.Graph().parse('tests/bsbm.ttl', format='ttl'))
    ns = mapping.graph.namespace_manager

    graph_rdb = rdflib.Graph(R2RStore(db=db, mapping=mapping), namespace_manager=ns)

    graph = rdflib.Graph()
    for t in graph_rdb:
        graph.add(t)
    param_sets = get_param_sets(path, graph)

    logging.warn(testcase.querytemplate)

    def sample_params(match):
        p = testcase.params.get(match.group(1))
        sample = random.choice( list(param_sets.get(p, ['?_'])) ).n3()
        logging.warn(f"{match.group(1)}: {sample}")
        return sample

    logging.warn(f"Graph has {len(graph)} triples")
    # gb = rdflib.term.URIRef('http://downlode.org/rdf/iso-3166/countries#GB')
    # for s in graph[:bsbm.country:gb]:
    #     logging.warn((s,'in gb'))
    #     break
    # raise

    tried = 0
    goal = None
    while not goal:
        query = re.sub('%([^%]+)%', sample_params, testcase.querytemplate)
        # logging.warn(query)

        goal = set(graph.query(query))
        logging.warn(f'goal: {len(goal)} triples\n' \
            + '\n'.join(' '.join(n.n3(ns) for n in t) for t in goal))
        if not goal:
            tried += 1
            logging.warn(f"Tried {tried} options")
            continue

        optimize_sparql() # THIS FUNCTION BREAKS NON-R2R STORES ?!?
        made = set(graph_rdb.query(query))
        logging.warn(f'made: {len(made)} triples\n' \
            + '\n'.join(' '.join(n.n3(ns) for n in t) for t in made))
        assert made == goal

    reset_sparql()