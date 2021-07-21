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
        'ProductType': set(graph[ : RDF.type : bsbm.ProductType]),
        'ProductPropertyNumericValue': [rdflib.Literal(d) for d in range(1,500)],
        'OfferURI': set(graph[ : RDF.type : bsbm.ProductType]),
        'CurrentDate': set(d for _, d in graph[ : bsbm.validTo : ]),
        'ReviewURI': set(graph[ : RDF.type : review.Review]),
        'Dictionary1': [
            w for w in path.joinpath('titlewords.txt').open().read().splitlines()
        ],
        'CountryURI': set(d for _, d in graph[ : bsbm.country : ]),
        'Date': set(d._value for _, d in graph[ : DC.date : ]),
        'ProducerURI': set(graph[ : RDF.type : bsbm.Producer]),
    }

TESTS = list(yield_testcases(PATH))

@pytest.fixture()
def dbecho(pytestconfig):
    return pytestconfig.getoption("dbecho")

@pytest.mark.timeout(60)
@pytest.mark.parametrize("testcase", TESTS, ids=[t.id for t in TESTS])
@pytest.mark.parametrize("engine_name", ["sqlite", "duckdb"])
def test_bsbm(testcase: TestCase, engine_name: str, path, dbs):
    db = dbs[engine_name]

    mapping = R2RMapping(rdflib.Graph().parse('tests/bsbm.ttl', format='ttl'))
    ns = mapping.graph.namespace_manager

    graph_rdb = rdflib.Graph(R2RStore(db=db, mapping=mapping), namespace_manager=ns)

    graph = rdflib.Graph()
    for t in graph_rdb:
        graph.add(t)
    param_sets = get_param_sets(path, graph)

    logging.warn(testcase.querytemplate)
    
    def get_params(querytemplate):
        params = {}
        pnames = set(re.findall('%([^%]+)%', querytemplate))
        if any(p.startswith('ConsecutiveMonth') for p in pnames):
            from datetime import timedelta
            ps = [p for p in pnames if p.startswith('ConsecutiveMonth')]
            sample = random.choice( list(param_sets['Date']) )
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
        alt = pname.split('_')[0]
        domain = param_sets.get(tname) or param_sets[alt]
        sample = random.choice( list(domain) )
        return sample.n3() if isinstance(sample, rdflib.term.Node) else sample

    logging.warn(f"Graph has {len(graph)} triples")
    # gb = rdflib.term.URIRef('http://downlode.org/rdf/iso-3166/countries#GB')
    # for s in graph[:bsbm.country:gb]:
    #     logging.warn((s,'in gb'))
    #     break
    # raise

    goal = None
    querytemplate = testcase.querytemplate
    bad_params = set()
    while not goal:
        params = get_params(querytemplate)
        if str(params) in bad_params:
            continue
        logging.warn(f'params: {params}')
        query = re.sub('%([^%]+)%', lambda m: params[m.group(1)], querytemplate)

        try:
            goal = set(graph.query(query))
        except TypeError as e:
            logging.warn(f'Query failed with TypeError {e}')
        
        for t in goal:
            if any(n is None for n in t):
                logging.warn(f"None in goal result: {t}")

        gtxt = '\n'.join('\t'.join((n.n3(ns) if n else '') for n in t) for t in goal)
        logging.warn(f'goal: {len(goal)} triples\n' + gtxt)
        if not goal:
            bad_params.add( str(params) )
            logging.warn(f"Tried {len(bad_params)} options")
            continue

        optimize_sparql()


        made = set(graph_rdb.query(query))
        mtxt = '\n'.join('\t'.join((n.n3(ns) if n else '') for n in t) for t in made)
        logging.warn(f'made: {len(made)} triples\n' + mtxt)
        
        sql_query = graph_rdb.store.getSQL(query)
        test_out = pathlib.Path(f'test-results/{engine_name}-bsbm/')
        test_out.mkdir(parents=True, exist_ok=True)
        test_out.joinpath(f"{testcase.id}.md").write_text(f"""
# {testcase.id}

## Random parameter sample
```
{params}
```

## SPARQL query
```sparql
{query}
```

## Goal results
```
{gtxt}
```

## Created SQL query
```sql
{sql_query}
```

## Created SQL results
```
{mtxt}
```
""")

        assert made == goal
        break
    reset_sparql() 

def test_synthesis(module_results_df):
    df = module_results_df
    ids = df.testcase.apply(lambda x: x.id)
    def get_link(r):
        _, part, q = r.testcase.id.split('-')
        pre = 'http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/'
        parts = {
            'explore': 'spec/ExploreUseCase/#queryTripleQ',
            'bi': 'spec/BusinessIntelligenceUseCase/index.html#queryTripleQ'
        }
        link = pre + parts.get(part) + q.strip("query")
        return f"[{r.testcase.id}]({link})"
    df["link"] = df.apply(get_link, axis=1)
    
    status_emoji = {
        "passed": "✅",
        "failed": "❌",
        "xfailed": "🔆",
        "xpassed": "❗️",
    }
    testdir = pathlib.Path('test-results/')
    testdir.mkdir(parents=True, exist_ok=True)

    def get_status_link(row):
        logging.warn(row)
        testcase = row.testcase
        text = status_emoji.get(row.status, "") + " " + row.status
        return f"[{text}]({row.engine_name}-rdb2rdf/{testcase.id}.md)"
    df["status"] = df.apply(get_status_link, axis=1)

    with testdir.joinpath("bsbm.md").open("w") as fw:
        print("# Test results\n", file=fw)
        df = df[["engine_name", "link", "status", "duration_ms"]]
        print(df.to_markdown(index=False), file=fw)
