import turtle
from turtle import Turtle, Screen
import random

turtle_colors = ["light slate gray", "dodger blue", "powder blue", "medium turquoise",
                 "crimson", "firebrick", "navajo white", "slate blue"]

directions = [0, 90, 180, 270]

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
#tim.pensize(15)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

for i in range(360):
    tim.color(random_color())
    tim.circle(200)
    tim.right(1)


#for i in range(500):
    #tim.color(random_color())
    #tim.forward(30)
    #tim.setheading(random.choice(directions))

# for i in range(3, 15):
    #tim.color(random.choice(turtle_colors))
    #for s in range(i):
        #tim.forward(100)
        #tim.right(360/i)

screen = Screen()
screen.exitonclick()
