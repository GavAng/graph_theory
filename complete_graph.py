import turtle
from graph import Graph


class CompleteGraph(Graph):
    def draw_edges(self, vertex_positions):
        t = turtle.Turtle(visible=False)

        for v_i in range(1, self.n_vertices + 1):
            for v_j in range(v_i + 1, self.n_vertices + 1):
                t.up()
                t.goto(vertex_positions[v_i])
                t.down()
                t.goto(vertex_positions[v_j])


K = CompleteGraph
