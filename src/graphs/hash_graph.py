import numpy as np
from numpy import zeros

from graphs.graph_adt import BaseGraphAdt, MutableEdgesGraphAdt, MutableVerticesGraphAdt
from utils.typings import Vertex


class HashGraph(BaseGraphAdt, MutableVerticesGraphAdt, MutableEdgesGraphAdt):
    """
    An undirected simple graph data structure. Vertices can be any (hashable) type.
    """

    def __init__(self, *, adjacency_matrix: np.ndarray):
        n_dimensions, shape = adjacency_matrix.ndim, adjacency_matrix.shape
        if n_dimensions != 2 or shape != (n_vertices := shape[0], n_vertices):
            raise ValueError("adjacency matrix must be a square matrix")
        self.adjacency_matrix = adjacency_matrix

    @staticmethod
    def by_lists(vertex_list: list[Vertex], edge_list: list[tuple[Vertex, Vertex]]):
        """
        Creates a graph from a vertex and edge list.
        """

    def get_n_vertices(self):
        return self.adjacency_matrix.shape[0]

    def get_n_edges(self):
        return np.sum(self.adjacency_matrix) // 2

    def add_vertex(self, v: Vertex): ...

    def add_edge(self, v_1: Vertex, v_2: Vertex): ...
