"""
    Use the math library, parameters and inputs to calculate roots using the quadratic equation

    File: roots.py
    Author: Nicholas Curl

"""

# Import the math library to use math functions
from math import *


# Definitions of functions and procedures to calculate the roots using the quadratic equation
def quadratic_roots(valA, valB, valC):
    # Calculates the quadratic equation and outputs the roots, if any, and the values of the roots, if any
    # Prints the equation inputted
    print("Equation= ", valA, 'x' + u'\u00b2', '+', valB, 'x' + '+', valC, sep="")
    # Calculates the root for use in the if statements and calculations
    root = pow(valB, 2) - 4 * valA * valC
    # If statements to determine which roots to calculate based on the root variable
    if root < 0:
        print("Zero Roots")
    elif root == 0:
        print("One Root")
        # Calculates the singular root without the square root portion
        output = -valB / (2 * valA)
        print("x =", output)
        x = 0
    elif root > 0:
        # Calculates two roots using the full quadratic equation with both plus and minus the square root
        print("Two Roots")
        output = (-valB - sqrt(root)) / (2 * valA)
        print("x =", output)
        output = (-valB + sqrt(root)) / (2 * valA)
        print("x =", output)


# Prompts the user for values for the function
print('Ax' + u'\u00b2' + ' + Bx + C', sep="")
valueA = int(input("A = "))
print(valueA, 'x' + u'\u00b2' + ' + Bx + C', sep="")
valueB = int(input("B = "))
print(valueA, 'x' + u'\u00b2' + ' + ', valueB, 'x + C', sep="")
valueC = int(input("C = "))
quadratic_roots(valueA, valueB, valueC)
