from numbers import Number
from typing import List


class PriorityQueue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx: Number):
        if idx < 1:
            raise IndexError
        return self.items[idx - 1]

    def __setitem__(self, key, value):
        self.items[key - 1] = value

    def insert(self, item: Number):
        self.items.append(item)
        self.sift_up(self.__len__())

    def get_child(self, idx):
        if idx is None:
            return None, None

        children_a_idx = idx * 2
        children_b_idx = (idx * 2) + 1

        if children_a_idx > self.__len__():
            return None, None
        elif children_b_idx > self.__len__():
            return children_a_idx, None
        else:
            return children_a_idx, children_b_idx

    def get_parent(self, idx):
        if idx == 1:
            return 1
        return idx // 2

    def sift_up(self, idx):
        while True:
            parent_idx = self.get_parent(idx)
            if self[idx] < self[parent_idx] or idx == 1:
                break
            else:
                self[idx], self[parent_idx] = self[parent_idx], self[idx]
                idx = parent_idx

    def extract_max(self):
        max_value = self[1]
        self[1] = self[self.__len__()]
        self.items.pop(-1)
        self.sift_down(1)
        return max_value

    def sift_down(self, idx):
        if self.__len__() > 0:
            while True:
                children_a_idx, children_b_idx = self.get_child(idx)
                if children_a_idx is not None:
                    children_a = self[children_a_idx]
                else:
                    children_a = None

                if children_b_idx is not None:
                    children_b = self[children_b_idx]
                else:
                    children_b = None

                value = self[idx]

                if children_a is not None and children_b is None and children_a >= value:
                    self[idx], self[children_a_idx] = self[children_a_idx], self[idx]
                    idx = children_a_idx
                elif children_a is not None and children_b is not None and children_a >= children_b and children_a >= value:
                    self[idx], self[children_a_idx] = self[children_a_idx], self[idx]
                    idx = children_a_idx
                elif children_a is not None and children_b is not None and children_b >= children_a and children_b >= value:
                    self[idx], self[children_b_idx] = self[children_b_idx], self[idx]
                    idx = children_b_idx
                else:
                    break


def heap_sort(elements: List[Number]) -> List[Number]:
    """
    >>> heap_sort([1, 2, 3])
    [3, 2, 1]

    >>> heap_sort([1, 4, 6, 32, 0, 7, 6])
    [32, 7, 6, 6, 4, 1, 0]

    >>> heap_sort([-1, 0, 2, 3, 5, 32, 1,2, -23])
    [32, 5, 3, 2, 2, 1, 0, -1, -23]
    """
    heap = PriorityQueue()
    [heap.insert(e) for e in elements]
    return [heap.extract_max() for _ in elements]
