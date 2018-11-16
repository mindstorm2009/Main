"""
    File: input_read.py
    Author: Nicholas Curl
    Description: project
"""

import sys


def read_input(args):
    """Reads the input of the command line and checks to see if it is a file or directly from the command line"""
    word_list = []
    # Checks if it is a file or a command line input
    if len(args) < 2:
        text_source = sys.stdin
    else:
        print("Processing file ", args[1], "...", sep="")
        text_source = open(args[1])
    # Stores the input into a list
    for line in text_source:
        line = line.strip()
        word_list += [line.split()]
        if text_source == sys.stdin:
            break
    if text_source != sys.stdin:
        text_source.close()
    return word_list


def get_args():
    """Gets the arguments from the command line"""
    args = sys.argv
    return args[1:]
