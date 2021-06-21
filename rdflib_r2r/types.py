"""
rdflib_vkg.types
=======================
All commons types found in the rdflib_vkg package
"""
from typing import Optional, Set, Tuple, Union, Any, NamedTuple
from rdflib import Literal, URIRef, Variable

Term = Union[URIRef, Literal]
Triple = Tuple[Term, Term, Term]