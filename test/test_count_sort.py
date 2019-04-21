from random import randint
from sorting_algorithms import count_sort

NUMBER_OF_TESTS = 500
ARRAY_MAX_LEN = 100
MAX_INT_ARRAY = 100


def test_count_sort_integer():
    for _ in range(NUMBER_OF_TESTS):
        array_size = randint(0, ARRAY_MAX_LEN)
        array = [randint(0, MAX_INT_ARRAY) for _ in range(array_size)]

        assert count_sort(array) == sorted(array)
