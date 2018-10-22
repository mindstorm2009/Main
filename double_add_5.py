"""

    File: double_add_5.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Use recursive functions and iterative functions to calculate double plus 5

"""


# Definitions and functions to calculate double plus 5 both recursively and iteratively

def print_sequence_rec(start, count):
    """ Prints the sequence using the starting condition and calculating the values for every value of count recursively
    until count reaches 0."""
    """if statements to end the recursion as to not let it go on into infinity, also a defensive if statement is added 
    to make sure count >= 0"""
    if count < 0:
        pass
    elif count == 0:
        print(start, end=" ")
    else:
        print(start, end=" ")
        return print_sequence_rec((start * 2) + 5, count - 1)


def print_sequence_iter(start, count):
    """Uses iteration to calculate double plus 5 calculating count number of times from the starting value and prints
    the sequence of values."""
    n = count
    while count <= n:
        """if statements to end the loop as to not let it go on into infinity, also a defensive if statement is added 
        to make sure count >= 0"""
        if count < 0:
            break
        elif count == 0:
            print(start, end=" ")
            break
        else:
            print(start, end=" ")
            count = count - 1
            start = (start * 2) + 5


def find_end_rec(start, count):
    # Recursively finds the end value for the sequence and returns said value
    """if statements to end the recursion as to not let it go on into infinity, also a defensive if statement is added
    to make sure count >= 0"""
    if count < 0:
        pass
    elif count == 0:
        return start
    else:
        return find_end_rec((start * 2) + 5, count - 1)


def find_end_iter(start, count):
    # Iteratively finds the value for the sequence and returns said value
    n = count
    while count <= n:
        """if statements to end the loop as to not let it go on into infinity, also a defensive if statement is added 
        to make sure count >= 0"""
        if count < 0:
            break
        elif count == 0:
            break
        else:
            count = count - 1
            start = (start * 2) + 5
    return start


def find_start_rec(goal, count, counter):
    """ Uses recursion and the find_end_rec function to find the minimum starting value for the value after count number
    of times so that its last value is greater than or equal to the goal"""
    """if statements to end the recursion as to not let it go on into infinity, also a defensive if statement is added
    to make sure count >= 0"""
    if find_end_rec(counter, count) >= goal:
        return counter
    else:
        return find_start_rec(goal, count, counter + 1)


def find_start_iter(goal, count):
    """ Uses iteration and the find_end_iter function to find the minimum starting value for the value after count
    number of times so that its last value is greater than or equal to the goal"""
    n = 0
    while True:
        value = find_end_iter(n, count)
        """if statements to end the loop as to not let it go on into infinity, also a defensive if statement is added 
        to make sure count >= 0"""
        if value >= goal:
            break
        else:
            n = n + 1
    return n


def main(start, count, goal):
    # The main function to allow all the functions to be executed
    print_sequence_rec(start, count)
    print("")
    print_sequence_iter(start, count)
    print("")
    print(find_end_rec(start, count))
    print(find_end_iter(start, count))
    print(find_start_rec(goal, count, 0))
    print(find_start_iter(goal, count))


""" Checks to see if this file is being imported or run through the file, if it is being run through the file it will
execute the main function."""
if __name__ == '__main__':
    main(2, 5, 200)
