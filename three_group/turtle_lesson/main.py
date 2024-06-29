import turtle
import random


screen = turtle.Screen()

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(0.1)

colors = ["blue", "green", "yellow", "orange", "red", "black", "pink"]

def draw():
    for _ in range(20):
        tim.color("red")
        tim.forward(150)
        tim.color("green")
        tim.left(170)
        tim.forward(150)

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def move_left():
    tim.left(10)
    
def move_right():
    tim.right(10)  
    
def pen_up():
    tim.penup()  
    
def pen_down():
    tim.pendown()
    
def change_color():
    tim.color(random.choice(colors))
    
def pensize_up():
    tim.pensize(tim.pensize() + 2)
    
def pensize_down():
    tim.pensize(tim.pensize() - 2)
    
def clear_screen():
    tim.clear()
    
def home():
    tim.penup()
    tim.home()
    tim.setheading(0)
    tim.pendown()
    
    

    
 
   
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(pen_up, "q")
screen.onkeypress(pen_down, "e")
screen.onkeypress(change_color, "r")
screen.onkeypress(pensize_up, "t")
screen.onkeypress(pensize_down, "y")
screen.onkeypress(clear_screen, "c")
screen.onkeypress(draw, "x")
screen.onkeypress(home, "h")






screen.exitonclick()