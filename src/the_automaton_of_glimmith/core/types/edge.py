"""
This file defines an enum for the possible edge states of any given edge from glimmith (active, inactive, active<size_diff(x)>, active<ineq>...)
"""
from dataclasses import dataclass

from enum import IntFlag, IntEnum


class EdgeType(IntEnum):
    Inactive = 0
    Active = 1

    Shape = 2   # gemini/delta
    Ineq = 3    # inequality constraint over edge
    Diff = 4    # size difference(x)


class ShapeConstraint(IntFlag):
    Gemini = 0
    Delta = 1


class Edge(IntFlag):
    pass


