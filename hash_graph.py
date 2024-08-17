from draw_behaviour import DrawBehaviour, TurtleDraw
from numpy import ndarray, sum as numpy_sum, zeros
from typing import Type, Hashable


class HashGraph:
    """
    An undirected simple graph data structure. Vertices can be any (hashable) type.
    """

    def __init__(self, *, adjacency_matrix: ndarray, draw_behaviour: Type[DrawBehaviour] = TurtleDraw):
        n_dimensions, shape = adjacency_matrix.ndim, adjacency_matrix.shape
        if n_dimensions != 2 or shape != (n_vertices := shape[0], n_vertices):
            raise ValueError("adjacency matrix must be a square matrix")
        self.adjacency_matrix = adjacency_matrix
        self.draw_behaviour = draw_behaviour(self)

    @staticmethod
    def by_lists(vertex_list: list[Hashable], edge_list: list[tuple[Hashable, Hashable]]):
        """
        Creates a graph from a vertex and edge list.
        """

    def get_n_vertices(self):
        return self.adjacency_matrix.shape[0]

    def get_n_edges(self):
        return numpy_sum(self.adjacency_matrix) // 2

    def add_vertex(vertex_label: Hashable):
        pass

    def add_edge(edge: tuple[Hashable, Hashable]):
        pass

    def draw(self):
        self.draw_behaviour.draw()
