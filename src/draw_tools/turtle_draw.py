import turtle
from draw_tools.base_draw import DrawBehaviour
from graphs.graph_adt import BaseGraphAdt
from utils.typings import Point2d, Vertex


class TurtleDraw(DrawBehaviour):
    def __init__(self, graph: BaseGraphAdt, *, labelled: bool = True, center: Point2d = (0, 0)) -> None:
        super().__init__(graph, labelled=labelled)
        self._screen = turtle.Screen()
        self._turtle = turtle.Turtle(visible=False)
        self._center = center

        self._screen.tracer(0)

    def draw(self, **kwargs) -> None:
        vertex_positions = self._draw_vertices(**kwargs)
        self._draw_edges(vertex_positions)

        self._screen.update()
        self._screen.mainloop()

    def _draw_vertices(self, *, angle: int = 0, radius: int = 200) -> dict[Vertex, Point2d]:
        vertex_positions = {}

        exterior_angle = 360 / self._graph.n_vertices
        font_size = int(50 / self._graph.n_vertices**0.5)

        self._turtle.penup()
        self._turtle.left(90 - angle)
        for v in self._graph.vertices:
            self._turtle.goto(*self._center)
            self._turtle.forward(radius)

            vertex_positions[v] = self._turtle.pos()
            self._turtle.dot(15)

            if self._labelled:
                self._turtle.write(v, align="center", font=("Arial", font_size, "normal"))

            self._turtle.right(exterior_angle)

        return vertex_positions

    def _draw_edges(self, vertex_positions: dict[Vertex, Point2d]) -> None:
        self._turtle.width(5)

        for v_1, v_2 in self._graph.edges:
            self._turtle.penup()
            self._turtle.goto(vertex_positions[v_1])
            self._turtle.pendown()
            self._turtle.goto(vertex_positions[v_2])
