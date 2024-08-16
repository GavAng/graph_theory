import turtle


def draw_point(center_pos, *, radius=5):
    t = turtle.Turtle()
    t.hideturtle()

    t.up()
    t.goto(center_pos[0], center_pos[1] - radius)

    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
