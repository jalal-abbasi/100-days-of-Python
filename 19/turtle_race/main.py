import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet", prompt="Which turtle do you want to bet? enter a color: ")
color_list = ["red", "green", "yellow", "blue", "purple", "orange"]



turtles_list = []
y_value = -100
for color in color_list:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_value)
    turtles_list.append(new_turtle)
    y_value = y_value + 50

is_finished = True
if user_bet:
    is_finished = False

while not is_finished:
    for turtle_item in turtles_list:
        turtle_item.forward(randint(5, 30))
        if turtle_item.pos()[0] >= 230:
            if turtle_item.color()[0] == user_bet:
                print(f"You won the bet!")
            else:
                print(f"The {turtle_item.color()[0]} turtle won. you lost the bet...")
            is_finished = True



screen.exitonclick()
