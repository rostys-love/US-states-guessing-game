import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)
score = 0
# answer_state = screen.textinput(title="Guess the State", prompt="What`s another state's name?")
data = pandas.read_csv("50_states.csv")
# state = data[data["state"] == answer_state]
# print(state)


all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State, {score}/50 guessed", prompt="What`s another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("not_guessed.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        score = len(guessed_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    # for guess in guessed_states:
    #     if guess != answer_state:
    #         with open ("not_guessed.txt", mode="w") as not_guessed:
    #             not_guessed.write()


turtle.mainloop()
