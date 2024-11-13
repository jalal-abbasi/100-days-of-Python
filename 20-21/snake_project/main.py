from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# def is_hitting(head_pos, food_pos):
#     """ function two check if the food and the head is hitting without using the distance method of turtle module"""
#     xfood = food_pos[0]
#     yfood = food_pos[1]
#
#     xhead = head_pos[0]
#     yhead = head_pos[1]
#
#     if (xhead-15 < xfood < xhead+15) and (yhead-15 < yfood < yhead+15):
#         return True
#     else:
#         return False


def is_game_over():
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.print_gameover()
        return True
    elif snake.is_hitting_itself():
        score.print_gameover()
        return True


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)

food = Food()
score = Score()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    is_game_on = not is_game_over()
    head_position = snake.head.pos()
    food_position = food.pos()

    # if is_hitting(head_position, food_position):
    #     food.hideturtle()
    #     food = Food()
    #     while food.check_on_snake(snake.snake_body):
    #         food.hideturtle()
    #         food = Food()
    #     snake.increase_length()

    if snake.is_hitting_food(food):
        score.update_score()
        food.change_location()
        while food.check_on_snake(snake.snake_body):
            food.change_location()
        snake.increase_length()

screen.exitonclick()

