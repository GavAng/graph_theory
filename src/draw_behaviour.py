from abc import ABC, abstractmethod
from draw_tools import draw_point
from graph_adt import GraphAdt
from turtle import Turtle, Screen
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from integer_graph import IntegerGraph


class DrawBehaviour(ABC):

    def __init__(self, graph: GraphAdt):
        self._graph = graph

    @abstractmethod
    def draw(self): ...


class TurtleDraw(DrawBehaviour):

    def draw(self, *, labelled=False, angle=0, radius=200):
        window = Screen()
        window.tracer(0)

        vertex_positions = self.draw_vertices(labelled=labelled, angle=angle, radius=radius)
        self.draw_edges(vertex_positions)

        window.update()
        window.mainloop()

    def draw_vertices(self, *, labelled=False, angle=0, radius=200):
        n_vertices = self._graph.n_vertices
        vertex_positions = {}

        t = Turtle(visible=False)

        exterior_angle = 360 / n_vertices
        font_size = int(100 / n_vertices**0.5)

        t.up()
        t.left(90 - angle)
        for v_i in range(1, n_vertices + 1):
            t.forward(radius)

            vertex_positions[v_i] = t.pos()

            if labelled:
                t.write(v_i, align="center", font=("Arial", font_size, "normal"))
            draw_point(t.pos(), radius=10)

            t.goto(0, 0)
            t.right(exterior_angle)

        return vertex_positions

    def draw_edges(self, vertex_positions):
        t = Turtle(visible=False)

        for edge in self.edges:
            v1 = edge.get_endpoint()
            v2 = edge.get_adjacent(v1)
            t.up()
            t.goto(vertex_positions[v1])
            t.down()
            t.goto(vertex_positions[v2])
