from turtle import *


def initialize():
    up()
    speed(0)
    pencolor("blue")
    fillcolor("red")


def draw_one_bowtie(size):
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
    initialize()
    size=1000
    depth=int(input("Depth: "))
    setup(width=size, height=size, startx=None, starty=None)
    draw_bowties(size/6, depth)
    done()


if __name__ == '__main__':
    main()
