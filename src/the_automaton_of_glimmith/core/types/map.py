from .cell import Cell
from .edge import Edge
from .rules import Rules
from .shape import Shape
from .vertex import Vertex

MatrixDataType = Cell | Edge | Vertex


class GlimmithMap:

    map: list[list[MatrixDataType]]

    global_rules: Rules

    shapes: list[Shape] | None

    pass
