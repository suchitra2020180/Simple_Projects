
## There are random colorful cars on the road moving horizontally.
# The turtle which is controlled by the user must cross the other end of the road.
# If the turtle hits any cars then game over. If the turtle successfully crosses the road then the user reaches next level
# and the cars speed will inccrease according to the level

from turtle import Turtle, Screen
from Cars import Car
from User import Player
import time
from scoreboard import ScoreBoard
import random
#from User import User
#from scoreboard import scoreboard
my_screen = Screen()
my_screen.bgcolor("white")
my_screen.setup(width=600, height=600)
# stopped animation
my_screen.tracer(0)

car = Car()
player = Player()
score_board = ScoreBoard()

# Player control keys
my_screen.listen()
my_screen.onkey(fun=player.move_forward, key="Up")


game_is_on =True
while game_is_on:
    time.sleep(0.1)
    # Manually started animation
    my_screen.update()
    car.create_car()
    car.move()

    #Detect collison of car with turtle
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect the turtle reached the other end
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score_board.increase_level()






my_screen.exitonclick()

