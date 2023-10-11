from turtle import Turtle, Screen
import random
import tkinter_colors


def draw_random_way():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color(random.choice(tkinter_colors.colors))
    donatello.speed(0)
    donatello.width(10)

    directions = [0, 90, 180, 270]
    for _ in range(200):
        donatello.forward(100)
        donatello.setheading(random.choice(directions))
        donatello.color(random.choice(tkinter_colors.colors))

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    draw_random_way()
