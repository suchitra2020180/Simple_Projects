from turtle import Turtle,Screen

t = Turtle()
my_screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_Anticlockwise():
    #t.setheading(0)
    #t.circle(10,180)
    t.left(45)
    t.forward(10)


def move_clockwise():
    #t.setheading(90)
    #t.circle(-10,180)
    t.right(45)
    t.forward(10)
def clear():
    # Clear the drawing drawn by turtle
    t.clear()
    t.penup()
    # Bring the pointer/curser back to original position
    t.home()
    t.pendown()
# Event listeners # Take inputs from user
my_screen.listen()
# my_screen.onkey(fun=move_forward, key="space")
my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backward, key="s")
my_screen.onkey(fun=move_Anticlockwise,key="a")
my_screen.onkey(fun=move_clockwise, key="d")
my_screen.onkey(fun=clear, key="c")
my_screen.exitonclick()

