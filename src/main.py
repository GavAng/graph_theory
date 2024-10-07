from draw_tools import TurtleDraw
from graphs.hash_graph import HashGraph
from pprint import pprint

V = {0, 1.1, 2, 3}
E = {(0, 1.1), (1.1, 3)}
G = HashGraph[float](V, E)
G.add_vertex(-5.5)
G.add_edge(-5.5, 3)

print(G.vertices)
print(G.edges)
pprint(G._adjacency_list)

t = TurtleDraw(G)
t.draw()
