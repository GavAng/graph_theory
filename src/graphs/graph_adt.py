from abc import ABC, abstractmethod
from typing import Self

from utils.typings import Edge, Vertex


class BaseGraphAdt(ABC):
    @property
    @abstractmethod
    def n_vertices(self) -> int: ...

    @property
    @abstractmethod
    def n_edges(self) -> int: ...

    @property
    @abstractmethod
    def vertices(self) -> set[Vertex]: ...

    @property
    @abstractmethod
    def edges(self) -> set[Edge]: ...

    # @abstractmethod
    # def __or__(self, other: Self) -> Self: ...

    # @abstractmethod
    # def __ior__(self, other: Self) -> Self:
    #   return self | other


class MutableVerticesGraphAdt(ABC):
    @abstractmethod
    def add_vertex(self) -> None: ...

    @abstractmethod
    def remove_vertex(self) -> None: ...


class MutableEdgesGraphAdt(ABC):
    @abstractmethod
    def add_edge(self) -> None: ...

    @abstractmethod
    def remove_edge(self) -> None: ...
