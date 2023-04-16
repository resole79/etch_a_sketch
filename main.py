import turtle
from turtle import Turtle, Screen
from random import randint

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(5)
turtle.colormode(255)

def rando_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tommy.color(r, g, b)


def go_forward():
    rando_color()
    tommy.forward(10)


def go_backward():
    rando_color()
    tommy.backward(10)


def go_left():
    rando_color()
    tommy.left(10)


def go_right():
    rando_color()
    tommy.right(10)


def clear():
    tommy.penup()
    tommy.home()
    tommy.clear()


screen = Screen()
screen.listen()
screen.onkey(go_backward, "Left")
screen.onkey(go_forward, "Right")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
