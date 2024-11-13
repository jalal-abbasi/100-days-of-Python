import turtle
from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_counterclockwise():
    tim.left(10)


def reset_screen():
    turtle.resetscreen()


screen = Screen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=reset_screen)
screen.listen()
screen.exitonclick()
