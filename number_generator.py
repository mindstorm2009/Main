from random import *


def num_creator(filename):
    count = int(input("number of numbers: "))
    file = open(filename, "w+")
    for n in range(0, count):
        num = randint(0, 10000)
        file.write("%d\n" % num)
    file.close()


def main():
    filename = input("Filename: ")
    num_creator(filename)


if __name__ == '__main__':
    main()
