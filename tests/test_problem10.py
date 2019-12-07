import pytest

from src.problem10 import (
    sum_primes_below, sum_primes_below2, sieve_of_eratosthenes
)


def test_sum_primes_below_10_should_be_17():
    assert sum_primes_below(10) == 17


@pytest.mark.skip(reason="slow")
def test_sum_primes_below_2_000_000_should_be_142_913_828_922():
    assert sum_primes_below(2_000_000) == 142_913_828_922


def test_sum_primes_below2_10_should_be_17():
    assert sum_primes_below2(10) == 17


@pytest.mark.skip(reason="slow")
def test_sum_primes_below2_2_000_000_should_be_142_913_828_922():
    assert sum_primes_below2(2_000_000) == 142_913_828_922


def test_sieve_of_eratosthenes_10_should_be_17():
    assert sieve_of_eratosthenes(10) == 17


@pytest.mark.skip(reason="slow")
def test_sieve_of_eratosthenes_2_000_000_should_be_142_913_828_922():
    assert sieve_of_eratosthenes(2_000_000) == 142_913_828_922
