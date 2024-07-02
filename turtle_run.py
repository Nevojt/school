from turtle import Turtle, Screen
from random import randint

def create_turtle():
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x=-220, y=170)
    return pen

def position_turtle():
    y_positions = [-70, -40, -10, 20, 50, 80]
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = []
    for index, color in enumerate(colors):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-220, y=y_positions[index])
        all_turtles.append(new_turtle)
    return all_turtles

def draw_turtle(all_turtles, pen):
    is_race_on = user_bet is not None  # Only start the race if a bet was placed
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    pen.write(f"You've won! The {winning_color} turtle is the winner!",
                              font=("Arial", 16, "normal"))
                else:
                    pen.write(f"You've lost! The {winning_color} turtle is the winner!",
                              font=("Arial", 16, "normal"))
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")

pen = create_turtle()
all_turtles = position_turtle()
draw_turtle(all_turtles, pen)

screen.exitonclick()
