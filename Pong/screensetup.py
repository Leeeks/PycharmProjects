from turtle import Turtle
WALL_TOP = 200
WALL_BOTTOM = -200
WALL_RIGHT = 350
WALL_LEFT = -350

class ScreenSetup(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, WALL_TOP)
        self.setheading(270)
        self.make_line()

    def make_line(self):
        for i in range(31):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)
