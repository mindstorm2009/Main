"""
    Use turtle graphics to draw a tetris board with four simple shapes and use each shape twice
    
    File: tetris.py
    Author: Nicholas Curl
"""

# Import the turtle module to draw pictures on the canvas window
from turtle import *


"""Definitions of functions and procedures to draw a Tetris board, two line blocks, two square blocks, two L blocks and 
two reverse squiggly blocks"""


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


def draw_lineblock(rot):
    # Draws a line block colored blue
    fillcolor("blue")
    left(rot)
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


def draw_squareblock(rot):
    # Draws a square block colored yellow
    fillcolor("yellow")
    left(rot)
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


def draw_rsquig(rot):
    # Draws a reverse squiggly block colored red
    fillcolor("red")
    left(rot)
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
    right(90)
    forward(10)
    right(90)


def draw_lblock(rot):
    # Draws a L block colored green
    fillcolor("green")
    left(rot)
    draw_block()
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
    right(180)


def square_block1():
    # Sets the preconditions for drawing the first square block, draws it and moves back to the home position
    left(90)
    forward(30)
    left(90)
    forward(90)
    draw_squareblock(180)
    forward(90)
    right(90)
    forward(30)
    left(90)


def line_block1():
    # Sets the preconditions for drawing the first line block, draws it and moves back to the home position
    left(90)
    forward(40)
    left(90)
    forward(90)
    draw_lineblock(180)
    forward(90)
    right(90)
    forward(40)
    left(90)


def line_block2():
    # Sets the preconditions for drawing the second line block, draws it and moves back to the home position
    right(90)
    forward(10)
    right(90)
    forward(90)
    draw_lineblock(270)
    right(90)
    forward(90)
    left(90)
    forward(10)
    right(90)


def r_squig1():
    # Sets the preconditions for drawing the first reverse squiggily block, draws it and moves back to the home position
    left(90)
    forward(20)
    left(90)
    forward(80)
    draw_rsquig(90)
    left(90)
    forward(80)
    right(90)
    forward(20)
    left(90)


def l_block1():
    # Sets the preconditions for drawing the first L block, draws it and moves back to the home position
    left(90)
    forward(50)
    left(90)
    forward(60)
    draw_lblock(0)
    right(180)
    forward(60)
    right(90)
    forward(50)
    left(90)


def l_block2():
    # Sets the preconditions for drawing the second L block, draws it and moves back to the home position
    right(90)
    forward(40)
    right(90)
    forward(90)
    draw_lblock(180)
    forward(90)
    left(90)
    forward(40)
    right(90)


def square_block2():
    # Sets the preconditions for drawing the second square block, draws it and moves back to the home position
    right(90)
    forward(10)
    right(90)
    forward(80)
    draw_squareblock(0)
    right(180)
    forward(80)
    left(90)
    forward(10)
    right(90)


def r_squig2():
    """ Sets the preconditions for drawing the second reverse squiggly block, draws it and moves back to the home
    position"""
    right(90)
    forward(10)
    right(90)
    forward(60)
    draw_rsquig(270)
    right(90)
    forward(60)
    left(90)
    forward(10)
    right(90)


def main():
    """ The program draws the tetris board, two square blocks, two line blocks, two L blocks, and two reverse squiggly
    blocks with each shape in different positions and rotations."""
    initialize()
    draw_board()
    square_block1()
    line_block1()
    line_block2()
    r_squig1()
    l_block1()
    l_block2()
    square_block2()
    r_squig2()
    done()


# The main program function
main()

