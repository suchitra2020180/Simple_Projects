from turtle import Turtle
import random
colors = ["red", "black", "orange", "blue", "green", "violet", "yellow"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed =START_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.5, stretch_len=1)
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)



    def move(self):
        for car in self.all_cars:
            car.backward(START_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
