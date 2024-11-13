import turtle
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# STARTING_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def increase_length(self):
        self.add_segment(self.snake_body[-1].pos())

    # def increase_length(self):
    #     head_pos = self.head.pos()
    #     head_heading = self.head.heading()
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.setheading(head_heading)
    #     if head_heading == UP:
    #         new_segment.goto(head_pos[0], head_pos[1] + 20)
    #     elif head_heading == DOWN:
    #         new_segment.goto(head_pos[0], head_pos[1] - 20)
    #     elif head_heading == RIGHT:
    #         new_segment.goto(head_pos[0] + 20, head_pos[1])
    #     else:
    #         new_segment.goto(head_pos[0] - 20, head_pos[1])
    #     self.head = new_segment
    #     self.snake_body = [new_segment] + self.snake_body

    def move(self):
        num_segments = len(self.snake_body)
        for index in range(num_segments-1, 0, -1):
            xcor = self.snake_body[index - 1].xcor()
            ycor = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def is_hitting_food(self, food):
        distance = self.head.distance(food)
        if distance <= 15:
            return True
        else:
            return False

    def is_hitting_itself(self):
        for segment in self.snake_body[1:]:
            distance = self.head.distance(segment)
            if distance < 15:
                return True
        return False

