from turtle import Turtle
from random import randint

SIZE = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(SIZE, SIZE)
        self.penup()
        self.change_location()
        self.speed("fastest")

    def check_on_snake(self, segments_list):
        for segment in segments_list:
            if self.distance(segment) <= 15:
                return True
        return False

    def change_location(self):
        self.goto(randint(-280, 280), randint(-280, 280))



