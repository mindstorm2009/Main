"""
    File: spellotron.py
    Author: Nicholas Curl
    Description: project
"""

import sys
from words import *
from lines import *
from input_read import get_args

# Global Variables
LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"


def make_adjacent_letters():
    """Creates a dictionary with keys being the alphabet and the values being a list of adjacent keys"""
    adj = {}
    file = open(KEY_ADJACENCY_FILE, encoding="utf-8")
    for line in file:
        line.strip()
        keys = line.split()
        # Checks to see if the key is already in the dictionary
        if keys[0] not in adj:
            adj[keys[0]] = keys[1:]
        else:
            adj[keys[0]] += keys[1:]
    file.close()
    return adj


def make_dictionary():
    """Creates a dictionary of the english dictionary with keys being the first letter of the word capitals are included
    and values of the words that have the same starting letter and capitalization"""
    dictionary = {}
    file = open(LEGAL_WORD_FILE, encoding="utf-8")
    for line in file:
        line = line.strip()
        # Checks to see if key is already in the dictionary
        if line[0] not in dictionary:
            dictionary[line[0]] = [line]
        else:
            dictionary[line[0]] += [line]
    file.close()
    return dictionary


def correction(dictionary, adj_letters):
    """The main function to determine which mode to use"""
    args = get_args()
    """ Checks to see if there are too many arguments given and stops the program if it is true or if there are too few
    arguments"""
    if len(args) > 2:
        print("Too Many Arguments", file=sys.stderr)
        sys.exit()
    elif len(args) < 1:
        print("Too Few Arguments", file=sys.stderr)
        sys.exit()
    """ Determines which mode to use, if there one is not given or misspelled prints an error message and exits
     the program"""
    if args[0] == "words":
        words(args, dictionary, adj_letters)
    elif args[0] == "lines":
        lines(args, dictionary, adj_letters)
    else:
        print("Cannot determine method", file=sys.stderr)
        sys.exit()


def main():
    adj_letters = make_adjacent_letters()
    dictionary = make_dictionary()
    correction(dictionary, adj_letters)


if __name__ == '__main__':
    main()
