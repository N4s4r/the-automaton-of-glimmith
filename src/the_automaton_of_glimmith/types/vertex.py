"""
This file defines an enum for the possible vertex states of any given vertex from glimmith (inactive, active<watchtower(x)>)
"""

from enum import IntEnum

class Vertex(IntEnum):
    Inactive = 0
    WTOne = 1
    WTTwo = 2
    WTThree = 3
    WTFour = 4
