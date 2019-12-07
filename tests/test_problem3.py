from src.problem3 import largest_prime_factor, factor_brute_force


def test_factor_brute_force():
    assert factor_brute_force(13195) == [5, 7, 13, 29]


def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29


def test_largest_prime_factor_for_600851475143():
    assert largest_prime_factor(600851475143) == 6857
