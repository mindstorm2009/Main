"""
    File: moving.py
    Author: Nicholas Curl
"""

from dataclasses import dataclass


@dataclass
class Box:
    __slots__ = 'content', 'capacity', 'remaining'
    content: list
    capacity: int
    remaining: int


@dataclass
class Item:
    __slots__ = 'name', 'weight'
    name: str
    weight: int


def make_boxes_and_items(filename):
    """Creates two lists one for the boxes using the Box data class and one for items using the Item data class"""
    file = open(filename)
    boxes = []
    items = []
    for line in file:
        if line[0].isdigit():
            box_list = line.split()
            for element in box_list:
                boxes += [Box([], int(element), int(element))]
        else:
            words = line.split()
            item = Item(words[0], int(words[1]))
            items += [item]
    file.close()
    return boxes, items


def swap(lst, i, j):
    """Swaps elements of a list from position i to position j of the imputed list"""
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def sort_ascending_items(items):
    """Sorts the items by weight in ascending order"""
    for mark in range(0, len(items)):
        n = 0
        temp = mark
        while True:
            # Checks to see if the maker term is greater than the previous term
            if items[temp].weight > items[temp - n].weight:
                swap(items, temp, temp - n)
                temp = temp - n
                n = 0
            if n == temp:
                break
            n += 1
    return items


def sort_boxes_ascending(boxes):
    """Sorts the boxes by the remaining capacity in ascending order"""
    for mark in range(0, len(boxes)):
        n = 0
        temp = mark
        while True:
            # Checks to see if the maker term is greater than the previous term
            if boxes[temp].remaining > boxes[temp - n].remaining:
                swap(boxes, temp, temp - n)
                temp = temp - n
                n = 0
            if n == temp:
                break
            n += 1
    return boxes


def sort_boxes_descending(boxes):
    """Sorts the boixes by the remaining capacity in descending order"""
    for mark in range(0, len(boxes)):
        n = 0
        temp = mark
        while True:
            # Checks to see if the maker term is less than the previous term
            if boxes[temp].remaining < boxes[temp - n].remaining:
                swap(boxes, temp, temp - n)
                temp = temp - n
                n = 0
            if n == temp:
                break
            n += 1
    return boxes


def greedy_strat1(filename):
    """Runs through the first greedy strategy"""
    boxes, items = make_boxes_and_items(filename)
    packed = False
    notpacked = []
    items = sort_ascending_items(items)
    for item in items:
        boxes = sort_boxes_ascending(boxes)
        for i in range(0, len(boxes)):
            if item.weight <= boxes[i].remaining:
                boxes[i].remaining = boxes[i].remaining - item.weight
                boxes[i].content += [item]
                packed = True
                break
            else:
                packed = False
        if packed == False:
            notpacked += [item]
    return boxes, notpacked


def packing(boxes, unpacked):
    """Checks the contents of each box and determines if every item was packed"""
    if unpacked == []:
        print("All items successfully packed into boxes")
        for i in range(0, len(boxes)):
            print("Box", i + 1, "of weight capacity", boxes[i].capacity, "contains:")
            for contents in boxes[i].content:
                print(" ", contents.name, "of weight", contents.weight)
    else:
        print("Unable to pack all items!")
        for i in range(0, len(boxes)):
            print("Box", i + 1, "of weight capacity", boxes[i].capacity, "contains:")
            for contents in boxes[i].content:
                print(" ", contents.name, "of weight", contents.weight)
        for remaining in unpacked:
            print(remaining.name, "of weight", remaining.weight, "got left behind.")


def greedy_strat2(filename):
    """Runs throuh the second greedy strategy"""
    boxes, items = make_boxes_and_items(filename)
    packed = False
    notpacked = []
    items = sort_ascending_items(items)
    for item in items:
        boxes = sort_boxes_descending(boxes)
        for i in range(0, len(boxes)):
            if item.weight <= boxes[i].remaining:
                boxes[i].remaining = boxes[i].remaining - item.weight
                boxes[i].content += [item]
                packed = True
                break
            else:
                packed = False
        if packed == False:
            notpacked += [item]
    return boxes, notpacked


def greedy_strat3(filename):
    """Runs though the third greedy strategy"""
    boxes, items = make_boxes_and_items(filename)
    packed = False
    notpacked = []
    items = sort_ascending_items(items)
    for item in items:
        for i in range(0, len(boxes)):
            if item.weight <= boxes[i].remaining:
                boxes[i].remaining = boxes[i].remaining - item.weight
                boxes[i].content += [item]
                packed = True
                break
            else:
                packed = False
        if packed == False:
            notpacked += [item]
    return boxes, notpacked


def main():
    """Executes the previous greedy strategies and checks to see if all the items have been packed"""
    filename = input("Enter data filename: ")
    print("\nResults from Greedy Strategy 1")
    boxes, unpacked = greedy_strat1(filename)
    packing(boxes, unpacked)
    boxes, unpacked = greedy_strat2(filename)
    print("\nResults from Greed Strategy 2")
    packing(boxes, unpacked)
    boxes, unpacked = greedy_strat3(filename)
    print("\nResults from Greed Strategy 3")
    packing(boxes, unpacked)


# Checks to see if being run as a file or library
if __name__ == '__main__':
    main()
