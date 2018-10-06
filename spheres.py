"""
Nicholas Curl
"""

from turtle import *
from random import *


def init():
    speed(0)
    colormode(255)
    hideturtle()


def draw_circles(rad, dec):
    if rad <= 0:
        pass
    else:
        circle(rad)
        return draw_circles(rad - dec, dec)


def draw_color_circles(rad, dec, r, g, b):
    red = r - rad
    grn = g - rad
    blu = b - rad
    color(red, grn, blu)
    if rad <= 0:
        pass
    else:
        begin_fill()
        circle(rad)
        end_fill()
        return draw_color_circles(rad - dec, dec, r, g, b)


def draw_sphere(rad, dec, r, g, b):
    red = r - rad
    grn = g - rad
    blu = b - rad
    color(red, grn, blu)
    x = xcor()
    y = ycor()
    if rad <= 0:
        pass
    else:
        down()
        begin_fill()
        circle(rad)
        end_fill()
        x += 0.3 * dec
        y += 1.35 * dec
        goto(x, y)
        up()
        return draw_sphere(rad - dec, dec, r, g, b)


def draw_spheres(num_spheres):
    up()
    while True:
        if num_spheres == 0:
            break
        x = randint(-300, 300)
        y = randint(-300, 300)
        rad = randint(30, 75)
        r = randint(rad, 255)
        g = randint(rad, 255)
        b = randint(rad, 255)
        goto(x, y)
        draw_sphere(rad, 1, r, g, b)
        num_spheres -= 1


def main():
    init()
    tracer(0)
    draw_spheres(10)
    done()


main()
