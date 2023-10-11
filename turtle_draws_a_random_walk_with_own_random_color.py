from turtle import Turtle, Screen
import random


def draw_random_way():

    screen = Screen()
    screen.colormode(255)

    donatello = Turtle()
    donatello.shape("turtle")
    donatello.speed(0)
    donatello.width(10)

    directions = [0, 90, 180, 270]
    for _ in range(200):
        random_rgb = [random.randint(0, 255) for _ in range(3)]
        donatello.color(tuple(random_rgb))
        donatello.forward(100)
        donatello.setheading(random.choice(directions))

    screen.exitonclick()


if __name__ == "__main__":
    draw_random_way()
