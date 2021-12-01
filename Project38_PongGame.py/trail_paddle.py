class Paddle():
    def __init__(self):
        self.n_segments = 3
        self.all_segments = []
        self.paddle_body = self.all_segments
        # colors = ["white", "red", "blue", "green"]
        x = 0
        y = 0
        for seg in range(0, self.n_segments):
            t = Turtle()
            t.shape("square")
            t.color("white")
            self.all_segments.append(t)
            t.penup()
            t.goto(x, y)
            y += 20
        self.all_segments[0].setheading(270)

    def move(self):
        for seg in range(len(self.all_segments)-1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg-1].ycor()
            self.all_segments[seg].goto(new_x, new_y)
        self.all_segments[0].forward(20)


    def middle_line(self):
        m = Turtle()
        m.color("white")
        m.penup()
        m.goto(0, -280)
        m.setheading(90)
        m.pendown()
        for i in range(0, 30):
            m.forward(10)
            m.penup()
            m.forward(10)
            m.pendown()

    def upward(self):
        self.all_segments[0].setheading(90)

    def downward(self):
        self.all_segments[0].setheading(270)