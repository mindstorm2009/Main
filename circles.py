"""

    File: circles.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Use the turtle library, parameters, inputs, and recursion to draw circles in decreasing size and in
    different positions on the canvas.

"""

# Import the turtle module to draw pictures on the canvas window
from turtle import *


# Definitions and functions to  draw circles in decreasing size and in different positions on the canvas using recursion

def initialize(size):
    # Initializes the turtle to the starting position
    up()
    right(90)
    forward(size)
    left(90)
    speed(0)


def draw_one_circle(size):
    # Draws one circle
    down()
    circle(size)
    up()


def draw_circles(depth, size):
    """
    draw_circles recursively draws circles with each iteration being 1/2 of the original circle at placed at the left
    and right most points on the circle
    depth (int): The current depth of recursion
    size (int): The starting size of each circle
    Preconditions:
        depth >= 0, size > 0
        turtle is facing east
        turtle pen is up
    Post-conditions:
        Circle/s have been drawn for the current depth,
        turtle is facing east
        turtle pen is up
    """
    if depth == 0:
        pass
    elif depth == 1:
        draw_one_circle(size)
    else:
        draw_one_circle(size)
        left(90)
        forward(size)
        left(90)
        forward(size)
        right(180)
        draw_circles(depth - 1, size / 2)
        forward(size * 2)
        draw_circles(depth - 1, size / 2)
        right(180)
        forward(size)
        left(90)
        forward(size)
        left(90)


def main():
    # Main function to run the program and prompts the user for the depth of the recursion
    size = 200
    initialize(size)
    depth = int(input("Depth: "))
    draw_circles(depth, size)
    done()


# Runs the main function
if __name__ == '__main__':
    main()
