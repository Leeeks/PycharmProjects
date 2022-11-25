from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("ManuBall.gif")
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.random_direction()
        self.start_speed = 2

    def random_direction(self):
        self.start_speed = 2
        random_int = random.randint(0, 360)
        self.setheading(random_int)

    def move(self):
        self.forward(self.start_speed)

    def reflexion_wall(self):
        new_heading = - self.heading()
        self.setheading(new_heading)

    def reflexion_paddle(self):
        self.start_speed += 0.2
        new_heading = - (self.heading() + 180)
        self.setheading(new_heading)