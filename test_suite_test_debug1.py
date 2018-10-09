from test_debug1 import *


def caesar_shift_0():
    test = caesar("FUNCTION", "FUNCTION")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_1():
    test = caesar("FUNCTION", "GVODUJPO")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_5():
    test = caesar("FUNCTION", "KZSHYNTS")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_10():
    test = caesar("FUNCTION", "PEXMDSYX")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_15():
    test = caesar("FUNCTION", "UJCRIXDC")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_20():
    test = caesar("FUNCTION", "ZOHWNCIH")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def caesar_shift_25():
    test = caesar("FUNCTION", "BQJYPEKJ")
    if test != -1:
        print("success", test)
    else:
        print("failed")


def main():
    caesar_shift_0()
    caesar_shift_1()
    caesar_shift_5()
    caesar_shift_10()
    caesar_shift_15()
    caesar_shift_20()
    caesar_shift_25()


main()
