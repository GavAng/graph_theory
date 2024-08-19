from abc import ABC, abstractmethod


class GraphAdt(ABC):

    @property
    @abstractmethod
    def n_vertices(self) -> int: ...

    @property
    @abstractmethod
    def n_edges(self) -> int: ...

    def __init_subclass__(cls, *, has_mutable_vertices: bool = False, has_mutable_edges: bool = False) -> None:
        if has_mutable_vertices:

            @abstractmethod
            def add_vertex(self) -> None: ...

            @abstractmethod
            def remove_vertex(self) -> None: ...

            setattr(cls, add_vertex.__name__, add_vertex)
            setattr(cls, remove_vertex.__name__, remove_vertex)

        if has_mutable_edges:

            @abstractmethod
            def add_edge(self) -> None: ...

            @abstractmethod
            def remove_edge(self) -> None: ...

            setattr(cls, add_edge.__name__, add_edge)
            setattr(cls, remove_edge.__name__, remove_edge)
