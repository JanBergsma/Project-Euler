from math import sqrt
from functools import reduce
from operator import mul
from collections import Counter
from src.problem3 import factor_brute_force


def smallest_multiple(n):
    """
    Smallest multiple

    Problem 5
    2520 is the smallest number that can be divided by each of
    the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
    >>> smallest_multiple(10)
    2520
    """
    ps = {p: 1 for p in primes(n)}
    for i in range(2, n + 1):
        if i not in ps:
            c = Counter(factor_brute_force(i))
            for k, v in c.items():
                if v > ps[k]:
                    ps[k] = v

    return reduce(lambda v, t: v * t[0]**t[1], ps.items(), 1)


def smallest_multiple_(n):
    """
    Smallest multiple

    Problem 5
    2520 is the smallest number that can be divided by each of
    the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?
    """
    result = 1
    for i in range(1, n + 1):
        result = result * i // gcd(result, i)
    return result


def primes(upper_bound=100):
    if upper_bound < 2: return []
    primes = []
    i = 3
    j = int(sqrt(upper_bound))
    while i < upper_bound:
        if all(i % p != 0 for p in primes if p <= j):
            primes.append(i)
        i += 2
    return [2] + primes


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def main():
    print(f'primes(10) = {primes(10)}')
    print(f'primes(20) = {primes(20)}')
    print(f'smallest_multiple_(10) = {smallest_multiple_(10)} and should be 2520')  # nopep8
    print(f'smallest_multiple(10) = {smallest_multiple(10)} and should be 2520')  # nopep8
    print(f'smallest_multiple(20) = {smallest_multiple(20)} and should be 232792560')  # nopep8
    print(f'primes(100_000) = {primes(100_000)}')
    print(f'smallest_multiple(100_000) = {smallest_multiple(100_000)}')


if __name__ == "__main__":
    main()
