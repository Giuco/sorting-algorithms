from copy import deepcopy
from numbers import Number
from random import shuffle
from typing import List


def is_sorted(elements: List[Number]) -> bool:
    for i in range(1, len(elements)):
        previous = elements[i - 1]
        current = elements[i]

        if previous > current:
            return False

    return True


def bogo_sort(elements: List[Number]) -> List[Number]:
    elements_copy = deepcopy(elements)

    while not is_sorted(elements_copy):
        shuffle(elements_copy)

    return elements_copy
