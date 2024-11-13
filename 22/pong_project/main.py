from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from wall import Wall
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
score_r = Score("right")
score_l = Score("left")
wall = Wall(-300)
while wall.ypos < 400:
    wall = Wall(wall.increment_y())

screen.listen()
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')

screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')

is_game_on = True

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    ball.hit_wall()
    ball.hit_paddle(right_paddle)
    ball.hit_paddle(left_paddle)

    if ball.xcor() > 410:
        score_l.increase_score()
        ball.reset_position()
    elif ball.xcor() < -410:
        score_r.increase_score()
        ball.reset_position()

screen.exitonclick()




