import turtle

import colorgram
import random
from turtle import Turtle
from turtle import Screen

turtle.colormode(255)

colors = colorgram.extract('download.jpg', 54)
print((len(colors)))
# colors : a list of color objects. each color object has a rgb attribute which is a tuple.
my_turtle = Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setposition(-400, -300)
my_turtle.speed("fastest")
for _ in range(10):
    for _ in range(10):
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
        rand_color_obj = random.choice(colors)
        rand_color = rand_color_obj.rgb
        print(rand_color)
        my_turtle.dot(20, rand_color)
    turtle_y_pos = my_turtle.pos()[1]
    my_turtle.penup()
    my_turtle.setposition(-400, turtle_y_pos+50)

screen = Screen()
screen.exitonclick()
