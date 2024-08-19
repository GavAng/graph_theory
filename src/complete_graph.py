import turtle
from graph_adt import GraphAdt


class CompleteGraph(GraphAdt, has_mutable_vertices=True, has_mutable_edges=False): ...


K = CompleteGraph
