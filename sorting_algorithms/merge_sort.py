from numbers import Number
from typing import List, Tuple


def split(elements: List[Number]) -> Tuple[List[Number], List[Number]]:
    middle_index = len(elements) // 2

    return elements[:middle_index], elements[middle_index:]


def merge(left: List[Number], right: List[Number]) -> List[Number]:
    sorted_elements = list()

    while left or right:
        if not left:
            sorted_elements += right
            right = []
        elif not right:
            sorted_elements += left
            left = []
        elif left[0] >= right[0]:
            sorted_elements.append(right.pop(0))
        else:
            sorted_elements.append(left.pop(0))

    return sorted_elements


def merge_sort(elements: List[Number]) -> List[Number]:
    if len(elements) <= 1:
        return elements

    left, right = split(elements)

    return merge(merge_sort(left), merge_sort(right))
