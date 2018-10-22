"""

    File: arrows.py
    Assignment: lab
    Language: python3
    Author: Nicholas Curl
    Purpose: Use the turtle library, parameters, inputs, recursion and iteration to draw arrows of random sizes,
    placement and colors within a bounding box
    different positions on the canvas.

"""

# Import the turtle, random, and math libraries
from turtle import *
from random import *
from math import *

"""Definitions and functions to draw arrows of different size, placement, and color randomly using recursion and 
iteration"""

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
    """Draws a bounding box with a length of 400 units on each side"""
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
    """ Draws one arrow based on the size, passed as a parameter, and randomly selects a color"""
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
    """Chooses a random angle within the range of [-30 degrees, 30 degrees], then moves the turtle forward based on the
    parameter"""
    angle = randint(-MAX_ANGLE, MAX_ANGLE)
    left(angle)
    forward(move)


def arrows_rec(count, area):
    """Recursively draws count number of arrows, with each sequence choosing a random size and movement within their
    maximum boundaries, while keeping the triangles from drawing outside the bounding box, and calculates the total
    area painted"""
    size = randint(1, MAX_SIZE)
    move = randint(1, MAX_DISTANCE)
    # Checks to see if the count is 0 to finish the recursion
    if count == 0:
        return area
    else:
        turtle_move(move)
        x = abs(xcor()) + size
        y = abs(ycor()) + size
        # Checks to see if the arrow to be drawn will be outside the bounding box
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
    """Iteratively draws count number of arrows, with each sequence choosing a random size and movement within their
        maximum boundaries, while keeping the triangles from drawing outside the bounding box, and calculates the total
        area painted"""
    area = 0
    n = 0
    # Condition to return the area if the count is not > 0
    if count == 0:
        return area
    while n <= count:
        size = randint(1, MAX_SIZE)
        move = randint(1, MAX_DISTANCE)
        turtle_move(move)
        x = abs(xcor()) + size
        y = abs(ycor()) + size
        # Checks to see if the arrow to be will be outside the bounding box
        if x >= BOUNDING_BOX or y >= BOUNDING_BOX:
            left(180)
            forward(size + move)
        else:
            draw_arrow(size)
            area = 0.25 * (sqrt(3) * pow(size, 2)) + area
            n = n + 1
    return area


def main():
    """Main function that prompts the user for the amount of arrows to be drawn, and outputs the total area of both
    the recursive and iterative functions"""
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


# Checks to see if running as a file
if __name__ == '__main__':
    main()
