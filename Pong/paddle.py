from turtle import Turtle

MOVE_SPEED = 15
WALL_TOP = 200
WALL_BOTTOM = -200
WALL_RIGHT = 350
WALL_LEFT = -350


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.segments = []
        self.move_up = False
        self.move_down = False
        self.starting_position = starting_position
        self.hideturtle()
        self.create_paddle()

    def create_paddle(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_len=1, stretch_wid=0.5)
        new_segment.pu()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.setheading(270)
        new_segment.speed("fastest")
        self.segments.append(new_segment)

    def up(self):
        if self.segments[2].ycor() < WALL_TOP - 55:
            for segment in self.segments:
                segment.backward(MOVE_SPEED)

    def down(self):
        if self.segments[2].ycor() > WALL_BOTTOM + 60:
            for segment in self.segments:
                segment.forward(MOVE_SPEED)

