from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


for i in range(400):
    if i % 2 == 0:
        tim.color("red")
        tim.forward(30)
        tim.left(60)
    else:
        tim.color("blue")
        tim.forward(30)
        tim.right(60)
tim.speed(10)    
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)










screen.exitonclick()









# tim = Turtle()
# screen = Screen()

# tim.speed(1)

# for i in range(400):

#     tim.forward(1)
#     tim.left(1)



# tim.forward(120)
# tim.left(90)
# tim.forward(120)
# tim.left(90)
# tim.forward(120)














# def forwards():
#     tim.forward(10)


# def backwards():
#     tim.backward(10)


# def cointer_clockwise():
#     tim.left(10)


# def clockwise():
#     tim.right(10)


# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.onkey(fun=forwards, key="w")
# screen.onkey(fun=backwards, key="s")
# screen.onkey(fun=cointer_clockwise, key="a")
# screen.onkey(fun=clockwise, key="d")
# screen.onkey(fun=clear_screen, key="c")
# screen.listen()


# screen.exitonclick()
