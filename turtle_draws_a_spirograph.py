from turtle import Turtle, Screen
import random


def draw_random_way():

    screen = Screen()
    screen.colormode(255)

    donatello = Turtle()
    donatello.shape("turtle")
    donatello.speed(0)
    angle = 4
    for _ in range(int(360/angle)):
        random_rgb = [random.randint(0, 255) for _ in range(3)]
        donatello.color(tuple(random_rgb))
        donatello.circle(100)
        donatello.left(angle)

    screen.exitonclick()


if __name__ == "__main__":
    draw_random_way()
