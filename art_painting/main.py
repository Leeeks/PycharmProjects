import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = [(132, 95, 39), (147, 159, 174), (84, 95, 121), (51, 34, 19), (169, 140, 58), (175, 159, 122)]

screen = Screen()
screen.setup(700, 700)
screen.screensize(650, 650)

start_x = -325
start_y = -325

t = Turtle()
t.speed("fastest")
t.hideturtle()


for i in range(10):
    t.pu()
    t.setpos(start_x, start_y)
    start_y += 50

    for i in range(10):
        t.color(random.choice(color_list))
        t.pd()
        t.dot(20)
        t.pu()
        t.forward(50)


print(screen.screensize())
screen.exitonclick()