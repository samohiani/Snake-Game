from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(height=800, width=1400)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 695 or snake.head.xcor() < -695 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
