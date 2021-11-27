
from turtle import Turtle,Screen
import random
import turtle as t
pointer = Turtle()
print(pointer)
# Change the pointer shape to turtle
pointer.shape("turtle")
# Change the color of the pointer
           ##pointer.color("blue")
my_screen = Screen()
print(my_screen.canvheight)
# move forward 100 place
# pointer.forward(100)

# Drawing a square
print("TURTLE POSITION:",pointer.position)

def square():
    pointer.forward(100)
    pointer.right(90)
    pointer.forward(100)
    pointer.right(90)
    pointer.forward(100)
    pointer.right(90)
    pointer.forward(100)

##square()

# 10 spaces 50 times
def dashed_line():
    for i in range(0,15):
        pointer.forward(10)
        pointer.penup()
        pointer.forward(10)
        pointer.pendown()


##dashed_line()

# Drawing shapes from triangle, square to decagon with same position but with random colors
def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    pointer.color(R, G, B)


def different_shapes():
    # pointer.setpos(30, 30)
    pointer.sety(300)
    for shape_angle in range(3, 11):
        angle = 360/shape_angle
        change_color()

        for turn in range(0, shape_angle):
            pointer.forward(20)
            pointer.right(angle)
            pointer.forward(20)


##different_shapes()

##speed, thickness of pointer, random color
def random_walk():
    direction = ['E','W']
    pointer.pensize(10) # Thickness of the line
    pointer.speed("fastest")   # speed in range 1 to 10
    for i in range(0, 200):
        change_color()
        motion = random.choice(direction)
        if motion == 'E':
            pointer.right(90)
        else:
            pointer.left(90)
        pointer.forward(20)


#random_walk()

def draw_spirograph(gap_between_circles):
    pointer.shape("arrow")
    pointer.speed("fastest")
    for i in range(0, int(360/gap_between_circles)):
        change_color()
        pointer.circle(70)
        pointer.setheading(pointer.heading() +gap_between_circles)


draw_spirograph(5)




# Screen will  exit when we click
my_screen.exitonclick()


