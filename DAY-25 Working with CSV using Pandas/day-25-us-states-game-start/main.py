import turtle
import pandas

from IPython.utils.tz import tzUTC
from babel.util import missing

screen = turtle.Screen()
screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
score = 0


guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states to learn.csv
        # saves the not guessed states to new csv
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # if they got it right
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        print(state_data.x.item(), state_data.y.item())
        t.write(answer_state)





turtle.exitonclick()