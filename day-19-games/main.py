from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_start_pos = -100
all_turtles = []

for turtle_color in colors:
    color_str = turtle_color
    turtle_name = turtle_color + "_turtle"
    print(turtle_name)
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(color_str)
    turtle_name.pu()
    turtle_name.goto(x=-230, y=turtle_start_pos)
    turtle_start_pos += 45
    all_turtles.append(turtle_name)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()