from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_forwards():
    tim.forward(10)

def rotate_counter_clockwise():
    tim.left(10)

def rotate_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()

def pause_drawing():
    tim.penup()

def continue_drawing():
    tim.pendown()

def erase():
    tim.color("white")

from random import random
def purple():
    tim.color("purple")

def blue():
    tim.color("blue")

def red():
    tim.color("red")

def circle():
    tim.circle(30)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="q", fun=pause_drawing)
screen.onkey(key="e", fun=continue_drawing)
screen.onkey(key="t", fun=purple)
screen.onkey(key="y", fun=erase)
screen.onkey(key="b", fun=blue)
screen.onkey(key="r", fun=red)
screen.onkey(key="o", fun=circle)
screen.exitonclick()
