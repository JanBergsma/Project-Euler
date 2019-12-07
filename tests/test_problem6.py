import pytest
from src.problem6 import sum_square_difference, sum_square_difference_bf


def test_sum_square_difference_for_10_should_be_240():
    assert sum_square_difference(10) == 2640


TESTS = list((f'n = {n}', n) for n in range(101))


@pytest.mark.parametrize(
    "name, n",
    TESTS, ids=[test[0] for test in TESTS])
def test_stress(name, n):
    assert sum_square_difference(n) == sum_square_difference_bf(n)


def test_stress1():
    assert all(sum_square_difference(n) == sum_square_difference_bf(n)
               for n in range(101))
