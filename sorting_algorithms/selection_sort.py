from typing import List, Union
from copy import deepcopy


def selection_sort(elements: List[Union[float, int]]) -> List[Union[float, int]]:

    elements_copy = deepcopy(elements)

    for i in range(len(elements_copy)):
        smallest_number_index = i
        smallest_number = elements_copy[i]

        for e in range(i, len(elements_copy)):
            if elements_copy[e] < smallest_number:
                smallest_number_index = e
                smallest_number = elements_copy[e]

        elements_copy[smallest_number_index] = elements_copy[i]
        elements_copy[i] = smallest_number

    return elements_copy

