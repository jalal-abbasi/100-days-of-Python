from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.print_score()

    def print_score(self):
        self.write(f"score: {self.value}", move=False, align="center", font=('Courier', 12, 'normal'))

    def update_score(self):
        self.value += 1
        self.clear()
        self.print_score()

    def print_gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=('Courier', 18, 'normal'))
