
from store_location import *
from select_median import *


def test_compare_file1(n):
    """Runs each function to test the total time to find the optimal location and the sum of the distances to the
    optimal location from the test500Keven.txt file and runs each test n number of times"""
    print("Simple Median Tests- File 1\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_simple("test500Keven.txt")
    print("Quick Select Median Tests- File 1\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_quickselect("test500Keven.txt")


def test_compare_file2(n):
    """Runs each function to test the total time to find the optimal location and the sum of the distances to the
    optimal location from the test500Kodd.txt file and runs each test n number of times"""
    print("Simple Median Tests- File 2\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_simple("test500Kodd.txt")
    print("Quick Select Median Tests- File 2\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_quickselect("test500Kodd.txt")


def test_compare_file3(n):
    """Runs each function to test the total time to find the optimal location and the sum of the distances to the
        optimal location from the test_dataset_large.txt file and runs each test n number of times"""
    print("Simple Median Tests- File 3\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_simple("test_dataset_large.txt")
    print("Quick Select Median Tests- File 3\n")
    for i in range(n):
        print("Test ", i + 1)
        elapsed_time_quickselect("test_dataset_large.txt")


def main():
    """The main function to run each of the test comparisons and prompts the user for the number of tests to run for
    each file"""
    n = int(input("How many runs of the implementation to run: "))
    test_compare_file1(n)
    test_compare_file2(n)
    test_compare_file3(n)


main()
