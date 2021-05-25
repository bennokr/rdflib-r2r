"""
rdflib_vkg.types
=======================
All commons types found in the rdflib_vkg package
"""
from typing import Optional, Set, Tuple, Union, Any, NamedTuple
from rdflib import Literal, URIRef, Variable
from sqlalchemy.engine import Engine

Term = Union[URIRef, Literal]
Triple = Tuple[Term, Term, Term]