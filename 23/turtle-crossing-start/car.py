from turtle import Turtle
from random import randint

XRANGE = (-300, 300)
YRANGE = (-250, 250)

class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.x_pos = randint(XRANGE[0], XRANGE[1])
        self.y_pos = randint(YRANGE[0], YRANGE[1])
        self.penup()
        self.goto(self.x_pos, self.y_pos)
