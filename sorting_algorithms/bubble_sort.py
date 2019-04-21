from typing import List
from copy import deepcopy


def bubble_sort(elements: List[float]) -> List[float]:
    elements_copy = deepcopy(elements)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, len(elements_copy)):
            previous = i - 1
            current = i

            if elements_copy[previous] > elements_copy[current]:
                is_sorted = False
                elements_copy[previous], elements_copy[current] = elements_copy[current], elements_copy[previous]

    return elements_copy
