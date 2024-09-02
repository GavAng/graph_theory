from draw_behaviour import TurtleDraw
from graphs.hash_graph import HashGraph
from graphs.integer_graph import IntegerGraph

V = {0, 1.1, 2, 3}
E = {(0, 1.1), (1.1, 3)}
G = HashGraph[float](V, E)
G.add_vertex(-5.5)
G.add_edge(-5.5, 3)

print(G.vertices)
print(G.edges)

t = TurtleDraw(G)
t.draw()
