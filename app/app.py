from flask import Flask, request, abort, render_template
import os, sys, pathlib
import sqlite3
import html

basedir = os.path.dirname(os.path.realpath(__file__))
test_path = pathlib.Path( basedir ).parent / 'tests'
sys.path.append( test_path )
import tests.test_rdb2rdf
import tests.test_bsbm
import tests.util
categories = {
    'RDB2RDF': tests.test_rdb2rdf.TESTS,
    'BSBM': tests.test_bsbm.TESTS
}

import rdflib
rdb2rdftest = rdflib.Namespace("http://purl.org/NET/rdb2rdf-test#")
from rdflib_r2r import R2RStore, R2RMapping

import app_deploy

app = Flask(__name__)
app.add_url_rule('/update_server', methods=['POST'], view_func=app_deploy.update)

def get_sql_mapping(categories, example, only_schema=False):
    schema, mapping = "", None
    for ex in categories['RDB2RDF']:
        if ex.id == example:
            for ts in ex.values:
                schema = ts.path.joinpath(ts.sql_fname).open().read()
                if rdb2rdftest.mappingDocument in ts.meta:
                    # Load mapping
                    mapfile = ts.path.joinpath(ts.meta[rdb2rdftest.mappingDocument])
                    fmt = rdflib.util.guess_format(str(mapfile))
                    mapping = R2RMapping(rdflib.Graph().parse(str(mapfile), format=fmt))
                    
    for ex in categories['BSBM']:
        if ex.id == example:
            for ts in ex.values:
                path = test_path / "BSBM" / "dataset"
                fnames = [t for t in path.glob("*.sql")]
                for fname in fnames:
                    script = fname.open().read()
                    for line in script.splitlines():
                        if not line.lower().startswith('insert') or not only_schema:
                            schema += line + '\n'
            mapping_file = test_path / "bsbm.ttl"
            mapping = R2RMapping(rdflib.Graph().parse(mapping_file, format="ttl"))
    
    return schema, mapping

@app.route("/")
def index():
    example = request.args.get("example", "")
    schema, mapping = "", None
    sparql = 'select ?s ?p ?o where {?s ?p ?o}'
    if example:
        schema, mapping = get_sql_mapping(categories, example, only_schema=True)

    # Schema visualize
    con = sqlite3.connect('')
    cur = con.executescript(schema)
    mermaid = "erDiagram\n"
    all_fks = []
    for _, table, *_ in cur.execute('select * from sqlite_master').fetchall():
        if table.startswith('sqlite'):
            continue
        fks = cur.execute(f'PRAGMA foreign_key_list("{table}")').fetchall()
        fks = {col: (fk_table, fk_col) for _, _, fk_table, col, fk_col, *_ in fks}
        for col, (fk_table, fk_col) in fks.items():
            all_fks += [(table, fk_table, f'{col}->{fk_col}')]
        mermaid += f'    {table} {{\n'
        cols = cur.execute(f'PRAGMA table_info("{table}")').fetchall()
        for _, colname, coltype, notnull, default, pk in cols:
            pk = 'PK' if pk else ''
            fk = 'FK' if colname in fks else ''
            coltype = coltype.replace(' ', '')
            mermaid += f'        {coltype} {colname} {pk} {fk}\n'
        mermaid += '    }\n\n'
    for table1, table2, name in all_fks:
        mermaid += f'{table1} ||--o{{ {table2} : "{name}"\n'


    return render_template('index.html', 
        categories=categories, 
        example=example,
        schema=schema,
        mermaid=mermaid,
        mapping=mapping.graph.serialize() if mapping else '',
        sparql=sparql,
    )

@app.route("/make_sql")
def make_sql():
    example = request.args.get("example", "")
    sql, mapping = get_sql_mapping(categories, example, only_schema=False)
    con = sqlite3.connect('')
    cur = con.executescript(sql)
    db = tests.util.setup_engine('sqlite', creator = lambda: con)
    if mapping is None:
        mapping = R2RMapping.from_db(db)
    ns = mapping.graph.namespace_manager
    r2r = R2RStore(db=db, mapping=mapping)

    sparql = request.args.get("sparql", "")
    sql_query = r2r.getSQL(sparql) 
    return sql_query

@app.route("/run_sql")
def run_sql():
    example = request.args.get("example", "")
    db, _ = get_sql_mapping(categories, example, only_schema=False)
    print(db)
    con = sqlite3.connect('')
    cur = con.executescript(db)
    
    sql = request.args.get("sql", "")
    results = cur.execute(sql).fetchall()
    return '<br>'.join(html.escape(str(r)) for r in results)

if __name__ == '__main__':
    app.run(debug=True)
