from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from Scoreboard import scoreboard
import random

screen=Screen()
screen.setup(600,600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    for segments in snake.segment[1:]:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()










screen.exitonclick()