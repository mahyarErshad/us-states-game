import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 is guessed.", prompt="What is the next State?").title()
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == answer]
        t.goto(int(state.x), int(state.y))
        t.write(answer)

screen.exitonclick()