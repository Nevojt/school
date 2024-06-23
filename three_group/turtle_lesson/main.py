import turtle


screen = turtle.Screen()

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(0.1)


for _ in range(40):
    tim.color("red")
    tim.forward(150)
    tim.color("green")
    tim.left(170)
    tim.forward(150)
    






screen.exitonclick()