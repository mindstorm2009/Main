from random import *


def num_creator_file(filename):
    count = int(input("number of numbers: "))
    limit = int(input("Upper Limit: "))
    file = open(filename, "w+")
    for n in range(0, count):
        num = randint(0, limit)
        file.write("%d\n" % num)
    file.close()


def num_creator_list():
    count = int(input("Number of Numbers: "))
    limit = int(input("Upper Limit: "))
    lst = []
    for n in range(0, count):
        num = randint(0, limit)
        lst += [num]
    return lst


def main():
    filename = input("Filename: ")
    num_creator_file(filename)


if __name__ == '__main__':
    main()
