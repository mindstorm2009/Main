from math import *


def fib0():
    return 0


def fib1():
    return 1


def fib2():
    return fib0() + fib1()


def fib3():
    return fib2() + fib1()


print(fib3())
