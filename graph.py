from draw_behaviour import DrawBehaviour, TurtleDraw
from numpy import array_equal, ndarray, sum as numpy_sum, transpose, zeros
from typing import Type


class Graph:
    """
    An undirected simple graph data structure. Vertices will be integers starting at 0.
    """

    def __init__(self, *, adjacency_matrix: ndarray, draw_behaviour: Type[DrawBehaviour] = TurtleDraw):
        n_dimensions, shape = adjacency_matrix.ndim, adjacency_matrix.shape
        if n_dimensions != 2 or shape != (n_vertices := shape[0], n_vertices):
            raise ValueError("adjacency matrix must be a square matrix")
        if not array_equal(transpose(adjacency_matrix), adjacency_matrix):
            raise ValueError("Undirected graphs must have a symmetric adjacency matrix.")
        self.adjacency_matrix = adjacency_matrix
        self.draw_behaviour = draw_behaviour(self)

    def __repr__(self):
        return str(self.adjacency_matrix)

    @staticmethod
    def by_n_vertices(n_vertices: int):
        """
        Creates a graph with a given number of vertices.
        """
        return Graph(adjacency_matrix=zeros(shape=(n_vertices, n_vertices)))

    def get_n_vertices(self):
        return self.adjacency_matrix.shape[0]

    def get_n_edges(self):
        return numpy_sum(self.adjacency_matrix) // 2

    def add_vertex(self):
        n_vertices = self.get_n_vertices()
        new_adjacency_matrix = zeros(shape=(n_vertices + 1, n_vertices + 1))
        new_adjacency_matrix[:-1, :-1] = self.adjacency_matrix
        self.adjacency_matrix = new_adjacency_matrix

    def add_edge(self, edge: tuple[int, int]):
        v1, v2 = edge[0], edge[1]
        if v1 == v2:
            raise ValueError("Simple graphs cannot contain an edge between the same vertex.")
        n_vertices = self.get_n_vertices()
        if min(v1, v1) <= -1 or n_vertices <= max(v1, v2):
            raise ValueError(f"Vertices in edge must be in range(0, {n_vertices}).")
        if self.adjacency_matrix[v1][v2]:
            raise ValueError(f"Edge {edge} already exists.")
        self.adjacency_matrix[v1][v2] = 1
        self.adjacency_matrix[v2][v1] = 1

    def draw(self):
        self.draw_behaviour.draw()
