from turtle import *
from math import *
from random import *

def init():
    setworldcoordinates(-10, 0, 10, 1000)
    speed(0)
    ht()
    colormode(255)
    up()



def draw_circle(rad, r, g, b):
    color(r, g, b)
    down()
    begin_fill()
    circle(rad)
    end_fill()
    up()


def draw_circles(rad, dec):
    r = 0
    g = 55
    b = 0
    angle = 0
    x = 0
    y = 0
    red = r
    grn = g
    blu = b
    while True:
        while True:
            red += dec
            grn += dec
            blu += dec
            if grn > 255:
                break
            goto(x, y)
            x = angle
            y = x * exp(x)
            draw_circle(rad, red, grn, blu)
            angle += 0.1
        while True:
            red -= dec
            grn -= dec
            blu -= dec
            if red < 0:
                break
            goto(x, y)
            x = 10 * angle
            y = x*exp(x)
            draw_circle(rad, red, grn, blu)
            angle += 0.1

def draw_function():
    angle = -100
    x = 0
    y = 0
    while True:
        goto(x,y)
        down()
        x += 0.1
        y = log1p(x)
        angle += 0.1

def main():
    init()
    #draw_circles(5, 1)
    draw_function()
    done()


main()
