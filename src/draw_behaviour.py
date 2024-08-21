from abc import ABC, abstractmethod
from turtle import Screen, Turtle

from graphs.graph_adt import BaseGraphAdt
from utils.typings import Point2d, Vertex


class DrawBehaviour(ABC):
    def __init__(self, graph: BaseGraphAdt, *, labelled: bool = False) -> None:
        self._graph = graph
        self._labelled = labelled

    @abstractmethod
    def draw(cls, graph: BaseGraphAdt) -> None: ...


class TurtleDraw(DrawBehaviour):
    def __init__(self, graph: BaseGraphAdt, labelled: bool = False, center: Point2d = (0, 0)) -> None:
        super().__init__(graph, labelled=labelled)
        self._turtle = Turtle(visible=False)
        self._center = center

    def draw(self, **kwargs) -> None:
        window = Screen()
        window.tracer(0)

        vertex_positions = self._draw_vertices(**kwargs)
        self._draw_edges(vertex_positions)

        window.update()
        window.mainloop()

    def _draw_vertices(self, *, angle: int = 0, radius: int = 200) -> dict[Vertex, Point2d]:
        vertex_positions = {}

        exterior_angle = 360 / self._graph.n_vertices
        font_size = int(100 / self._graph.n_vertices**0.5)

        self._turtle.up()
        self._turtle.goto(*self._center)
        self._turtle.left(90 - angle)
        for v in self._graph.vertices:
            self._turtle.forward(radius)

            vertex_positions[v] = self._turtle.pos()

            if self._labelled:
                self._turtle.write(v, align="center", font=("Arial", font_size, "normal"))
            self.draw_point(self._turtle.pos(), radius=10)

            self._turtle.goto(*self._center)
            self._turtle.right(exterior_angle)

        return vertex_positions

    def _draw_edges(self, vertex_positions: dict[Vertex, Point2d]) -> None:
        self._turtle.width(5)

        for v_1, v_2 in self._graph.edges:
            self._turtle.up()
            self._turtle.goto(vertex_positions[v_1])
            self._turtle.down()
            self._turtle.goto(vertex_positions[v_2])

    def draw_point(self, center_pos: Point2d, *, radius: int = 5) -> None:
        self._turtle.up()
        self._turtle.goto(center_pos[0], center_pos[1] - radius)

        self._turtle.fillcolor("black")
        self._turtle.begin_fill()
        self._turtle.circle(radius)
        self._turtle.end_fill()
