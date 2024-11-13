from turtle import Turtle

RIGHT_X_POSITION = 350
LEFT_X_POSITION = -350


class Paddle(Turtle):
    def __init__(self, right_or_left):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        right_or_left = right_or_left.lower()
        if right_or_left == "right":
            self.goto(RIGHT_X_POSITION, 0)
        elif right_or_left == "left":
            self.goto(LEFT_X_POSITION, 0)

    def move_up(self):
        current_y = self.ycor()
        self.sety(current_y+20)

    def move_down(self):
        current_y = self.ycor()
        self.sety(current_y-20)


