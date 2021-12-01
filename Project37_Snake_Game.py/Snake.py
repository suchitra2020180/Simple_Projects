from turtle import Turtle
Up = 90
Down = 270
Right = 0
Left = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        #  SNAKE BODY WITH 3SQUARES
        for i in range(0, 3):
            self.add_segment(i)

    # EVERYTIME WHEN THE SNAKE TAKES THE FOOD ITS BODY WILL EXTEND
    # position to add segment
    def add_segment(self,position):
        x = 0
        y = 0
        t = Turtle(shape="square")
        t.color("white")
        self.snake_body.append(t)
        t.penup()
        t.goto(x, y)
        x -= 20

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            # The snake body has 3 segments and 3rd segment should move to 2nd and 2nd segment should move to Ist.
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def move_upward(self):
        if self.head.heading() != Down:
            # self.snake_body[0].heading()
            self.snake_body[0].setheading(Up)

    def move_downward(self):
        if self.head.heading() != Up:
            self.snake_body[0].setheading(Down)

    def move_right(self):
        if self.head.heading() != Left:
            # t.setheading(0)
            self.head.setheading(Right)

    def move_left(self):
        if self.head.heading() != Right:
            # t.setheading(180)
            self.head.setheading(Left)

    def reset(self):
        self.snake_body.clear()
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.create_snake()
        self.head = self.snake_body[0]
