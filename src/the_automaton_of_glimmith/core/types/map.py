from .cell import Cell
from .edge import Edge
from .vertex import Vertex
from .rules import Rules
from .shape import Shape

from typing import List

MatrixDataType = Cell | Edge | Vertex


class GlimmithMap():

    map: List[List[MatrixDataType]]

    global_rules: Rules

    shapes: List[Shape] | None

    pass