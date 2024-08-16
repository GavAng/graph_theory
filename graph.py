import turtle


class Graph:
    def __init__(self, n_vertices, edges={}):
        self.n_vertices = n_vertices
        self.edges = edges

    def draw(self, *, labeled=False, angle=0, radius=200):
        wn = turtle.Screen()
        wn.tracer(0)

        vertex_positions = self.draw_vertices(
            labeled=labeled, angle=angle, radius=radius
        )
        self.draw_edges(vertex_positions)

        wn.update()
        wn.mainloop()

    def draw_vertices(self, *, labeled=False, angle=0, radius=200):
        import draw_tools

        vertex_positions = {}

        t = turtle.Turtle(visible=False)

        exterior_angle = 360 / self.n_vertices
        font_size = int(100 / self.n_vertices**0.5)

        t.up()
        t.left(90 - angle)
        for v_i in range(1, self.n_vertices + 1):
            t.forward(radius)

            vertex_positions[v_i] = t.pos()

            if labeled:
                t.write(v_i, align="center", font=("Arial", font_size, "normal"))
            draw_tools.draw_point(t.pos(), radius=10)

            t.goto(0, 0)
            t.right(exterior_angle)

        return vertex_positions

    def draw_edges(self, vertex_positions):
        t = turtle.Turtle(visible=False)

        for edge in self.edges:
            v1 = edge.get_endpoint()
            v2 = edge.get_adjacent(v1)
            t.up()
            t.goto(vertex_positions[v1])
            t.down()
            t.goto(vertex_positions[v2])
