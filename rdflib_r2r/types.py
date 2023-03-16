"""
All commons types found in the rdflib_r2r package
"""
from typing import Optional, Set, Tuple, Union, Any, NamedTuple
from rdflib import Literal, URIRef, Variable

AnyTerm = Union[URIRef, Literal]
Triple = Tuple[URIRef, URIRef, AnyTerm]
TriplePattern = Union[URIRef, Literal, Variable]
SearchQuery = Tuple[Optional[URIRef], Optional[URIRef], Optional[AnyTerm]]
BGP = Set[SearchQuery]