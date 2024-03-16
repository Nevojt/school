from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed(10)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         t.color(c)
#         t.forward(steps)
#         t.right(50)
def right():
    t.color('red')
    t.fillcolor('yellow')
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(170)
        if abs(t.pos()) < 1:
            break
    t.end_fill()

def left():
    t.color('red')
    t.fillcolor('yellow')
    t.begin_fill()
    while True:
        t.forward(200 * (-1))
        t.right(170 * (-1))
        if abs(t.pos()) < 1:
            break
    t.end_fill()
    
left()
right()















screen.exitonclick()