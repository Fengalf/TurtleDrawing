from turtle import Turtle, Screen


def draw_square():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color("purple")

    for _ in range(0, 4):
        donatello.forward(100)
        donatello.left(90)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    draw_square()
