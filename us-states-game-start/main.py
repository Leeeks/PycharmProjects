import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

matrix2 = data[data.columns[0]]
states_list = matrix2.tolist()

matrix2 = data[data.columns[1]]
x_positions = matrix2.tolist()

matrix2 = data[data.columns[2]]
y_positions = matrix2.tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="Whats's another state name?").lower()
    print(answer_state)

    if answer_state == "exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for entry in states_list:
        if answer_state == entry.lower():
            guessed_states.append(entry)
            turtle2 = turtle.Turtle()
            turtle2.hideturtle()
            turtle2.pu()
            turtle2.goto(x_positions[states_list.index(entry)], y_positions[states_list.index(entry)])
            turtle2.write(entry)
