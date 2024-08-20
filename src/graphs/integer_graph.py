from draw_behaviour import DrawBehaviour, TurtleDraw
from graphs.graph_adt import GraphAdt
import numpy as np
from numpy import int8, zeros
from typing import Type


class IntegerGraph(GraphAdt, has_mutable_vertices=True, has_mutable_edges=True):
    """
    An undirected simple graph data structure. Vertices will be integers starting at 0.
    """

    def __init__(self, *, adjacency_matrix: np.ndarray, draw_behaviour: Type[DrawBehaviour] = TurtleDraw) -> None:
        n_dimensions, shape = adjacency_matrix.ndim, adjacency_matrix.shape
        if n_dimensions != 2 or shape != (n_vertices := shape[0], n_vertices):
            raise ValueError("adjacency matrix must be a square matrix")
        if not np.array_equal(adjacency_matrix.T, adjacency_matrix):
            raise ValueError("Undirected graphs must have a symmetric adjacency matrix.")
        self.adjacency_matrix = adjacency_matrix
        self.draw_behaviour = draw_behaviour(self)

    def __repr__(self) -> str:
        # return f"{' '.join(map(str, range(self.n_vertices)))}\n{'\n'.join(
        #     f'{str(i)} {" ".join(map(str, self.adjacency_matrix[i, :i]))}' for i in range(self.n_vertices)
        # )}"
        return str(self.adjacency_matrix)

    @classmethod
    def by_n_vertices(cls, n_vertices: int) -> "IntegerGraph":
        return cls(adjacency_matrix=zeros(shape=(n_vertices, n_vertices), dtype=int8))

    @property
    def n_vertices(self) -> int:
        return self.adjacency_matrix.shape[0]

    @property
    def n_edges(self) -> int:
        return int(np.sum(self.adjacency_matrix) / 2)

    def add_vertex(self) -> None:
        zero_column = zeros((self.n_vertices, 1), dtype=int8)
        zero_row = zeros((1, self.n_vertices + 1), dtype=int8)
        self.adjacency_matrix = np.hstack((self.adjacency_matrix, zero_column))
        self.adjacency_matrix = np.vstack((self.adjacency_matrix, zero_row))

    def remove_vertex(self, v: int) -> None:
        """
        Warning: removing a vertex will decrement the integer label of vertices 'greater' than it.
        """
        if v <= -1 or self.n_vertices <= v:
            raise ValueError(f"Vertices in graph are in range(0, {self.n_vertices}).")
        self.adjacency_matrix = np.delete(self.adjacency_matrix, (v), axis=0)
        self.adjacency_matrix = np.delete(self.adjacency_matrix, (v), axis=1)

    def add_edge(self, v1: int, v2: int) -> None:
        if v1 == v2:
            raise ValueError("Simple graphs cannot contain an edge between the same vertex.")
        if min(v1, v1) <= -1 or self.n_vertices <= max(v1, v2):
            raise ValueError(f"Vertices in edge must be in range(0, {self.n_vertices}).")
        if self.adjacency_matrix[v1][v2]:
            raise ValueError(f"Edge ({v1}, {v2}) already exists.")
        self.adjacency_matrix[v1][v2] = 1
        self.adjacency_matrix[v2][v1] = 1

    def remove_edge(self, v1: int, v2: int) -> None:
        if min(v1, v1) <= -1 or self.n_vertices <= max(v1, v2):
            raise ValueError(f"Vertices in edge must be in range(0, {self.n_vertices}).")
        if not self.adjacency_matrix[v1][v2]:
            raise ValueError(f"Edge ({v1}, {v2}) does not exist.")
        self.adjacency_matrix[v1][v2] = 0
        self.adjacency_matrix[v2][v1] = 0

    def draw(self) -> None:
        self.draw_behaviour.draw()
