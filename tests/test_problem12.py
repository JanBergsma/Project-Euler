from src.problem12 import (
    A000217, find_first_triangle_number_with_divisors, triangle_number
)


def test_triangle_numbers():
    assert list(triangle_number(len(A000217))) == A000217


def test_find_first_triangle_number_with_divisors_500_should_be_76576500():
    find_first_triangle_number_with_divisors(500) == 76576500
