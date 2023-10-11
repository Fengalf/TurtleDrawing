from turtle import Turtle, Screen
import random
import colorgram


def draw_spotty_image(img="image.jpg"):
    color_picker = colorgram.extract(img, 10)

    screen = Screen()
    screen.colormode(255)
    canv_width = screen.canvwidth
    canv_heigth = screen.canvheight
    screen.setworldcoordinates(-1, -1, screen.window_width() -
                               1, screen.window_height() - 1)

    donatello = Turtle()
    donatello.shape("turtle")
    donatello.speed(0)

    move = 50
    spot_size = 20

    rows = 10
    columns = 10

    donatello.penup()
    turn_left = True
    for col in range(columns):
        for _ in range(rows):
            donatello.color(random.choice(color_picker).rgb)
            donatello.dot(spot_size)
            donatello.forward(move)
        if turn_left:
            donatello.left(90)
            donatello.forward(move)
            donatello.left(90)
            turn_left = False
        elif col < columns-1:
            donatello.right(90)
            donatello.forward(move)
            donatello.right(90)
            turn_left = True

    #     donatello.pendown()

    screen.exitonclick()


if __name__ == "__main__":
    draw_spotty_image()
