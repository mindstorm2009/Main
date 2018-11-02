"""
file: linked_insort.py
author: your name here
description: homework
"""

import linked_code


def insert(value, lnk):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    lnk
    if lnk is None:
        return linked_code.LinkNode(value, None)
    if lnk.value < value:
        return linked_code.LinkNode(lnk.value, insert(value, lnk.rest))
    if lnk.value > value:
        return linked_code.LinkNode(value, lnk)

    # return None  # Change this line, too.


def insort(lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    # YOUR CODE HERE
    length = linked_code.length_iter(lnk)
    for mark in range(length - 1):
        index = mark
        while index > -1 and linked_code.value_at(lnk, index) > linked_code.value_at(lnk, index + 1):
            value = linked_code.value_at(lnk, index)
            lnk = linked_code.remove_at(index, lnk)
            lnk = insert(value, lnk)
            index -= 1
        index = mark
        if linked_code.value_at(lnk, index) < linked_code.value_at(lnk, index + 1):
            value = linked_code.value_at(lnk, index)
            lnk = linked_code.remove_at(index, lnk)
            lnk = insert(value, lnk)
    return lnk

    # return None  # Change this line, too.


def pretty_print(lnk):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    lst = []
    while lnk is not None:
        lst += [lnk.value]
        lnk = lnk.rest
    print(lst)
    # YOUR CODE HERE
