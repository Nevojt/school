
import turtle
import pandas


data = pandas.read_csv("ua_state_game/state_ua.csv")
# print(data)
all_state = data["state"].to_list()
# print(all_state)
guesses_state = []

screen = turtle.Screen()
screen.title("State Ukraine")
screen.setup(610, 600)

image = "ua_state_game/UA.gif"
screen.addshape(image)
turtle.shape(image)

try:
    while len(guesses_state) < 24:
        answer_state = screen.textinput(title=f"{len(guesses_state)}/24 States",
                                        prompt="What do you chaise").title()
        
        if answer_state == "exit":
            missing_state = [state for state in all_state if state not in guesses_state]
            break
        
        elif answer_state in all_state:
            guesses_state.append(answer_state)
            t = turtle.Turtle()
            t.color("red")
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
    
except AttributeError as e:
    print("Error: " + str(e))






screen.exitonclick()























# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("Області України")
# screen.setup(610, 600)
# image = "ua_state_game/UA.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("ua_state_game/state_ua.csv")
# all_state = data["state"].to_list()
# guesses_state = []

# try:
#     while len(guesses_state) < 24:
#         answer_state = screen.textinput(title=f"{len(guesses_state)}/24 Областей",
#                                         prompt="Яку область ти вибереш?").title()
#         if answer_state == "Exit":
#             missing_state = [state for state in all_state if state not in guesses_state]
#             break
        
#         if answer_state in all_state:
#             guesses_state.append(answer_state)
#             t = turtle.Turtle()
#             t.color("red")
#             t.hideturtle()
#             t.penup()
#             state_data = data[data.state == answer_state]
#             t.goto(int(state_data.x), int(state_data.y))
#             t.write(answer_state)

# except AttributeError as e:
#     print("Error: " + str(e))


# screen.exitonclick()




































# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("Області України")
# screen.setup(610, 600)
# image = "ua_state_game/UA.gif"
# screen.addshape(image)

# turtle.shape(image)

# data = pandas.read_csv("ua_state_game/state_ua.csv")
# all_state = data["state"].to_list()
# guessed_states = []

# try:
#     while len(guessed_states) < 24:
#         answer_state = screen.textinput(title=f"{len(guessed_states)}/24 Областей", prompt="Яку область вибереш?").title()

#         if answer_state == "Вихід":
#             missing_state = [state for state in all_state if state not in guessed_states]
#             break
        
#         if answer_state in  all_state:
#             guessed_states.append(answer_state)
#             t = turtle.Turtle()
#             t.color("red")
#             t.hideturtle()
#             t.penup()
#             state_data = data[data.state == answer_state]
#             t.goto(int(state_data.x), int(state_data.y))
#             t.write(answer_state)
# except AttributeError as e:
#     print("Error: " + str(e))



# screen.exitonclick()
