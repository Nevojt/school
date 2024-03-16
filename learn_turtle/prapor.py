from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


t.fillcolor("yellow")
t.begin_fill()
for i in range(2):
    t.forward(-250)
    t.left(-90)
    t.forward(-75)
    t.left(-90)
t.end_fill()
t.up()
t.left(90)
t.forward(75)
t.down()

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.forward(75)
    t.left(90)
    t.forward(250)
    t.left(90)
t.end_fill()















screen.exitonclick()