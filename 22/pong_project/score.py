from turtle import Turtle

RIGHTPOS = (80, 200)
LEFTPOS = (-80, 200)

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.value = 0
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        if position.lower() == "right":
            self.goto(RIGHTPOS)
        elif position.lower() == "left":
            self.goto(LEFTPOS)
        self.show_score()

    def increase_score(self):
        self.value += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.value}", move=False, align="center", font=('Courier', 80, 'normal'))

    def restart_round(self, ball, ):
        pass
