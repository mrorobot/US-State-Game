import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("US state game")
turtle = Turtle()

screen.addshape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
game_on = True
i = 0
guessed_state=[]
missed_state=[]
while game_on:
    answer_state = screen.textinput("guess the state", "what's the state name").title()
    if answer_state=="Exit":
        break
    if answer_state in states:
        i += 1
        state = data[data["state"] == answer_state]
        turtle.goto(int(state.x.iloc[0]),int(state.y.iloc[0]) )
        turtle.write(answer_state, align="center", font=('Arial', 8, 'normal'))
        guessed_state.append(answer_state)

    if i == len(states):
        game_on = False
# for ele in states:
#     if ele in states and ele not in guessed_state:
#         missed_state.append(ele)
#


missed_state=[n for n in states if n in states and n not in guessed_state]
new_data=pandas.DataFrame(missed_state)
new_data.to_csv("missed_list.csv")

