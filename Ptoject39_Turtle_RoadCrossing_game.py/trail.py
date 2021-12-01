from turtle import Turtle,Screen
my_screen = Screen()
my_screen.setup(600, 600)
t = Turtle()
t.shape("square")
for i in range(0, 12):
    if t.xcor() < 280:
        t.forward(90)
my_screen.exitonclick()

