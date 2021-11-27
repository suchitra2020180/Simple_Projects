from turtle import Turtle
class Snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        #  SNAKE BODY WITH 3SQUARES
        for i in range(0, 3):
            t = Turtle(shape="square")
            t.color("white")
            self.snake_body.append(t)
            t.penup()
            t.goto(x, y)
            x -= 20

    def move(self):
        for seg in range(start=len(snake_body) - 1, stop=0, step=-1):
            # The snake body has 3 segments and 3rd segment should move to 2nd and 2nd segment should move to Ist.
            new_x = snake_body[seg - 1].xcor()
            new_y = snake_body[seg - 1].ycor()
            snake_body[seg].goto(new_x, new_y)
        snake_body[0].forward(20)