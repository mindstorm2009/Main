"""
    File: store_location.py
    Author: Nicholas Curl
"""


from time import *


# Uses the same code from quick_sort.py
def quick_sort(L):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        (less, same, more) = partition(pivot, L)
        return quick_sort(less) + same + quick_sort(more)


def partition(pivot, L):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    less, same, more = ([], [], [])
    for e in L:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return less, same, more


# New Code
def create_list(filename):
    """Creates a list from a given file"""
    file = open(filename)
    L = []
    for line in file:
        a, b = line.split(" ")
        b.strip()
        L += [int(b)]
    file.close()
    return L


def median_simple(L):
    """Uses the quicksort algorithm to sort the list then choose the median values, calculates the average of the middle
    two values if the list is even"""
    lst = quick_sort(L)
    # Checks to see if the list is even
    if len(lst) % 2 == 1:
        half = int(len(lst) // 2)
        return lst[half]
    else:
        half = int(len(lst) / 2)
        average = (lst[half - 1] + lst[half]) / 2
        return average


def distance(L, loc):
    """Calculates the distance of each location in relation to the median store and calculates the sum of those
    distances"""
    accum = 0
    for element in L:
        accum += abs(loc - element)
    return accum

def elapsed_time_simple(filename):
    """Runs the elapsed time to figure out the median value as well as the sum of the distances to the target store"""
    lst = create_list(filename)
    start = time()
    loc = median_simple(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time :", "%.20f" % (end - start), "seconds\n")


def main():
    """Main function to execute the best location and the distance.  It also calculates the time to accomplish these
    functions"""
    filename = input("Enter data file: ")
    lst = create_list(filename)
    start = time()
    loc = median_simple(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time :", "%.20f" % (end - start), "seconds")

# Checks to see if being run as a file or as a library and executes the main() function if being run as a file
if __name__ == '__main__':
    main()
