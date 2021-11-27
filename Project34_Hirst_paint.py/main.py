import colorgram
import turtle
import random
t = turtle.Turtle()
my_screen = turtle.Screen()
print(my_screen.canvheight)
# Extract colors from a image
colors=colorgram.extract('DamienHirst.jpg', 20)
print(colors)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color= (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
# moving the pointer from center to backward
t.penup()
t.setx(-500)
t.sety(-200)
t.pendown()

for col in range(0,10):
    for row in range(0, 10):
        t.speed("fastest")
        sel_color = random.choice(rgb_colors)
        print("selected color:",sel_color)
        my_screen.colormode(255)
        t.pencolor(sel_color)
        # setting the fill color
        t.fillcolor(sel_color)
        # begin filling the color
        t.begin_fill()
        # Draw a circle
        t.circle(20)
        # stop filling the color
        t.end_fill()
        t.penup()
        t.forward(50)
        t.pendown()
    t.penup()
    t.backward(500)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.pendown()
    t.hideturtle()

my_screen.exitonclick()