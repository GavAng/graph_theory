from abc import ABCMeta, abstractmethod


class GraphAdtMetaclass(ABCMeta):
    def __new__(cls, name, bases, attributes, *, has_mutable_vertices: bool, has_mutable_edges: bool):

        if has_mutable_vertices:

            @abstractmethod
            def add_vertex(self): ...

            @abstractmethod
            def remove_vertex(self): ...

            attributes |= {"add_vertex": add_vertex, "remove_vertex": remove_vertex}

        if has_mutable_edges:

            @abstractmethod
            def add_edge(self): ...

            @abstractmethod
            def remove_edge(self): ...

            attributes |= {"add_edge": add_edge, "remove_edge": remove_edge}

        return super().__new__(cls, name, bases, attributes)


class GraphAdt(metaclass=GraphAdtMetaclass, has_mutable_vertices=True, has_mutable_edges=True):

    @property
    @abstractmethod
    def n_vertices(self): ...

    @property
    @abstractmethod
    def n_edges(self): ...
