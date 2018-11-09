from dataclasses import dataclass
from typing import Union
from node import *


@dataclass
class PriorityQueue:
    __slots__ = 'size', 'front', 'back'
    size: int
    front: Union[None, Node]
    back: Union[None, Node]


def make_priority_queue():
    return PriorityQueue(0, None, None)


def nodes_by_priority(nodes, element):
    if nodes is None:
        node = Node(element, None)
        return node
    else:
        if element.priority < nodes.value.priority:
            return Node(nodes.value, nodes_by_priority(nodes.rest, element))
        elif element.priority == nodes.value.priority:
            return Node(nodes.value, nodes_by_priority(nodes.rest, element))
        else:
            return Node(element, nodes)


def get_end(nodes):
    if nodes.rest is None:
        return nodes.value
    else:
        return get_end(nodes.rest)


def enqueue(queue, element):
    nodes = queue.front
    newnode = Node(element, None)
    if is_empty(queue):
        queue.front = newnode
        nodes = queue.front
    else:
        queue.front = nodes_by_priority(nodes, element)
        nodes = queue.front
    queue.back = Node(get_end(nodes), None)
    queue.size = queue.size + 1


def dequeue(queue):
    """
        Remove the front element from the queue. (returns removed value)
        precondition: queue is not empty.
        """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed


def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value


def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value


def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed


def is_empty(queue):
    """
    Is the queue empty?
    """
    return queue.front == None
