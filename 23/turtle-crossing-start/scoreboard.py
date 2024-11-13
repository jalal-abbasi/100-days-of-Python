from turtle import Turtle
FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(TEXT_POSITION)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level : {self.score}", move=False, align="Left", font=FONT)

    def level_up(self):
        self.score += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="Center", font=FONT)
