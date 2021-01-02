from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    
    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square") 
            car.shapesize(1, 2) 
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.penup()
            car.goto(300, random.randint(-220, 300))
            self.cars.append(car)

    
    
    def move_left(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)

