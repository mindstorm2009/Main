"""
    Use turtle graphics to draw a tetris board with four simple shapes and use each shape twice, and draw one additional
    block of the users choice, including position and rotation.

    File: tetris2.py
    Author: Nicholas Curl
"""

# Import the turtle module to draw pictures on the canvas window
from turtle import *

"""Definitions of functions and procedures to draw a Tetris board, two line blocks, two square blocks, two L blocks, 
two squiggly blocks, and one additional block of the users choice, position, and rotation"""


def initialize():
    """Starting conditions before functions are run with the pen up, facing north, and starting in the left corner of
    the board"""
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
    # Draws a line block colored blue moved to any position and rotation
    fillcolor("blue")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
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
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 90 or rot == 270:
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
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    else:
        print("error")
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def draw_squareblock(col, row):
    # Draws a square block colored yellow moved to any position and rotation
    fillcolor("yellow")
    # Moves the datum point to the starting position
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
    # Moves the datum point back to the home position
    turtle_move(-col, -row)


def draw_rsquig(col, row, rot):
    # Draws a s block colored red moved to any position and rotation
    fillcolor("red")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
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
        # Moves the datum point back to the home position
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
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    else:
        print("error")
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def draw_squig(col, row, rot):
    # Draws a z block colored purple moved to any position and rotation
    fillcolor("purple")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
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
        forward(10)
        left(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 90 or rot == 270:
        right(90)
        forward(10)
        left(90)
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
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    else:
        print("error")
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def draw_lblock(col, row, rot):
    # Draws a L block colored green moved to any position and rotation
    fillcolor("green")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
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
        left(90)
        forward(20)
        left(90)
        forward(10)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 90:
        right(90)
        forward(10)
        left(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        draw_block()
        forward(10)
        left(90)
        forward(20)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 180:
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        right(90)
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        left(180)
        forward(20)
        left(90)
        forward(20)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 270:
        right(90)
        forward(10)
        left(90)
        draw_block()
        left(90)
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        right(180)
        forward(20)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    else:
        print("error")
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def draw_rlblock(col, row, rot):
    # Draws a J block colored orange moved to any position and rotation
    fillcolor("orange")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
    if rot == 0:
        forward(10)
        draw_block()
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
        right(90)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 90:
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        left(90)
        draw_block()
        left(90)
        forward(10)
        left(90)
        forward(20)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 180:
        forward(20)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        right(90)
        forward(10)
        draw_block()
        right(90)
        forward(30)
        left(90)
        forward(10)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 270:
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        forward(10)
        left(90)
        forward(20)
        left(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def draw_tblock(col, row, rot):
    # Draws a t block colored blue moved to any position and rotation
    fillcolor("pink")
    # Moves the datum point to the starting position
    turtle_move(col, row)
    # Conditional for rotation
    if rot == 0:
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        left(90)
        draw_block()
        left(90)
        forward(10)
        right(90)
        forward(10)
        draw_block()
        right(180)
        forward(20)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 90:
        forward(10)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        draw_block()
        right(90)
        forward(10)
        draw_block()
        right(180)
        forward(20)
        left(90)
        forward(10)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 180:
        right(90)
        forward(10)
        left(90)
        draw_block()
        forward(10)
        draw_block()
        left(90)
        draw_block()
        right(90)
        forward(10)
        draw_block()
        right(180)
        forward(20)
        right(90)
        forward(10)
        right(90)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    elif rot == 270:
        forward(20)
        right(90)
        draw_block()
        forward(10)
        draw_block()
        forward(10)
        draw_block()
        right(90)
        forward(10)
        draw_block()
        right(90)
        forward(20)
        left(90)
        forward(10)
        right(180)
        # Moves the datum point back to the home position
        turtle_move(-col, -row)
    else:
        print("error")
        # Moves the datum point back to the home position
        turtle_move(-col, -row)


def turtle_move(x, y):
    # Function to move the turtle to any row or column on the screen
    x = (x * 10)
    y = (y * 10)
    right(90)
    forward(x)
    left(90)
    forward(y)


def shape_chooser():
    # Function to prompt the user for the shape, rotation, row, and column, and apply those variables accordingly
    # Prompts for the user
    shape = input("What Shape (B,I,L,J,Z,S,T): ")
    deg = int(input("What rotation (0,90,180,270)"))
    posY = int(input("What Row (0-19):"))
    posX = int(input("What Column (0-9):"))
    # Conditionals for choosing the thape
    if shape == "I" or shape == "i":
        draw_lineblock(posX, posY, deg)
    elif shape == "B" or shape == "b":
        draw_squareblock(posX, posY)
    elif shape == "S" or shape == "s":
        draw_rsquig(posX, posY, deg)
    elif shape == "L" or shape == "l":
        draw_lblock(posX, posY, deg)
    elif shape == "J" or shape == "j":
        draw_rlblock(posX, posY, deg)
    elif shape == "T" or shape == "t":
        draw_tblock(posX, posY, deg)
    elif shape == "Z" or shape == "z":
        draw_squig(posX, posY, deg)
    else:
        print("error")


def main():
    """ The program draws the tetris board, two line blocks, two square blocks, two L blocks,
    two squiggly blocks draw any shape with any position and rotation."""
    initialize()
    draw_board()
    draw_lineblock(0, 0, 90)
    draw_squareblock(1, 0)
    draw_lineblock(3, 0, 0)
    draw_lblock(7, 0, 270)
    draw_lblock(0, 2, 90)
    draw_squig(2, 1, 0)
    draw_squareblock(5, 1)
    draw_squig(4, 3, 0)
    shape_chooser()
    done()


# The main program function
main()
