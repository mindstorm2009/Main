"""
    File: selection_sort.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Creates a list from a given file and sorts it from lowest to highest
"""


# Definitions and functions to sort a list

def list_creator(filename):
    """Creates a list from an inputted file and strips whitespace before it is added to the list"""
    lst = []
    file = open(filename)
    for line in file:
        temp = line.strip()
        lst += [int(temp)]
    file.close()
    return lst


def swap(lst, i, j):
    """Swaps elements of a list from position i to position j of the imputed list"""
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def selection_sort(lst):
    """First prints the unsorted list and sorts the based on the marker term being less than the previous term and
    prints the sorted list"""
    print("Unsorted List:", lst)
    # Goes through the entire list
    for mark in range(0, len(lst)):
        n = 0
        temp = mark
        while True:
            # Checks to see if the maker term is less than the previous term
            if lst[temp] < lst[temp - n]:
                swap(lst, temp, temp - n)
                temp = temp - n
                n = 0
            if n == temp:
                break
            n += 1
    print("Sorted List:", lst)


def main():
    """Main function to run the program and prompt the user for a file to be sorted"""
    filename = input("What is the File Name: ")
    list_creator(filename)
    selection_sort(lst)


# Checks to see if being run as a file or being used as a library and runs the main() function if it is from the file
if __name__ == '__main__':
    main()
