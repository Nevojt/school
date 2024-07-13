from tkinter import font
from turtle import Turtle, Screen, width
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make you bet",
                            prompt="Whit turtle will win race? Enter color:")


pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(x=-220, y=170)

y_position = [-70, -40, -10, 20, 50, 80]
color = ["red", "green", "blue", "yellow", "purple", "orange"]

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race = True
    
while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                pen.write(f"Turtle winner {winning_color}",
                            font=("Arial", 16, "normal"))
            else:
                pen.write(f"You've lost! The {winning_color}",
                            font=("Arial", 16, "normal"))
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
               
            



screen.exitonclick()
