from quick_sort import *


def median(L):
    lst = quick_sort(L)
    if len(lst) % 2 == 1:
        half = len(lst) // 2
        return lst[half]
    else:
        half = len(lst) / 2
        average = (lst[half - 1] + lst[half]) / 2
        return average


def distance(lst, loc):
    accum = 0
    for element in lst:
        accum += abs(loc - element)
    return accum


