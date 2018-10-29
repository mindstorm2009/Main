"""
    File: anagram.py
    Author: Nicholas Curl
"""


def convert_file_to_lex():
    """Opens the american-english.txt encoded as utf-8 and creates a dictionary of keys that are lexicographically
    sorted and for each value that is the same as the key store it under that key"""
    file = open("american-english.txt", encoding="utf-8")
    lex = {}
    chars = []
    conv = ""
    for line in file:
        line = line.strip()
        for char in line:
            chars += [ord(char)]
            chars.sort()
        for val in chars:
            conv += chr(val)
        if conv not in lex:
            lex[conv] = [line]
        else:
            lex[conv] += [line]
        chars = []
        conv = ""
    return lex


def convert_to_lex(word):
    """Converts an inputted string lexicographically"""
    chars = []
    conv = ""
    word = word.strip()
    for char in word:
        chars += [ord(char)]
        chars.sort()
    for val in chars:
        conv += chr(val)
    return conv


def task3(dictionary, length):
    """Runs through all the keys that are of length length and determines the maximum anagrams of that are of length
    length"""
    counter = 0
    lst = []
    for keys in dictionary:
        if len(keys) == length:
            if len(dictionary[keys]) > counter:
                counter = len(dictionary[keys])
                lst = dictionary[keys]
    return lst


def task4(dictionary, length):
    """Runs through the keys of length length to determine the number of good jumble words"""
    counter = 0
    for keys in dictionary:
        if len(keys) == length:
            if len(dictionary[keys]) == 1:
                counter += 1
    return counter


def main():
    """The main function to prompt the user for each task and for creating the dictionary as well"""
    dictionary = convert_file_to_lex()
    indict = False
    while True:
        word = input("Enter input string (hit enter key to go to task 3): ")
        if word == "":
            length = input("Enter word length (hit enter key to go to task 4): ")
            if length == "":
                length = input("Enter word length (hit enter key to quit): ")
                if length == "":
                    break
                else:
                    length = int(length)
                    words = task4(dictionary, length)
                    print("Number of jumble usable words of length", length, ":", words)
            else:
                length = int(length)
                lst = task3(dictionary, length)
                print("Max anagrams for length", length, ":", len(lst))
                print("Anagram list:", lst)
        else:
            lex = convert_to_lex(word)
            for keys in dictionary:
                if lex == keys:
                    print("Corresponding Words:", dictionary[lex])
                    indict = True
                    break
                else:
                    indict = False
            if not indict:
                print("No words can be formed from:", word)


if __name__ == '__main__':
    main()
