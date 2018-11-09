"""
    File: tasks.py
    Author: Nicholas Curl
    Description: homework

"""


from dataclasses import dataclass
from priority_queue import *
from random import *


@dataclass
class Task:
    __slots__ = 'name', 'priority'
    name: str
    priority: int


def make_task(name, priority):
    """Makes an task"""
    return Task(name, priority)


def order_of_queue2(q, priority1, priority2, task1, task2):
    """Tests for checking the order of the queue of two elements"""
    print("Is Task 2 priority > Task 1 priority", priority2 > priority1)
    print("Is Task 2 priority < Task 1 priority", priority2 < priority1)
    print("Is Task 2 priority = Task 1 priority", priority2 == priority1)
    if priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
        return "priority2"
    elif priority1 > priority2:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
        return "priority1"
    elif priority1 == priority2:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
        return "Both"


def order_of_queue3(q, priority1, task1, priority2, task2, priority3, task3):
    """Tests for checking the order of the queue of three elements"""
    print("Is Task 3 priority > Task 1 priority", priority3 > priority1)
    print("Is Task 3 priority < Task 1 priority", priority3 < priority1)
    print("Is Task 3 priority = Task 1 priority", priority3 == priority1)
    print("Is Task 3 priority > Task 2 priority", priority3 > priority2)
    print("Is Task 3 priority < Task 2 priority", priority3 < priority2)
    print("Is Task 3 priority = Task 2 priority", priority3 == priority2)
    if priority1 < priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority2 < priority1 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority1 < priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority3 < priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority2 < priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority3 < priority2 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority1 < priority2 == priority3:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority3 == priority2 < priority1:
        print("front is Task('Task 1',", priority2, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority2 < priority1 == priority3:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority3 == priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority1 == priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority1, ")? ", task2 == back(q), sep="")
    elif priority1 == priority2 > priority3:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority1 == priority2 == priority3:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")


def priority4_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4):
    """Tests for checking the order of the queue if the fourth element is the front element"""
    if priority1 < priority2 < priority3 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority3 < priority2 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority2 == priority3 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority2 < priority1 < priority3 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority3 < priority1 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority1 == priority3 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority1 == priority2 < priority3 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority3 < priority1 < priority2 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority2 < priority1 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority2 < priority1 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority1 < priority2 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority1 == priority2 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority1 == priority2 < priority4:
        print("front is Task('Task 4',", priority4, ")? ", task4 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")


def priority3_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4):
    """Tests for checking the order of the queue if the third element is the front element"""
    if priority1 < priority2 < priority4 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority4 < priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority2 == priority4 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority2 < priority4 == priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority2 < priority1 < priority4 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority4 < priority1 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority1 == priority4 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority1 == priority2 < priority4 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 == priority1 < priority4 == priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority1 < priority4 == priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority4 < priority2 < priority1 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority1 < priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority2 == priority1 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority1 == priority4 == priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority1 < priority2 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority2 < priority1 < priority3:
        print("front is Task('Task 3',", priority3, ")? ", task3 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")


def priority2_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4):
    """Tests for checking the order of the queue if the second element is the front element"""
    if priority1 < priority3 < priority4 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority4 < priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority4 == priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority4 == priority3 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority4 < priority3 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority1 < priority3 < priority4 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    elif priority3 < priority1 < priority4 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority4 < priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority1 == priority4 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority1 < priority4 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority1 < priority4 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority1 < priority4 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority1 < priority4 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority4 < priority3 < priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority1 < priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority3 == priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority1 == priority4 == priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority3 < priority1 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority1 < priority3 < priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority1 < priority3 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority1 < priority3 == priority2:
        print("front is Task('Task 2',", priority2, ")? ", task2 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")


def priority1_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4):
    """Tests for checking the order of the queue if the first element is the front element"""
    if priority2 < priority3 < priority4 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority4 < priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority4 == priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority4 == priority3 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority4 < priority3 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority2 < priority3 < priority4 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 2',", priority2, ")? ", task2 == back(q), sep="")
    elif priority3 < priority2 < priority4 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority4 < priority2 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority2 == priority4 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority2 < priority4 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority4 == priority2 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 == priority2 < priority4 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority2 < priority4 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority3 < priority4 < priority2 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 3',", priority3, ")? ", task3 == back(q), sep="")
    elif priority4 < priority3 < priority2 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority2 < priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority3 == priority2 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority2 == priority4 == priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority1 == priority2 == priority3 == priority4:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority2 < priority3 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority2 < priority3 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority3 < priority2 < priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority3 == priority2 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority2 < priority3 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority2 < priority3 == priority4:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 < priority3 < priority2 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")
    elif priority4 == priority3 < priority2 == priority1:
        print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
        print("back is Task('Task 4',", priority4, ")? ", task4 == back(q), sep="")


def order_of_queue4(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4):
    """Tests for checking the order of the queue of four elements"""
    print("Is Task 4 priority > Task 1 priority", priority4 > priority1)
    print("Is Task 4 priority < Task 1 priority", priority4 < priority1)
    print("Is Task 4 priority = Task 1 priority", priority4 == priority1)
    print("Is Task 4 priority > Task 2 priority", priority4 > priority2)
    print("Is Task 4 priority < Task 2 priority", priority4 < priority2)
    print("Is Task 4 priority = Task 2 priority", priority4 == priority2)
    print("Is Task 4 priority > Task 3 priority", priority4 > priority3)
    print("Is Task 4 priority < Task 3 priority", priority4 < priority3)
    print("Is Task 4 priority = Task 3 priority", priority4 == priority3)
    priority4_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4)
    priority3_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4)
    priority2_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4)
    priority1_conditions(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4)


def main():
    """Tests the the priority_queue implementation"""
    # begin with empty queue
    q = make_priority_queue()
    print("Creating empty queue...")
    print("Queue empty?", is_empty(q) is True)
    print("Queue size is 0?", 0 == q.size)
    # add first element
    priority1 = randint(0, 10)
    print("enqueue Task('Task 1',", priority1, ")", sep="")
    task1 = make_task("Task 1", priority1)
    enqueue(q, task1)
    print("Queue not empty?", is_empty(q) is False)
    print("Queue size is 1?", 1 == q.size)
    print("front is Task('Task 1',", priority1, ")? ", task1 == front(q), sep="")
    print("back is Task('Task 1',", priority1, ")? ", task1 == back(q), sep="")
    # add second element
    priority2 = randint(0, 10)
    print("\nenqueue Task('Task 2',", priority2, ")", sep="")
    task2 = Task("Task 2", priority2)
    enqueue(q, task2)
    order_of_queue2(q, priority1, priority2, task1, task2)
    # add third element
    priority3 = randint(0, 10)
    print("\nenqueue Task('Task 3',", priority3, ")", sep="")
    task3 = Task("Task 3", priority3)
    enqueue(q, task3)
    order_of_queue3(q, priority1, task1, priority2, task2, priority3, task3)
    # add fourth element
    priority4 = randint(0, 10)
    print("\nenqueue Task('Task 4',", priority4, ")", sep="")
    task4 = Task("Task 4", priority4)
    enqueue(q, task4)
    order_of_queue4(q, priority1, task1, priority2, task2, priority3, task3, priority4, task4)
    # Empty the queue
    print("\nEmptying the queue...")
    while not is_empty(q):
        print("Front of stack:", front(q))
        print("Back of stack:", back(q))
        print("dequeue...")
        dequeue(q)


if __name__ == '__main__':
    main()
