.. rdflib-r2r documentation master file, created by
   sphinx-quickstart on Wed Mar 15 10:01:44 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Contents
========

.. toctree::
   :maxdepth: 2

   self

   api/rdflib_r2r

   
.. autosummary::
  :toctree: stubs

Welcome to the documentation for ``rdflib-r2r``. This library provides a virtual knowledge graph view of a relational database and allows for the rewriting of SPARQL queries to SQL. This document provides a comprehensive guide on how to use the library to interact with the R2RML-mapped relational data as if it were a semantic web data source.

**Overview**

The Resource Description Framework (RDF) is a widely used framework for modeling and exchanging data on the web. It provides a flexible and extensible data model that allows data to be represented as a directed graph, where nodes represent entities, and edges represent relationships between them. However, many data sources, such as relational databases, do not natively support RDF. This is where R2RML comes in.

The R2RML standard provides a way to map relational databases to RDF. It allows users to define mappings between the tables and columns in a relational database and RDF graphs. This enables the creation of virtual knowledge graphs from existing relational databases. The R2RML standard defines a set of rules for mapping relational data to RDF, such as the use of SQL queries to retrieve data, and the mapping of columns to RDF properties.

The Python library that we are presenting in this documentation extends the popular RDF library ``rdflib``, providing an implementation of the R2RML standard. The library allows users to generate a virtual knowledge graph from a relational database, providing a simple and easy-to-use interface for querying the data. Additionally, the library provides a query rewriting functionality that allows users to write SPARQL queries and have them automatically rewritten to SQL queries, optimizing query execution for large datasets.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
