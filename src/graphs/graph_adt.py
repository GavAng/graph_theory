from abc import ABC, ABCMeta, abstractmethod


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


class GraphAdtMetaclass(ABCMeta):
    def __new__(cls, name, bases, attributes, *, has_mutable_vertices: bool = False, has_mutable_edges: bool = False):

        bases = list(bases)

        if has_mutable_vertices:
            bases.append(MutableVerticesGraphAdt)

        if has_mutable_edges:
            bases.append(MutableEdgesGraphAdt)

        return super().__new__(cls, name, tuple(bases), attributes)


class GraphAdt(metaclass=GraphAdtMetaclass, has_mutable_edges=True):
    @property
    @abstractmethod
    def n_vertices(self) -> int: ...

    @property
    @abstractmethod
    def n_edges(self) -> int: ...
