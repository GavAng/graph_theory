from integer_graph import IntegerGraph

g = IntegerGraph.by_n_vertices(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 3)
print(g)
g.add_vertex()
print(g)
g.remove_vertex(2)
print(g)
g.remove_edge(2, 1)
print(g)
