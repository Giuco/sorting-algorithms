from copy import deepcopy
from numbers import Number
from random import shuffle
from typing import List


def bogo_sort(elements: List[Number]) -> List[Number]:
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
