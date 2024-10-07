import turtle
from abc import ABC, abstractmethod

from graphs.graph_adt import BaseGraphAdt
from utils.typings import Point2d, Vertex


class DrawBehaviour(ABC):
    def __init__(self, graph: BaseGraphAdt, *, labelled: bool = False) -> None:
        self._graph = graph
        self._labelled = labelled

    @abstractmethod
    def draw(cls, graph: BaseGraphAdt, positions: dict[Vertex, Point2d] = {}) -> None: ...
