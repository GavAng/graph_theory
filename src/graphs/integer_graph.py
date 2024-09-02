import numpy as np
from numpy import int8, zeros
from typing import Self

from graphs.graph_adt import BaseGraphAdt, MutableEdgesGraphAdt, MutableVerticesGraphAdt


class IntegerGraph(BaseGraphAdt, MutableVerticesGraphAdt, MutableEdgesGraphAdt):
    """
    An undirected simple graph data structure. Vertices will be integers starting at 0. Not as simple as HashGraph[int].
    """

    def __init__(self, *, adjacency_matrix: np.ndarray) -> None:
        n_dimensions, shape = adjacency_matrix.ndim, adjacency_matrix.shape
        if n_dimensions != 2 or shape != (n_vertices := shape[0], n_vertices):
            raise ValueError("adjacency matrix must be a square matrix")
        if not np.array_equal(adjacency_matrix.T, adjacency_matrix):
            raise ValueError("Undirected graphs must have a symmetric adjacency matrix.")
        self._adjacency_matrix = adjacency_matrix

    def __repr__(self) -> str:
        return f"  {" ".join(map(str, range(self.n_vertices)))}\n{
            "\n".join(f"{str(i)} {" ".join(map(str, self._adjacency_matrix[i, :i]))}" 
                      for i in range(self.n_vertices)
                      )}"

    @classmethod
    def by_n_vertices(cls, n_vertices: int) -> Self:
        return cls(adjacency_matrix=zeros(shape=(n_vertices, n_vertices), dtype=int8))

    @property
    def n_vertices(self) -> int:
        return self._adjacency_matrix.shape[0]

    @property
    def n_edges(self) -> int:
        return int(np.sum(self._adjacency_matrix) / 2)

    @property
    def vertices(self) -> set[int]:
        return set(range(self.n_vertices))

    @property
    def edges(self) -> set[tuple[int, int]]:
        edges = set()
        for i in range(1, self.n_vertices):
            for j in range(i):
                if self._adjacency_matrix[i][j]:
                    edges.add((i, j))
        return edges

    def add_vertex(self) -> None:
        zero_column = zeros((self.n_vertices, 1), dtype=int8)
        zero_row = zeros((1, self.n_vertices + 1), dtype=int8)
        self._adjacency_matrix = np.hstack((self._adjacency_matrix, zero_column))
        self._adjacency_matrix = np.vstack((self._adjacency_matrix, zero_row))

    def remove_vertex(self, v: int) -> None:
        """
        Warning: removing a vertex will decrement the integer label of vertices 'greater' than it.
        """
        if v <= -1 or self.n_vertices <= v:
            raise ValueError(f"Vertices in graph are in range(0, {self.n_vertices}).")
        self._adjacency_matrix = np.delete(self._adjacency_matrix, v, axis=0)
        self._adjacency_matrix = np.delete(self._adjacency_matrix, v, axis=1)

    def add_edge(self, v_1: int, v_2: int) -> None:
        if v_1 == v_2:
            raise ValueError("Simple graphs cannot contain an edge between the same vertex.")
        if min(v_1, v_2) <= -1 or self.n_vertices <= max(v_1, v_2):
            raise ValueError(f"Vertices in graph must be in range(0, {self.n_vertices}).")
        if self._adjacency_matrix[v_1][v_2]:
            raise ValueError(f"Edge ({v_1}, {v_2}) already exists.")
        self._adjacency_matrix[v_1][v_2] = 1
        self._adjacency_matrix[v_2][v_1] = 1

    def remove_edge(self, v_1: int, v_2: int) -> None:
        if min(v_1, v_2) <= -1 or self.n_vertices <= max(v_1, v_2):
            raise ValueError(f"Vertices in graph must be in range(0, {self.n_vertices}).")
        if not self._adjacency_matrix[v_1][v_2]:
            raise ValueError(f"Edge ({v_1}, {v_2}) does not exist.")
        self._adjacency_matrix[v_1][v_2] = 0
        self._adjacency_matrix[v_2][v_1] = 0
