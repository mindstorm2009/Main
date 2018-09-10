"""
    Use turtle graphics to draw a tetris board with four simple shapes and use each shape twice

    File: tetris2.py
    Author: Nicholas Curl
"""

# Import the turtle module to draw pictures on the canvas window
from turtle import *

"""Definitions of functions and procedures to draw a Tetris board, two line blocks, two square blocks, two L blocks and 
two reverse squiggly blocks"""


def initialize():
    # Starting conditions before functions are run with the pen up and facing north
    up()
    speed(0)
    left(180)
    forward(50)
    left(90)
    forward(100)
    right(180)


def draw_board():
    # Draws a Tetris board of 10 blocks by 20 blocks
    down()
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    up()


def draw_block():
    # Draws a single colored block
    down()
    begin_fill()
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    end_fill()
    up()


def draw_lineblock(col, row, rot):
    # Draws a line block colored blue
    fillcolor("blue")
    turtle_move(col, row)
    if rot == 0 or rot == 180:
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        right(180)
        forward(30)
        right(90)
        forward(-10)
        turtle_move(-col, -row)

    elif rot == 90 or rot == 270:
        fillcolor("red")
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        right(180)
        forward(30)
        right(180)
        turtle_move(-col, -row)
    else:
        print("error")


def draw_squareblock(col, row):
    # Draws a square block colored yellow
    fillcolor("yellow")
    turtle_move(col, row)
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
    turtle_move(-col, -row)


def draw_rsquig(col, row, rot):
    # Draws a reverse squiggly block colored red
    fillcolor("red")
    turtle_move(col, row)
    if rot == 0 or rot == 180:
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        right(180)
        forward(20)
        left(90)
        forward(20)
        left(180)
        turtle_move(-col, -row)
    elif rot == 90 or rot == 270:
        draw_block()
        forward(10)
        draw_block()
        left(90)
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        right(90)
        forward(20)
        right(180)
        turtle_move(-col, -row)


def draw_squig(col, row, rot):
    fillcolor("red")
    turtle_move(col, row)
    if rot == 0 or rot == 180:
        forward(20)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        left(90)
        draw_block()
        forward(10)
        draw_block()
        right(180)
        forward(20)
        left(90)
        forward(20)
        left(180)
        turtle_move(-col, -row)
    elif rot == 90 or rot == 270:
        draw_block()
        forward(10)
        draw_block()
        left(90)
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        right(90)
        forward(20)
        right(180)
        turtle_move(-col, -row)


def draw_lblock(col, row, rot):
    # Draws a L block colored green
    fillcolor("green")
    if rot == 0:
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        draw_block()
    """draw_block()
    left(90)
    forward(10)
    right(90)
    draw_block()
    forward(10)
    draw_block()
    forward(10)
    draw_block()
    right(90)
    forward(10)
    right(90)
    forward(20)
    right(180)"""


def turtle_move(x, y):
    x = x * 10
    y = y * 10
    right(90)
    forward(x)
    left(90)
    forward(y)


def main():
    """ The program draws the tetris board, two square blocks, two line blocks, two L blocks, and two reverse squiggly
    blocks with each shape in different positions and rotations."""
    initialize()
    draw_board()
    shape = input("What Shape (B,I,L,J,Z,S,T): ")
    posX = int(input("What Column (0-9):"))
    posY = int(input("What Row (0-19):"))
    deg = int(input("What direction (0,90,180,270)"))
    if shape == "I" or shape == "i":
        draw_lineblock(posX, posY, deg)
    elif shape == "B" or shape == "b":
        draw_squareblock(posX, posY)
    elif shape == "S" or shape == "s":
        draw_rsquig(posX, posY, deg)
    elif shape == "L" or shape == "l":
        draw_lblock(posX, posY, deg)
    done()


# The main program function
main()
