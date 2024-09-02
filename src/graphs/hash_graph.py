from collections import defaultdict
from typing import Generic, TypeVar

from graphs.graph_adt import BaseGraphAdt, MutableEdgesGraphAdt, MutableVerticesGraphAdt
from utils.typings import Vertex, Edge

VertexT = TypeVar("VertexT", bound=Vertex)  # change for square brackets once Pylance updates
EdgeT = Edge[VertexT]


class HashGraph(Generic[VertexT], BaseGraphAdt, MutableVerticesGraphAdt, MutableEdgesGraphAdt):
    """
    An undirected simple graph data structure. Vertices can be any (hashable) type.
    """

    def __init__(self, vertices: set[VertexT] = set(), edges: set[EdgeT] = set()) -> None:
        self._adjacency_list: dict[VertexT, set[VertexT]] = {}
        for v in vertices:
            self._adjacency_list[v] = set()
        for v_1, v_2 in edges:
            if v_1 in vertices and v_2 in vertices:
                self._adjacency_list[v_1].add(v_2)
                self._adjacency_list[v_2].add(v_1)
            else:
                raise ValueError(f"Vertex {v_1} or {v_2} not in given Vertex set.")

    @property
    def n_vertices(self) -> int:
        return len(self.vertices)

    @property
    def n_edges(self) -> int:
        return sum(len(edges) for edges in self._adjacency_list.values()) // 2

    @property
    def vertices(self) -> set[VertexT]:
        return set(self._adjacency_list)

    @property
    def edges(self) -> set[EdgeT]:
        edges = set()
        for v, neighbourhood in self._adjacency_list.items():
            for v_adjacent in neighbourhood:
                if (v_adjacent, v) not in edges:
                    edges.add((v, v_adjacent))
        return edges

    def add_vertex(self, v: VertexT, /) -> None:
        if v in self.vertices:
            raise ValueError(f"Vertex {v} already in graph.")
        self._adjacency_list[v] = set()

    def remove_vertex(self, v: VertexT, /) -> None:
        if v not in self.vertices:
            raise ValueError(f"Vertex {v} not in graph.")
        self._adjacency_list.pop(v)

    def add_edge(self, v_1: VertexT, v_2: VertexT, /) -> None:
        if v_1 == v_2:
            raise ValueError("Simple graphs cannot contain an Edge between the same Vertex.")
        if v_1 not in self.vertices or v_2 not in self.vertices:
            raise ValueError(f"Vertex {v_1} or {v_2} not in graph.")
        if v_1 in self._adjacency_list[v_2]:
            raise ValueError(f"Edge ({v_1}, {v_2}) already in graph.")
        self._adjacency_list[v_1].add(v_2)
        self._adjacency_list[v_2].add(v_1)

    def remove_edge(self, v_1: VertexT, v_2: VertexT, /) -> None:
        if v_1 not in self.vertices or v_2 not in self.vertices:
            raise ValueError(f"VertexT {v_1} or {v_2} not in graph.")
        if v_1 not in self._adjacency_list[v_2]:
            raise ValueError(f"Edge ({v_1}, {v_2}) not in graph.")
        self._adjacency_list[v_1].remove(v_2)
        self._adjacency_list[v_2].remove(v_1)
