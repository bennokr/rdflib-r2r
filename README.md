# rdflib-r2r

``rdflib-r2r`` is a wrapper library for accessing existing relational databases from rdflib using r2rml rdb2rdf mappings.

It provides a virtual knowledge graph view of a relational database and allows for the rewriting of SPARQL queries to SQL. The [``rdflib-r2r`` documentation](https://rdflib-r2r.readthedocs.io) provides a comprehensive guide on how to use the library to interact with the R2RML-mapped relational data as if it were a semantic web data source.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bennokr/rdflib-r2r/HEAD)

## Background

The Resource Description Framework (RDF) is a widely used framework for modeling and exchanging data on the web. It provides a flexible and extensible data model that allows data to be represented as a directed graph, where nodes represent entities, and edges represent relationships between them. However, many data sources, such as relational databases, do not natively support RDF. This is where R2RML comes in.

The R2RML standard provides a way to map relational databases to RDF. It allows users to define mappings between the tables and columns in a relational database and RDF graphs. This enables the creation of virtual knowledge graphs from existing relational databases. The R2RML standard defines a set of rules for mapping relational data to RDF, such as the use of SQL queries to retrieve data, and the mapping of columns to RDF properties.

The Python library that we are presenting in this documentation extends the popular RDF library ``rdflib``, providing an implementation of the R2RML standard. The library allows users to generate a virtual knowledge graph from a relational database, providing a simple and easy-to-use interface for querying the data. Additionally, the library provides a query rewriting functionality that allows users to write SPARQL queries and have them automatically rewritten to SQL queries, optimizing query execution for large datasets.

## Installation
```
pip install -e .
```

### Running Tests
Use `pytest -k` to perform selected tests, `pytest -x` to stop after failure. Examples:

```
pytest -xk "test_rdb2rdf[sqlite-"
pytest --nopattern -xk "test_rdb2rdf[sqlite-DirectGraphTC0014"
pytest -k "test_bsbm[sqlite-bsbm-explore-query3]"
```

## Getting Started
...

## Contributing
..
