# Create snake body
# Move the snake
# Control the snake using keyboard
# Detect collision with Food
# Create a score board an increase the score  when the snake hits the food
# Game ends when snake hits the wall or snake collides with tail


from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
my_screen = Screen()
my_screen.setup(width=600, height=600)
# screen color
my_screen.bgcolor("black")
my_screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True

my_screen.listen()
my_screen.onkey(fun=snake.move_upward, key="Up")
my_screen.onkey(fun=snake.move_downward, key="Down")
my_screen.onkey(fun=snake.move_right, key="Right")
my_screen.onkey(fun=snake.move_left, key="Left")


while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food 10x10pixel and buffer is 5
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

     # DETECT COLLISION WITH WALL
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on = False
        scoreboard.game_over()

    # DETECT COLLISION WITH OWN TAIL
    # If head collids with any segment of snake body then game over
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




my_screen.exitonclick()
