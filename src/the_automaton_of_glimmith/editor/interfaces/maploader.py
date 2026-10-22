from abc import ABC, abstractmethod
from pathlib import Path

from ..types.map import GlimmithMap


"""
Something that can save and load a Glimmith Map
"""
class MapLoader(ABC):

    @abstractmethod
    def load(path: str | Path) -> GlimmithMap:
        ...


    @abstractmethod
    def save (map: GlimmithMap, path: str | Path) -> bool:
        ...
