# Create snake body
# Move the snake
# Control the snake using keyboard
# Detect collision with Food
# Create a score board an increase the score  when the snake hits the food
# Game ends when snake hits the wall or snake collids with tail

import turtle
from turtle import Turtle, Screen
from Snake import Snake
import time
my_screen = Screen()
my_screen.setup(width=500, height=400)
# screen color
my_screen.bgcolor("black")
my_screen.title("Snake Game")

snake= Snake()



game_is_on =True
while game_is_on:
    my_screen.update
    time.sleep(0.1)


        i.forward(20)

        #if t.xcor()==250:




def move_upward():
    t.heading()
    t.setheading(90)

def move_downward():
    t.setheading(270)

def move_right():
    #t.setheading(0)
    t.right(90)
    t.forward(30)

def move_left():
    #t.setheading(180)
    t.left(90)
    t.forward(30)


def direction():
    my_screen.listen()
    my_screen.onkeypress(fun=move_upward, key ="u")
    my_screen.onkeypress(fun=move_downward, key="d")
    my_screen.onkeypress(fun=move_right, key="r")
    my_screen.onkeypress(fun=move_left, key="l")
my_screen.exitonclick()