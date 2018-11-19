"""
    File: ball_puzzle.py
    Author: Nicholas Curl
    Description: lab

"""
from stack import *
from ball_puzzle_animate import *


def move_ball(can1, can2, stack_list, ball):
    """Moves the ball from can1 to can2"""
    push(stack_list[can2], ball)
    animate_move(stack_list, can1, can2)


def make_cans():
    """Makes an 3 empty cans and puts them into a list"""
    stack_list = []
    for i in range(3):
        stack_list += [make_empty_stack()]
    return stack_list


def init(balls):
    """Initializes the balls in the red can and the animation"""
    cans = make_cans()
    ball_list = balls
    for ball in ball_list:
        push(cans[0], ball)
    print(cans)
    animate_init(balls)
    return cans


def solve_puzzle(stack_list):
    """Solves the puzzle and counts and returns the number of moves to complete the puzzle"""
    moves = 0
    while not is_empty(stack_list[0]):
        ball = pop(stack_list[0])
        if ball == "B":
            if is_empty(stack_list[2]) or stack_list[2].top.value == "B":
                move_ball(0, 2, stack_list, ball)
                moves += 1
            elif not is_empty(stack_list[2]) or stack_list[2].top.value != "B":
                push(stack_list[0], ball)
                while not is_empty(stack_list[2]):
                    if not stack_list[2].top.value == "R":
                        break
                    ball = pop(stack_list[2])
                    move_ball(2, 1, stack_list, ball)
                    moves += 1
                ball = pop(stack_list[0])
                move_ball(0, 2, stack_list, ball)
                moves += 1
        elif ball == "G":
            if is_empty(stack_list[1]) or stack_list[1].top.value == "G":
                move_ball(0, 1, stack_list, ball)
                moves += 1
            elif not is_empty(stack_list[1]) or stack_list[1].top.value != "G":
                push(stack_list[0], ball)
                while not is_empty(stack_list[1]):
                    if not stack_list[1].top.value == "R":
                        break
                    ball = pop(stack_list[1])
                    move_ball(1, 2, stack_list, ball)
                    moves += 1
                ball = pop(stack_list[0])
                move_ball(0, 1, stack_list, ball)
                moves += 1
        else:
            if stack_list[0].top.value == "B":
                move_ball(0, 1, stack_list, ball)
                moves += 1
            elif stack_list[0].top.value == "G":
                move_ball(0, 2, stack_list, ball)
                moves += 1
            else:
                move_ball(0, 1, stack_list, ball)
    for i in range(1, 3):
        while stack_list[i].top.value == "R":
            ball = pop(stack_list[i])
            move_ball(i, 0, stack_list, ball)
            moves += 1
    return moves


def main():
    """Main function for the program"""
    balls = input("What are the initial balls: ")
    stack_list = init(balls)
    moves = solve_puzzle(stack_list)
    print("Total number of moves to solve:", moves)
    animate_finish()


if __name__ == '__main__':
    main()
