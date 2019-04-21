from random import randint, random
from sorting_algorithms import selection_sort

NUMBER_OF_TESTS = 500
ARRAY_MAX_LEN = 1000
MAX_INT_ARRAY = 10000


def test_selection_sort_integer():
    for _ in range(NUMBER_OF_TESTS):
        array_size = randint(0, ARRAY_MAX_LEN)
        array = [randint(-MAX_INT_ARRAY, MAX_INT_ARRAY) for _ in range(array_size)]

        assert selection_sort(array) == sorted(array)


def test_selection_sort_float():
    for _ in range(NUMBER_OF_TESTS):
        array_size = randint(0, ARRAY_MAX_LEN)
        array = [randint(-MAX_INT_ARRAY, MAX_INT_ARRAY) - random() for _ in range(array_size)]

        assert selection_sort(array) == sorted(array)


def test_selection_sort_float_int_mixed():
    for _ in range(NUMBER_OF_TESTS):
        array_size = randint(0, ARRAY_MAX_LEN)
        array = [
            (randint(-MAX_INT_ARRAY, MAX_INT_ARRAY) -
             (0 if random() < .5 else random()))
            for _ in range(array_size)
        ]

        assert selection_sort(array) == sorted(array)
