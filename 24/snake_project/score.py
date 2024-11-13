from turtle import Turtle




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        with open("data.txt") as highest_score:
            self.highest_score = int(highest_score.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"score: {self.value}   Highest Score: {self.highest_score}", move=False, align="center", font=('Courier', 12, 'normal'))

    def update_score(self):
        self.value += 1
        self.clear()
        self.print_score()

    def reset_score(self):
        if self.value > self.highest_score:
            self.highest_score = self.value
            with open("data.txt", mode="w") as highest_score:
                highest_score.write(str(self.highest_score))
        self.value = 0
        self.print_score()


    # def print_gameover(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align="center", font=('Courier', 18, 'normal'))
