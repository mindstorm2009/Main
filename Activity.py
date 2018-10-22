from merge_sort import *
from quick_sort import *
from random import *
from math import *
from time import *

def create_random_list(n, limit):
    L = []
    for i in range(n):
        L += [randint(0, limit)]
    return L


def isSorted(L):
    index = 0
    sorted = False
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True

def calc_square_root():
    start = time()
    for i in range(10000000):
        sqrt(i)
    end = time()
    return end - start

def main():
    lst = create_random_list(5, 1000)
    test_lst = lst[:]
    test_lst.sort()
    print(isSorted(lst))
    print(isSorted(test_lst))
    print(calc_square_root(), " seconds")


main()
