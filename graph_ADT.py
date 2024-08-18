from abc import ABC, abstractmethod


class GraphADT(ABC):

    @property
    @abstractmethod
    def n_vertices(self):
        pass

    @property
    @abstractmethod
    def n_edges(self):
        pass

    @abstractmethod
    def add_vertex(self):
        pass

    @abstractmethod
    def remove_vertex(self):
        pass

    @abstractmethod
    def add_edge(self):
        pass

    @abstractmethod
    def remove_edge(self):
        pass
