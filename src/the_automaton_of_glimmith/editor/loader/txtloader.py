from ..interfaces.maploader import MapLoader

from ...core.types import GlimmithMap
from pathlib import Path

"""
Load a glimmith map stored in txt
"""
class TxtLoader(MapLoader):

    # we should formalize map format somewhere, somehow
    def load(path: str | Path) -> GlimmithMap:
        pass