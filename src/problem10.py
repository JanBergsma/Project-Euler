from math import sqrt
if __name__ == "__main__":
    from problem7 import is_prime
else:
    from src.problem7 import is_prime


def sum_primes_below(n):
    """
    Summation of primes

    Problem 10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    >>> sum_primes_below(10)
    17
    """
    return sum(primes(n))


def primes(n=100):
    i, odd_i = 0, 2
    while odd_i < n:
        if is_prime(odd_i):
            yield odd_i
        i += 1
        odd_i = 2 * i + 1


def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):     # Mark factors non-prime
                a[n] = False


def sum_primes_below2(n):
    return sum(primes_sieve(n))


def sieve_of_eratosthenes(limit):
    if limit < 2: return 0
    sieve_bound = (limit - 1) // 2 + 1
    sieve = [False] * sieve_bound
    crosslimit = (int(sqrt(limit)) - 1) // 2 + 1

    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                sieve[j] = True

    return 2 + sum(2 * i + 1 for i in range(1, sieve_bound) if not sieve[i])


def main(timning=False):
    print(sum_primes_below(10))
    print(sum_primes_below2(10))
    print(sum_primes_below(2_000_000))
    print(sum_primes_below2(2_000_000))
    print(sieve_of_eratosthenes(3_000_000))

    if not timning: return
    import timeit
    print(
        'sum_primes_below(2_000_000) ->',
        timeit.timeit(
            'sum_primes_below(2_000_000)',
            setup="from __main__ import sum_primes_below",
            number=100
        )
    )
    print(
        'sum_primes_below2(2_000_000) ->',
        timeit.timeit(
            'sum_primes_below2(2_000_000)',
            setup="from __main__ import sum_primes_below2",
            number=100
        )
    )
    print(
        'sieve_of_eratosthenes(2_000_000) ->',
        timeit.timeit(
            'sieve_of_eratosthenes(2_000_000)',
            setup="from __main__ import sieve_of_eratosthenes",
            number=100
        )
    )


if __name__ == "__main__":
    main(timning=False)
