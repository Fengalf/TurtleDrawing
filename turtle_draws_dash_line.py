from turtle import Turtle, Screen


def draw_dash_line():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color("purple")

    for _ in range(50):
        donatello.forward(10)
        donatello.penup()
        donatello.forward(10)
        donatello.pendown()

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    draw_dash_line()
