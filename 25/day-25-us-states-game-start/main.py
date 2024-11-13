from turtle import Turtle
from turtle import Screen
import pandas
from tkinter.simpledialog import askstring


states_data = pandas.read_csv("50_states.csv")
states_names = states_data.state.tolist()

game_screen = Screen()
game_screen.bgpic("blank_states_img.gif")
index = 0

for item in range(50):
    entered_name = askstring(f"{index}/50 States Correct", "What is the other state's name?").capitalize()
    if entered_name in states_names:
        state_x_pos = states_data[states_data.state == entered_name]["x"].tolist()[0]
        state_y_pos = states_data[states_data.state == entered_name]["y"].tolist()[0]
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.setx(state_x_pos)
        new_turtle.sety(state_y_pos)
        new_turtle.write(entered_name, align="center")
        index +=1



game_screen.exitonclick()

