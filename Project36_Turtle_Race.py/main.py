
import turtle as t
from turtle import Turtle,Screen
import random

my_screen= Screen()
# Setting screen to a width of 50 and height of 400 units
my_screen.setup(width=500, height=400)
is_race_on = False

# Creating 6 turtles with 6 different colors
color=["red", "blue", "green", "yellow", "violet", "orange"]
x=-250
y=-100
all_turtles=[]
for i in color:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x,y)
    y += 50
    all_turtles.append(new_turtle)


# Take user input
user_bet=my_screen.textinput(title=" Welcome to Turtle Race ", prompt=" Guess which turtle will win the race: ")
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        rand_distance= random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()

