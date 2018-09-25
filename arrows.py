"""

    File: arrows.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Use the turtle library, parameters, inputs, and recursion to draw bow ties in decreasing size and in
    different positions on the canvas.

"""

# Import the turtle, random, and math libraries
from turtle import *
from random import *
from math import *

# Definitions for the Constants
MAX_FIGURES = 500
MAX_DISTANCE = 30
MAX_SIZE = 30
MAX_ANGLE = 30
BOUNDING_BOX = 200


def initialize():
    """Initializes the turtle with the pen up, setting the color mode of the turtle to 255 and setting its drawing speed
     to 0"""
    up()
    colormode(255)
    speed(0)


def draw_bounding_box():
    forward(BOUNDING_BOX)
    left(90)
    down()
    forward(BOUNDING_BOX)
    left(90)
    forward(BOUNDING_BOX * 2)
    left(90)
    forward(BOUNDING_BOX * 2)
    left(90)
    forward(BOUNDING_BOX * 2)
    left(90)
    forward(BOUNDING_BOX)
    left(90)
    up()
    forward(BOUNDING_BOX)
    left(180)


def draw_arrow(size):
    r = randint(10, 255)
    g = randint(10, 255)
    b = randint(10, 255)
    color(r, g, b)
    begin_fill()
    down()
    forward(size)
    left(120)
    forward(size)
    left(120)
    forward(size)
    left(120)
    end_fill()
    up()


def turtle_move(move):
    angle = randint(-MAX_ANGLE, MAX_ANGLE)
    left(angle)
    forward(move)


def arrows_rec(count, area):
    size = randint(1, MAX_SIZE)
    move = randint(1, MAX_DISTANCE)
    if count == 0:
        return area
    else:
        turtle_move(move)
        x = abs(xcor()) + size
        y = abs(ycor()) + size
        if x >= BOUNDING_BOX or y >= BOUNDING_BOX:
            left(180)
            forward(size + move)
            return arrows_rec(count, area)
        else:
            draw_arrow(size)
            temp = area
            area = 0.25 * (sqrt(3) * pow(size, 2))
            return arrows_rec(count - 1, temp + area)


def arrows_iter(count):
    area = 0
    n = 0
    if count == 0:
        return area
    while n <= count:
        size = randint(1, MAX_SIZE)
        move = randint(1, MAX_DISTANCE)
        turtle_move(move)
        x = abs(xcor()) + size
        y = abs(ycor()) + size
        if x >= BOUNDING_BOX or y >= BOUNDING_BOX:
            left(180)
            forward(size + move)
        else:
            draw_arrow(size)
            area = 0.25 * (sqrt(3) * pow(size, 2)) + area
            n = n + 1
    return area


def main():
    initialize()
    count = int(input("Arrows (0-500): "))
    if count > 500 or count < 0:
        print("Figure count out of range")
        bye()
        exit()
    draw_bounding_box()
    print("The total area painted is ", arrows_rec(count, 0), " units.")
    input("Hit enter to continue...")
    reset()
    initialize()
    draw_bounding_box()
    print("The total area painted is ", arrows_iter(count), " units.")
    print("Close the canvas window to quit.")
    done()


if __name__ == '__main__':
    main()
