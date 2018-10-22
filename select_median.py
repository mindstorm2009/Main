from store_location import *
from quick_sort import *
from time import *


def quick_select(L, k):
    if L != []:
        pivot = L[len(L) // 2]
        smallerList, same, largerList = partition(pivot, L)
        count = len(same)
        m = len(smallerList)
        if k >= m and k < m + count:
            return pivot
        elif m > k:
            return quick_select(smallerList, k)
        else:
            return quick_select(largerList, k - m - count)


def median_quickselect(L):
    k = (len(L) - 1) // 2
    if len(L) % 2 == 1:
        med = quick_select(L, k)
        return med
    else:
        val1 = quick_select(L, k)
        val2 = quick_select(L, k + 1)
        med = (val1 + val2) / 2
        return med


def elapsed_time_quickselect(filename):
    lst = create_list(filename)
    start = time()
    loc = median_quickselect(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time:", "%.20f" % (end - start), "seconds\n")


def main():
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
