from random import shuffle
from typing import List, Union
from copy import deepcopy

Numeric = Union[int, float]
Vector = List[Numeric]


def bogo_sort(elements: Vector) -> Vector:
    elements_copy = deepcopy(elements)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, len(elements_copy)):
            previous = elements_copy[i - 1]
            current = elements_copy[i]

            if previous > current:
                is_sorted = False
                shuffle(elements_copy)
                break

    return elements_copy
