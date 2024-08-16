from edge import Edge
from graph import Graph


class MutableGraph(Graph):
    def add_edge(self, edge: Edge):
        if max(edge) <= self.n_vertices:
            self.edges.add(edge)
        else:
            raise ValueError(
                f"edge references vertex {max(edge)}, graph contains largest vertex {self.n_vertices}"
            )

    # def remove_edge(self, edge):
