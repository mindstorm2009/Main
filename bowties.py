"""

    File: circles.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Use the turtle library, parameters, inputs, and recursion to draw bow ties in decreasing size and in
    different positions on the canvas.

"""

# Import the turtle module to draw pictures on the canvas window
from turtle import *


# Definitions and functions to draw bow ties in decreasing size and in different positions using recursion

def initialize():
    # Start with the turtle pen up, color of the pen being blue, and the fill color being red
    up()
    speed(0)
    pencolor("blue")
    fillcolor("red")


def draw_one_bowtie(size):
    # Function to draw one bow tie using two triangles and a circle
    down()
    left(30)
    forward(size)
    right(120)
    forward(size)
    right(120)
    forward(size * 2)
    left(120)
    forward(size)
    left(120)
    forward(size)
    right(30)
    up()
    left(90)
    forward(size / 4)
    left(90)
    down()
    begin_fill()
    circle(size / 4)
    up()
    end_fill()
    left(90)
    forward(size / 4)
    left(90)


def draw_bowties(size, depth):
    """
    draw_bowties recursively draws bow ties with each iteration being 1/3 of the original bow tie, rotated 30 degrees
    more than the previous iteration, and moved that depths size away from the previous iteration
    depth (int): The current depth of recursion
    size (int): The starting size of each circle
    Preconditions:
        depth >= 0, size > 0
        turtle is facing east
        turtle pen is up
    Post-conditions:
        Bow tie/s have been drawn for the current depth,
        turtle is facing east
        turtle pen is up
    """
    if depth == 0:
        pass
    elif depth == 1:
        draw_one_bowtie(size)
    else:
        draw_one_bowtie(size)
        left(30)
        forward(size * 2)
        draw_bowties(size / 3, depth - 1)
        back(size * 2)
        right(60)
        back(size * 2)
        draw_bowties(size / 3, depth - 1)
        forward(size * 2)
        left(30)


def main():
    # Main function to run the program
    initialize()
    size = 1000
    depth = int(input("Depth: "))
    setup(width=size, height=size, startx=None, starty=None)
    draw_bowties(size / 6, depth)
    done()


# Execution of the main function
if __name__ == '__main__':
    main()
