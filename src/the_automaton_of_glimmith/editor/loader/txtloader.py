from pathlib import Path

from ...core.types.map import GlimmithMap
from ..interfaces.maploader import MapLoader

"""
Load a glimmith map stored in txt
"""
class TxtLoader(MapLoader):

    # we should formalize map format somewhere, somehow
    def load(self, path: str | Path) -> GlimmithMap:
        pass
