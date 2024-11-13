from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pace = 10
        self.y_pace = 10
        self.ball_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.x_pace
        y_position = self.ycor() + self.y_pace
        self.goto(x_position, y_position)

    def hit_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_pace *= -1

    def hit_paddle(self, paddle):
        if paddle.ycor() - 50 <= self.ycor() <= paddle.ycor() + 50:
            if (self.xcor() <= -330) or (330 <= self.xcor()):
                self.x_pace *= -1

        #
        # elif (paddle.ycor() - 65 < self.ycor() < paddle.ycor() - 50) or (paddle.ycor() + 50 < self.ycor() < paddle.ycor() + 65):
        #     if -360 <= self.xcor() <= -340 or 340 <= self.xcor() <= 360:
        #         self.y_pace *= -1


    def reset_position(self):
        self.ball_speed *= 0.9
        self.goto(0, 0)
        self.x_pace *= -1
    # def move(self):
    #     self.forward(30)
    #     current_pos = self.pos()
    #     current_heading = self.heading()
    #     if current_pos[1] > 280 or current_pos[1] < -280:
    #         if current_heading == 45 or current_heading == 225:
    #             self.right(90)
    #         else:
    #             self.left(90)





