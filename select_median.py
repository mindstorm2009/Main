"""
    File: select_median.py
    Author: Nicholas Curl
"""

from store_location import *
from quick_sort import *
from time import *


def quick_select(L, k):
    """An algorithm to figure out the kth smallest value of a list"""
    if L != []:
        pivot = L[len(L) // 2]
        smallerList, same, largerList = partition(pivot, L)
        count = len(same)
        m = len(smallerList)
        """ Checks to see if the k value is greater than or equal to the length of the smaller list and les than the 
        length of the smaller list and the total number of elements that are the same as the pivot"""
        if k >= m and k < m + count:
            return pivot
        elif m > k:
            return quick_select(smallerList, k)
        else:
            return quick_select(largerList, k - m - count)


def median_quickselect(L):
    """Selects the median value using the quick select algorithm"""
    k = (len(L) - 1) // 2
    # Checks to see if the length of the list is even or odd
    if len(L) % 2 == 1:
        med = quick_select(L, k)
        return med
    else:
        val1 = quick_select(L, k)
        val2 = quick_select(L, k + 1)
        med = (val1 + val2) / 2
        return med


def elapsed_time_quickselect(filename):
    """Finds the best location for the store, the sum of the distances of each other store locations, and the total time
    to for the functions to execute"""
    lst = create_list(filename)
    start = time()
    loc = median_quickselect(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time:", "%.20f" % (end - start), "seconds\n")


def main():
    """The main function to find the optimal location for the store, the sum of the distances of other stores to the
    optimal store and the total time to execute both of these functions"""
    filename = input("Enter data file: ")
    lst = create_list(filename)
    start = time()
    loc = median_quickselect(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time:", "%.20f" % (end - start), "seconds\n")


if __name__ == '__main__':
    main()
