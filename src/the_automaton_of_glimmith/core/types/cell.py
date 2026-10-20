"""
This file defines an enum for the possible cell states of any given cell from glimmith (active, inactive, active<rose(x)>, active<compass(x)>)
"""

from dataclasses import dataclass
from enum import IntEnum

# inactive
# active
# rose windows
# area number
# palisade
# polynomio :(
# compass


@dataclass
class Inactive:
    pass


@dataclass
class Active:
    pass


@dataclass
class Rose():
    # in practice we only see up to 5 types but in theory there can be more
    type: int


@dataclass
class Area():
    size: int


@dataclass
class Palisade(IntEnum):
    Empty = 0
    One = 1
    Corner = 2
    Hallway = 3
    End = 4
    Full = 5


# TODO: Implement shape class to define a polynomio
@dataclass
class Polynomio():
    # uhh
    pass


@dataclass
class Compass():
    N: int | None
    S: int | None
    E: int | None
    W: int | None


Cell = Inactive | Active | Rose | Area | Palisade | Polynomio | Compass