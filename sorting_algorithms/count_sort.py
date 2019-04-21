from typing import List


def count_sort(elements: List[int]) -> List[int]:
    elements_count = list()

    for e in elements:
        if e >= len(elements_count):
            elements_count += [0]*(e-len(elements_count)+1)

        elements_count[e] += 1

    sorted_elements = list()
    for i, c in enumerate(elements_count):
        sorted_elements += [i]*c

    return sorted_elements
