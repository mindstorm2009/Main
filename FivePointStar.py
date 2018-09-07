"""
    Use turtle graphics to draw a star using triangles

    File: FivePointStar.py
    Author: Nicholas Curl
"""

# Import the turtle module to draw pictures on the canvas window

import turtle

# Definitions of functions and procedures to draw a star


def setup():
    """Setups the turtle with the pen up and facing north"""
    turtle.up()
    turtle.seth(90)


def main():
    """The program draws a star, and prints instructions to close the canvas window to end the program"""
    setup()
    draw_triangle()
    turtle.left(72)
    draw_triangle()
    turtle.left(144)
    draw_triangle()
    turtle.left(216)
    draw_triangle()
    turtle.left(288)
    draw_triangle()
    print("press the X button to close the program")
    turtle.done()


def draw_triangle():
    """Draws an equilateral triangle with a 200 points on each side and 140 points from the home position"""
    turtle.forward(140)
    turtle.left(90)
    turtle.down()
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(100)
    turtle.up()
    turtle.left(90)
    turtle.forward(140)
    turtle.seth(90)


# The main program function
main()

