from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.x_coordinates = [x for x in range(-280, 280, 20)]
        self.y_coordinates = [x for x in range(-280, 280, 20)]
        random_x = random.choice(self.x_coordinates)
        random_y = random.choice(self.y_coordinates)
        self.goto(random_x, random_y)


    def refresh(self):
        random_x = random.choice(self.x_coordinates)
        random_y = random.choice(self.y_coordinates)
        self.goto(random_x, random_y)