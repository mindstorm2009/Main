from dataclasses import dataclass


@dataclass
class Box:
    __slots__ = 'content', 'capacity'
    content: list
    capacity: int


@dataclass
class Item:
    __slots__ = 'name', 'weight'
    name: str
    weight: int


def make_boxes_and_items(filename):
    file = open(filename)
    boxes = []
    items = []
    for line in file:
        if line[0].isdigit():
            box_list = line.split()
            for element in box_list:
                print(element)
                boxes += [Box([], int(element))]
        else:
            words = line.split()
            item = Item(words[0], int(words[1]))
            items += [item]
    file.close()
    return boxes, items
def sort_ascending_items(items):

def greedy_strart1(boxes, items)
def main():
    filename = input("Enter data filename: ")
    boxes, items = make_boxes_and_items(filename)
    print(boxes)
    print(items)

main()