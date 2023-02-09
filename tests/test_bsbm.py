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
from natsort import natsorted
import math

import pytest
import rdflib
from rdflib.namespace import RDF, DC, Namespace
from rdflib.compare import to_isomorphic, graph_diff
from rdflib.util import from_n3

from util import setup_engine, create_database
from rdflib_r2r import R2RStore, R2RMapping, optimize_sparql, reset_sparql
from sqlalchemy.engine import Engine


dcterms = Namespace("http://purl.org/dc/elements/1.1/")
review = Namespace("http://purl.org/stuff/rev#Review")
bsbm = Namespace("http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/")

PATH = pathlib.Path("tests/BSBM")
TIMEOUT = 60

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
        for d in natsorted(tpath.glob("query*desc.txt"), key=lambda x: str(x)):
            params = dict(l.split("=") for l in open(d).read().splitlines()[2:])

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
        "ProductFeatureURI": set(graph[: RDF.type : bsbm.ProductFeature]),
        "ProductURI": set(graph[: RDF.type : bsbm.Product]),
        "ProductTypeURI": set(graph[: RDF.type : bsbm.ProductType]),
        "ProductType": set(graph[: RDF.type : bsbm.ProductType]),
        "ProductPropertyNumericValue": [rdflib.Literal(d) for d in range(1, 500)],
        "OfferURI": set(graph[: RDF.type : bsbm.ProductType]),
        "CurrentDate": set(d for _, d in graph[: bsbm.validTo :]),
        "ReviewURI": set(graph[: RDF.type : bsbm.Review]),
        "Dictionary1": [
            w for w in path.joinpath("titlewords.txt").open().read().splitlines()
        ],
        "CountryURI": set(d for _, d in graph[: bsbm.country :]),
        "Date": set(d._value for _, d in graph[: DC.date :]),
        "ProducerURI": set(graph[: RDF.type : bsbm.Producer]),
    }


TESTS = list(yield_testcases(PATH))


def get_test_hyperlink(id):
    _, part, q = id.split("-")
    pre = "http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/"
    parts = {
        "explore": "spec/ExploreUseCase/#queryTripleQ",
        "bi": "spec/BusinessIntelligenceUseCase/index.html#queryTripleQ",
    }
    link = pre + parts.get(part) + q.strip("query")
    return f"[{id}]({link})"


@pytest.fixture()
def dbecho(pytestconfig):
    return pytestconfig.getoption("dbecho")


def normalize(results):
    def norm(x):
        if x is None:
            return None
        x = x.toPython()
        if isinstance(x, float):
            return round(x, 4)
        return x

    normalized = set()
    for row in results:
        row = tuple(norm(x) for x in row)
        normalized.add( row )
    return normalized


