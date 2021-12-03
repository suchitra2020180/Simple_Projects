from turtle import Turtle
START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_POINT = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        #player = Turtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(START_POSITION)
        # self.go_to_start()
        self.left(90)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.goto(START_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_POINT:
            return True
        else:
            return False
