import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess The State", prompt="What is the next State?")

data = pandas.read_csv("50_states.csv")
data

screen.exitonclick()