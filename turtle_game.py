from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def cointer_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=cointer_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.listen()


screen.exitonclick()
