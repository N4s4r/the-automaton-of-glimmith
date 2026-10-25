from abc import ABC, abstractmethod
from pathlib import Path

from ...core.types.map import GlimmithMap

"""
Something that can save and load a Glimmith Map
"""
class MapLoader(ABC):

    @abstractmethod
    def load(self, path: str | Path) -> GlimmithMap:
        ...


    @abstractmethod
    def save (self, map: GlimmithMap, path: str | Path) -> bool:
        ...
