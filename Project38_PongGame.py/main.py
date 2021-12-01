
# step1: Create a screen
# step2: create paddle and its movements
from turtle import Turtle, Screen
from Ball import Ball
from Paddle import Paddle
from scoreboard import ScoreBoard
import time
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong Game")
# Tracer controls animation
my_screen.tracer(0)
ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
#paddle.move()
#paddle.middle_line()
score_board = ScoreBoard()
score_board.update_score()


my_screen.listen()
my_screen.onkey(fun=right_paddle.go_up, key="Up")
my_screen.onkey(fun=right_paddle.go_down, key="Down")
my_screen.onkey(fun=left_paddle.go_up, key="w")
my_screen.onkey(fun=left_paddle.go_down, key="s")
# Manual animation
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    ball.move()
    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right_paddle and left_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the right_paddle misses
    # The ball should go to centre position and then start moving to other player
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.left_point()

    # Detect when the left_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.right_point()

my_screen.exitonclick()






