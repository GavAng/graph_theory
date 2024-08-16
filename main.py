from graph import Graph
from complete_graph import K
from edge import Edge
from mutable_graph import MutableGraph

g = MutableGraph(5, {Edge(1, 2), Edge(3, 4), Edge(2, 5)})
# g.draw()
g.add_edge(Edge(4, 6))
g.draw()

# k = K(10)
# k.draw(labeled=True)
# g.draw(labeled=True)
