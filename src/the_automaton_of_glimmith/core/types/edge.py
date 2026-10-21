"""
This file defines an enum for the possible edge states of any given edge from glimmith (active, inactive, active<size_diff(x)>, active<ineq>...)
"""
from dataclasses import dataclass
from enum import IntFlag, IntEnum


@dataclass
class Inactive():
    pass


@dataclass
class Active():
    pass


# gemini and delta are the same kind of constraint but negated
@dataclass
class Shape(IntFlag):
    Gemini = 0
    Delta = 1

# inequality constraint represented as X less than, where X is the enum value below
@dataclass
class Ineq(IntEnum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

#the size difference constraint has an arbitrary int value in principle
@dataclass
class Diff():
    value: int


Edge = Inactive | Active | Shape | Ineq | Diff


