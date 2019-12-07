import pytest
from src.problem5 import smallest_multiple

TESTS = [
    ('smallest multiple of 2 should be 1', 1, 1),
    ('smallest multiple of 10 should be 2520', 10, 2520),
    ('smallest multiple of 20 should be 232792560', 20, 232792560),
]


@pytest.mark.parametrize(
    "name, n, expected",
    TESTS, ids=[test[0] for test in TESTS])
def test_smallest_multiple(name, n, expected):
    assert smallest_multiple(n) == expected
