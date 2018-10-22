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
    file = open(filename)
    L = []
    for line in file:
        a, b = line.split(" ")
        b.strip()
        L += [int(b)]
    file.close()
    return L


def median_simple(L):
    lst = quick_sort(L)
    if len(lst) % 2 == 1:
        half = int(len(lst) // 2)
        return lst[half]
    else:
        half = int(len(lst) / 2)
        average = (lst[half - 1] + lst[half]) / 2
        return average


def distance(L, loc):
    accum = 0
    for element in L:
        accum += abs(loc - element)
    return accum

def elapsed_time_simple(filename):
    lst = create_list(filename)
    start = time()
    loc = median_simple(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time :", "%.20f" % (end - start), "seconds\n")


def main():
    filename = input("Enter data file: ")
    lst = create_list(filename)
    start = time()
    loc = median_simple(lst)
    dist = distance(lst, loc)
    end = time()
    print("Optimum new store location:", loc)
    print("Sum of distances to new store:", dist, "\n")
    print("Elapsed time :", "%.20f" % (end - start), "seconds")


if __name__ == '__main__':
    main()
