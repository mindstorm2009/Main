"""
File: HW08.py
Author: Nicholas Curl
"""

# Import the necessary libraries and programs to run this program.
import random
from time import *
import insertion_sort
import merge_sort
import quick_sort


# Definitions and functions to test different sorting algorithms and for running a merge-quick sort algorithm


def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()]
    return L


def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(1, 100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random() * i]
    return L


def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8) * i]
    return L


def partition(L):
    """Same as the partition function in quick_sort.py file, but returns a blank tuple when a blank list is inputted and
    sets the pivot when called"""
    if L == []:
        return [], [], []
    pivot = L[0]
    less, same, more = ([], [], [])
    for e in L:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return less, same, more


def split(L):
    """Same as the split function in merge_sort.py, which splits the list based on even and odd indexes"""
    if L == []:
        return []
    else:
        evens = []
        odds = []
        is_even_index = True
        for e in L:
            if is_even_index:
                evens.append(e)
            else:
                odds.append(e)
            is_even_index = not is_even_index
        return evens, odds


def merge_quick_sort(L):
    """A sorting algorithm that utilizes the merge and quick sort algorithms.  Each recursion it runs a layer of quick
    sort and a layer of merge sort."""
    # Checks to see if the list is blank
    if L == []:
        return []
    else:
        half1, half2 = split(L)
        less1, same1, more1 = partition(half1)
        less2, same2, more2 = partition(half2)
        half1 = merge_quick_sort(less1) + same1 + merge_quick_sort(more1)
        half2 = merge_quick_sort(less2) + same2 + merge_quick_sort(more2)
        return merge_sort.merge(half1, half2)


def test_merge_quick_sort():
    """Tests the merge-quick sort algorithm with a list of length 20, printing the unsorted list and the sorted list"""
    print("Testing the correctness of merge_quick_sort:")
    print("Before sorted:")
    unsorted_lst = get_list2(20)
    print(unsorted_lst)
    print("After sorted:")
    sorted_list = merge_quick_sort(unsorted_lst)
    print(sorted_list)


def test_compare_l1(n):
    """Test the speed of each algorithm using the get_list1() function to create a list of n length"""
    print("Testing with list 1- random elements")
    lst1 = get_list1(n)
    lst2 = lst1[:]
    lst3 = lst1[:]
    lst4 = lst1[:]
    start = time()
    sorted_list = merge_sort.merge_sort(lst1)
    end = time()
    print("Merged sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = insertion_sort.insertion_sort(lst2)
    end = time()
    print("Insertion sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = quick_sort.quick_sort(lst3)
    end = time()
    print("Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = merge_quick_sort(lst4)
    end = time()
    print("Merge-Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    print("")


def test_compare_l2(n):
    """Test the speed of each algorithm using the get_list2() function to create a list of n length"""
    print("Testing with list 2 - repeated elements")
    lst1 = get_list2(n)
    lst2 = lst1[:]
    lst3 = lst1[:]
    lst4 = lst1[:]
    start = time()
    sorted_list = merge_sort.merge_sort(lst1)
    end = time()
    print("Merged sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = insertion_sort.insertion_sort(lst2)
    end = time()
    print("Insertion sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = quick_sort.quick_sort(lst3)
    end = time()
    print("Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = merge_quick_sort(lst4)
    end = time()
    print("Merge-Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    print("")


def test_compare_l3(n):
    """Test the speed of each algorithm using the get_list3() function to create a list of n length"""
    print("Testing with list 3 - overall increasing elements, not favorable to quick sort")
    lst1 = get_list3(n)
    lst2 = lst1[:]
    lst3 = lst1[:]
    lst4 = lst1[:]
    start = time()
    sorted_list = merge_sort.merge_sort(lst1)
    end = time()
    print("Merged sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = insertion_sort.insertion_sort(lst2)
    end = time()
    print("Insertion sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = quick_sort.quick_sort(lst3)
    end = time()
    print("Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = merge_quick_sort(lst4)
    end = time()
    print("Merge-Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    print("")


def test_compare_l4(n):
    """Test the speed of each algorithm using the get_list4() function to create a list of n length"""
    print("Testing with list 4 - not favorable to quick sort")
    lst1 = get_list4(n)
    lst2 = lst1[:]
    lst3 = lst1[:]
    lst4 = lst1[:]
    start = time()
    sorted_list = merge_sort.merge_sort(lst1)
    end = time()
    print("Merged sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = insertion_sort.insertion_sort(lst2)
    end = time()
    print("Insertion sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = quick_sort.quick_sort(lst3)
    end = time()
    print("Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    start = time()
    sorted_list = merge_quick_sort(lst4)
    end = time()
    print("Merge-Quick sort elapsed time: ", "%.9f" % (end - start), " seconds")
    print("")


def test_compare():
    """Runs each of the test_compare_#() functions and sets n to 10000"""
    n = 10000
    print("")
    print("Time comparison test begins.")
    print("All lists used in this test are of length", n)
    print("")
    test_compare_l1(n)
    test_compare_l2(n)
    test_compare_l3(n)
    test_compare_l4(n)
    print("Time comparison test ends.")


def main():
    """Main function for running the test_merge_quick_sort() function and the test_compare() function"""
    test_merge_quick_sort()
    test_compare()


# Checks to see if being run as a file or as a library
if __name__ == '__main__':
    main()
