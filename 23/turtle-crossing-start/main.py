import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def check_collision(turtle, cars):
    for car in cars.car_list:
        distance = turtle.distance(car)
        # if turtle.ycor() - 20 < car.ycor() < turtle.ycor() + 20:
        #     if turtle.xcor() - 15 < car.xcor() < turtle.xcor() + 15:
        #         scoreboard.game_over()
        #         return False
        if distance <= 25:
            scoreboard.game_over()
            return False
    return True


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(key="Up", fun=player.move)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.reset_position():
        scoreboard.level_up()
        car_manager.speed_up()
    car_manager.move_cars()
    game_is_on = check_collision(player, car_manager)

screen.exitonclick()
