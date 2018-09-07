"""
    Use turtle graphics to draw a tetris board with two simple shapes

    File: Lab 1.py
    Author: Nicholas Curl
"""


# Import the turtle module to draw pictures on the canvas window
import turtle
from turtle import *

# Definitions of functions and procedures to draw a tetris board, a line block, and a square block


def initialize():
    # Starting conditions before functions are run with the pen up and facing north
    left(90)
    up()
    speed(0)


def draw_board():
    # Draws a Tetris board of 10 blocks by 20 blocks
    left(90)
    forward(50)
    down()
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(100)
    up()
    left(90)
    forward(50)
    left(90)


def draw_block():
    # Draws a single colored block
    down()
    begin_fill()
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    end_fill()
    up()


def draw_lineblock():
    # Draws a line block colored blue
    fillcolor("blue")
    draw_block()
    forward(10)
    draw_block()
    forward(10)
    draw_block()
    forward(10)
    draw_block()
    left(180)
    forward(30)
    left(180)


def draw_squareblock():
    # Draws a square block colored yellow
    fillcolor("yellow")
    draw_block()
    forward(10)
    draw_block()
    right(90)
    forward(10)
    left(90)
    draw_block()
    left(180)
    forward(10)
    left(180)
    draw_block()
    left(90)
    forward(10)
    right(90)


def main():
    # The program draws the board, draws in a line block in the lower left corner and draws a square block next to it
    initialize()
    draw_board()
    left(90)
    forward(30)
    left(90)
    forward(90)
    left(180)
    draw_squareblock()
    forward(90)
    right(90)
    forward(30)
    left(90)
    left(90)
    forward(40)
    left(90)
    forward(90)
    left(180)
    draw_lineblock()
    forward(90)
    right(90)
    forward(40)
    left(90)
    done()

# The main program function
main()
