from turtle import Turtle, Screen
import random
import tkinter_colors


def draw_n_gons():
    donatello = Turtle()
    donatello.shape("turtle")
    donatello.color(random.choice(tkinter_colors.colors))

    sides = 3
    for _ in range(8):
        angle = 360/sides
        for __ in range(sides):
            donatello.forward(100)
            donatello.left(angle)
        sides += 1
        donatello.color(random.choice(tkinter_colors.colors))

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    draw_n_gons()
