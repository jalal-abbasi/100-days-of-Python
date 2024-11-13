import turtle
from turtle import Turtle
from turtle import Screen
from random import randint
from random import random

# related to challenge 5


def generate_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


the_fucking_turtle = Turtle()
the_fucking_turtle.color("black")

# challenge 3
# for edge_number in range(3, 11):
#     the_fucking_turtle.pencolor(random(), random(), random())
#     for _ in range(edge_number):
#         the_fucking_turtle.down()
#         the_fucking_turtle.forward(100)
#         the_fucking_turtle.left(180-(180*(edge_number-2)/edge_number))

# challenge 4
# speed
# the_fucking_turtle.speed(9)
# # line size
# the_fucking_turtle.width(9)
# # random distance
# rand_turn = [90, 180, 270]
#
# while True:
#     the_fucking_turtle.pencolor(random(), random(), random())
#     the_fucking_turtle.forward(randint(1,100))
#     # random 90 degree turns to right-left
#     the_fucking_turtle.right(rand_turn[randint(0,1)])
#     the_fucking_turtle.showturtle()

# challenge 5
turtle.colormode(255)
for angle in range(0, 370, 10):
    the_fucking_turtle.pencolor(generate_color())
    the_fucking_turtle.speed("fastest")
    the_fucking_turtle.setheading(angle)
    the_fucking_turtle.circle(100)
    print(angle)





screen = Screen()
screen.exitonclick()




