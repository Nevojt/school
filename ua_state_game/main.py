import turtle
import pandas

screen = turtle.Screen()
screen.title("Області України")
screen.setup(610, 600)
image = "UA.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("state_ua.csv")
all_state = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/24 Областей", prompt="Яку область вибереш?").title()

    if answer_state == "Вихід":
        # missing_state = []
        # for state in all_state:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        # new_data = pandas.DataFrame(missing_state)
        # new_data.to_csv("states.csv")
        break
    
    if answer_state in  all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)










screen.exitonclick()