@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
@pytest.mark.parametrize("engine_name", ["sqlite"])  # ["sqlite", "duckdb"]
def test_bsbm(testcase: TestCase, engine_name: str, path, dbs):
    test_out = pathlib.Path(f"test-results/{engine_name}-bsbm/")
    test_out.mkdir(parents=True, exist_ok=True)
    test_file = test_out.joinpath(f"{testcase.id}.md")
    report = f"# {testcase.id}\n{get_test_hyperlink(testcase.id)}\n\n"

    try:
        db = dbs[engine_name]

        mapping = R2RMapping(rdflib.Graph().parse("tests/bsbm.ttl", format="ttl"))
        ns = mapping.graph.namespace_manager

        graph_rdb = rdflib.Graph(R2RStore(db=db, mapping=mapping), namespace_manager=ns)

        graph = rdflib.Graph()
        for t in graph_rdb:
            graph.add(t)
        param_sets = get_param_sets(path, graph)

        logging.warn(testcase.querytemplate)
        logging.warn(testcase.params)

        import pickle
        cache_params = {}
        cachefile = pathlib.Path("test-results/bsbm-params.pickle")
        if cachefile.exists():
            cache_params = pickle.load(cachefile.open('rb'))

        def get_params(querytemplate):
            params = {}
            pnames = set(re.findall("%([^%]+)%", querytemplate))
            if any(p.startswith("ConsecutiveMonth") for p in pnames):
                from datetime import timedelta

                ps = [p for p in pnames if p.startswith("ConsecutiveMonth")]
                sample = random.choice(list(param_sets["Date"]))
                month = sample.replace(day=1)
                for p in sorted(ps, key=lambda x: int(x[-1])):
                    params[p] = month.isoformat()
                    month = (month + timedelta(days=40)).replace(day=1)
            for pname in pnames:
                if pname not in params:
                    params[pname] = sample_param(pname)
            
            return params

        def sample_param(pname):
            tname = testcase.params.get(pname)
            alt = pname.split("_")[0]
            domain = param_sets.get(tname) or param_sets[alt]
            sample = random.choice(list(domain))
            return sample.n3() if isinstance(sample, rdflib.term.Node) else sample

        logging.warn(f"Graph has {len(graph)} triples")

        goal = None
        querytemplate = testcase.querytemplate
        bad_params = set()
        while not goal:
            if testcase.id in cache_params:
                params = cache_params[testcase.id]
            else:
                params = get_params(querytemplate)
            if str(params) in bad_params:
                continue
            query = re.sub("%([^%]+)%", lambda m: params[m.group(1)], querytemplate)

            try:
                goal = set(graph.query(query))
            except TypeError as e:
                logging.warn(f"Query failed with TypeError {e}")

            gtxt = "\n".join(
                "\t".join((n.n3(ns) if n else "") for n in t) for t in goal
            )
            if goal:
                logging.warn(f"goal: {len(goal)} triples\n" + gtxt)
                logging.warn(f"Tried {len(bad_params)} options")
                logging.warn(f"params: {params}")
                cache_params[testcase.id] = params
                pickle.dump(cache_params, cachefile.open('wb'))
            
            if not goal:
                bad_params.add(str(params))
                continue
            
            for t in goal:
                if any(n is None for n in t):
                    logging.warn(f"None in goal result: {t}")

            optimize_sparql()

            paramstr = "\n".join(f"{k} = {v}" for k, v in params.items())
            report += f"## Random parameter sample\n```\n{paramstr}\n```\n\n"
            report += f"## SPARQL query\n```sparql\n{query}\n```\n\n"
            report += f"## Goal results\n```\n{gtxt}\n```\n\n"
            
            sql_query = graph_rdb.store.getSQL(query) 
            report += f"## Created SQL query\n```sql\n{sql_query}\n```\n\n"

            made = set(graph_rdb.query(query))
            mtxt = "\n".join(
                "\t".join((n.n3(ns) if n else "") for n in t) for t in made
            )
            logging.warn(f"made: {len(made)} triples\n" + mtxt)
            report += f"## Created SQL results\n```\n{mtxt}\n```\n\n"

            report += ('SUCCES' if made == goal else 'FAIL')
            test_file.write_text(report)

            assert normalize(goal) == normalize(made)
            break
        reset_sparql()
    except Exception as e:
        if not isinstance(e, AssertionError):
            import traceback, os
            tb = traceback.format_exc().replace(os.getcwd(), '')
            report += f"\n```\n{tb}\n```"
            test_file.write_text(report)
        raise e


def test_synthesis(module_results_df):
    df = module_results_df
    df["link"] = df.apply(lambda r: get_test_hyperlink(r.testcase.id), axis=1)
    status_emoji = {
        "passed": "✅",
        "failed": "❌",
        "xfailed": "🔆",
        "xpassed": "❗️",
        "timeout": "⏱",
    }
    testdir = pathlib.Path("test-results/")
    testdir.mkdir(parents=True, exist_ok=True)

    def get_status_link(row):
        logging.warn(row)
        testcase = row.testcase
        text = status_emoji.get(row.status, "") + " " + row.status
        return f"[{text}]({row.engine_name}-bsbm/{testcase.id}.md)"

    df["status"][df.duration_ms > TIMEOUT*1000] = "timeout"
    df["status"] = df.apply(get_status_link, axis=1)

    with testdir.joinpath("bsbm.md").open("w") as fw:
        print("# Test results\n", file=fw)
        df = df[["engine_name", "link", "status", "duration_ms"]]
        print(df.to_markdown(index=False), file=fw)
