from turtle import *


def initialize():
    speed(0)


def get_num(st):
    digits = ''
    for ch in st:
        if ch.isdigit():
            digits += ch
        else:
            break
    if digits == '':
        print("Invalid Syntax")
        return None
    else:
        return int(digits)


def get_num_double(st):
    num1 = get_num(st)
    num2 = get_num(st[len(num1) + 1:])
    return int(num1), int(num2)


def turn_left(st):
    num = get_num(st)
    left(num)


def turn_right(st):
    num = get_num(st)
    right(num)


def draw_square(st):
    num = get_num(st)
    for i in range(0, 4):
        forward(num)
        left(90)


def draw_triangle(st):
    num = get_num(st)
    for i in range(0, 3):
        forward(num)
        left(120)


def draw_circle(st):
    num = get_num(st)
    circle(num)


def move_forward(st):
    num = get_num(st)
    forward(num)


def move_backward(st):
    num = get_num(st)
    backward(num)


def pen_up():
    up()


def pen_down():
    down()


def draw_rectangle(st):
    length, width = get_num_double(st)
    for i in range(0, 2):
        forward(length)
        left(90)
        forward(width)
        left(90)


def draw_polygon(st):
    sides, length = get_num_double(st)
    angle = 360 / sides
    for i in range(0, sides):
        forward(length)
        left(angle)


def go_to(st):
    x, y = get_num_double(st)
    goto(x, y)


def turtle_color(st):
    num = get_num(st)
    if num == 0:
        pencolor("red")
    elif num == 1:
        pencolor("blue")
    elif num == 2:
        pencolor("green")
    elif num == 3:
        pencolor("yellow")
    elif num == 4:
        pencolor("brown")
    else:
        pencolor("black")


def process_st(st):
    for i in range(len(st)):
        if st[i] == "<":
            turn_left(st[i + 1:])
        elif st[i] == ">":
            turn_right(st[i + 1:])
        elif st[i] == "S":
            draw_square(st[i + 1:])
        elif st[i] == "T":
            draw_triangle(st[i + 1:])
        elif st[i] == "C":
            draw_circle(st[i + 1:])
        elif st[i] == "F":
            move_forward(st[i + 1:])
        elif st[i] == "B":
            move_backward(st[i + 1:])
        elif st[i] == "U":
            pen_up()
        elif st[i] == "D":
            pen_down()
        elif st[i] == "R":
            draw_rectangle(st[i + 1:])
        elif st[i] == "P":
            draw_polygon(st[i + 1:])
        elif st[i] == "G":
            go_to(st[i + 1:])
        elif st[i] == "Z":
            turtle_color(st[i + 1:])


def main():
    initialize()
    st = input("Commands:")
    process_st(st)
    done()


if __name__ == '__main__':
    main()
