"""
file: test_link_sort.py
author: your name here
description: tester for functions in linked_insort.py
"""

import linked_insort as linked_insort_sol
from dataclasses import dataclass
from typing import Any, Union
import linked_code


@dataclass(frozen=True)
class Node:
    __slots__ = 'value', 'rest'
    value: Any
    rest: Union[None, 'Node']


def read_file(fname):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """
    file = open(fname)
    line1 = file.readline()
    line1.strip()
    if line1 =="":
        return None
    lnk = Node(int(line1), None)
    for line in file:
        line.strip()
        lnk = Node(int(line), lnk)
    lnk = linked_code.reverse_iter(lnk)
    file.close()
    return lnk  # Replace this line, too.


def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input("Enter file name: ")
    if name == "":
        return

    original_s = read_file(name)
    if original_s is not None:
        print("unsorted:", original_s)
        sorted_s = linked_insort_sol.insort(original_s)
        print("sorted:", sorted_s)

        print("pretty printed original: ", end="")
        linked_insort_sol.pretty_print(original_s)
        print("pretty printed sorted: ", end="")
        linked_insort_sol.pretty_print(sorted_s)
    else:
        print("Value not given")




if __name__ == "__main__":
    main()
