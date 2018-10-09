"""

    File: shapy_turtle.py
    Assignment: lab
    Language: python3
    Author: Nicholas Curl
    Purpose: Use the turtle library, parameters, inputs, and for loops to process commands from a single string, and
    execute those commands.

"""

from turtle import *


# Defenitions and Functions to process and execute commands from a single string

def initialize():
    """Initalizes the turtle to have speed of 0"""
    speed(0)


def get_num(st):
    """Processes the numbers from the inputted string and returns those numbers, if the there is a syntax error the
    function returns None"""
    digits = ''
    for ch in st:
        if ch.isdigit():
            digits += ch
        else:
            break
    # Checks to see if there is an invalid syntax
    if digits == '':
        print("Invalid Syntax")
        return None
    else:
        return int(digits)


def get_num_double(st):
    """Processes two numbers needed for functions requiring two numerical values"""
    num1 = str(get_num(st))
    num2 = get_num(st[len(num1) + 1:])
    return int(num1), int(num2)


def turn_left(st):
    """Turtle turns left num degrees based on the inputted string"""
    num = get_num(st)
    left(num)


def turn_right(st):
    """Turtle turns right num degrees based on the inputted string"""
    num = get_num(st)
    right(num)


def draw_square(st):
    """Turtle draws a square with a side length of num based on the inputted string"""
    num = get_num(st)
    for i in range(0, 4):
        forward(num)
        left(90)


def draw_triangle(st):
    """Turtle draws a triangle with a side length of num based on the inputted string"""
    num = get_num(st)
    for i in range(0, 3):
        forward(num)
        left(120)


def draw_circle(st):
    """Turtle draws a circle of radius num """
    num = get_num(st)
    circle(num)


def move_forward(st):
    """Turtle moves forward num based on the inputted string"""
    num = get_num(st)
    forward(num)


def move_backward(st):
    """Turtle moves back num based on the inputted string"""
    num = get_num(st)
    backward(num)


def pen_up():
    """Turtle puts the pen up"""
    up()


def pen_down():
    """Turtle puts the pen down"""
    down()


def draw_rectangle(st):
    """Turtle draws a rectangle with a length and width defined by the string inputted"""
    length, width = get_num_double(st)
    for i in range(0, 2):
        forward(length)
        left(90)
        forward(width)
        left(90)


def draw_polygon(st):
    """Turtle draws a polygon of n sides with a side length of length units defined by the inputted string"""
    sides, length = get_num_double(st)
    angle = 360 / sides
    for i in range(0, sides):
        forward(length)
        left(angle)


def go_to(st):
    """Turtle goes to a certain coordinate (x,y) defined by the inputted string"""
    x, y = get_num_double(st)
    goto(x, y)


def turtle_color(st):
    """Changes the pen color of the turtle based on the inputted string"""
    num = get_num(st)
    if num == 0:
        pencolor("red")
    elif num == 1:
        pencolor("blue")
    elif num == 2:
        pencolor("green")
    elif num == 3:
        pencolor("yellow")
    elif num == 4:
        pencolor("brown")
    else:
        pencolor("black")


def process_st(st):
    """Processes the string to determine which function to execute, then executes the function"""
    for i in range(len(st)):
        if st[i] == "<":
            turn_left(st[i + 1:])
        elif st[i] == ">":
            turn_right(st[i + 1:])
        elif st[i] == "S":
            draw_square(st[i + 1:])
        elif st[i] == "T":
            draw_triangle(st[i + 1:])
        elif st[i] == "C":
            draw_circle(st[i + 1:])
        elif st[i] == "F":
            move_forward(st[i + 1:])
        elif st[i] == "B":
            move_backward(st[i + 1:])
        elif st[i] == "U":
            pen_up()
        elif st[i] == "D":
            pen_down()
        elif st[i] == "R":
            draw_rectangle(st[i + 1:])
        elif st[i] == "P":
            draw_polygon(st[i + 1:])
        elif st[i] == "G":
            go_to(st[i + 1:])
        elif st[i] == "Z":
            turtle_color(st[i + 1:])


def main():
    """Main function to run process_st(), initialize(), and take in an input for the commands from the user"""
    initialize()
    st = input("Commands:")
    process_st(st)
    done()


# Checks to see if being run as a file or library
if __name__ == '__main__':
    main()
