from math import sqrt


def sieve_of_eratosthenes(limit):
    if limit < 2: return
    sieve_bound = (limit - 1) // 2 + 1
    sieve = [False] * sieve_bound
    crosslimit = (int(sqrt(limit)) - 1) // 2 + 1

    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
                sieve[j] = True

    yield 2

    for i in range(1, sieve_bound):
        if not sieve[i]:
            yield 2 * i + 1


def mersennne_numbers(number=5):
    for p in sieve_of_eratosthenes(number):
        p = 2**p - 1
        yield p


def factor_brute_force(x):
    roots = []
    for i in sieve_of_eratosthenes(int(sqrt(x)) + 1):
        while x > 1 and x % i == 0:
            x = x // i
            roots.append(i)
    if x > 1:
        roots.append(x)
    return roots


def is_prime(p):
    if p < 2: return False
    if p == 2 or p == 3: return True
    if p % 2 == 0 or p % 3 == 0: return False
    return all(p % i and p % (i + 2) for i in range(5, int(sqrt(p)) + 1, 6))


def aks(p):
    """
        AKS primality test
    """

    if p == 2: return True
    c = 1
    for i in range(p // 2 + 1):
        c = c * (p - i) // (i + 1)
        if c % p: return False
    return True


first_100_primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]

print(max(sieve_of_eratosthenes(2_000_000)))
# assert list(sieve_of_eratosthenes(100)) == first_100_primes
# print(list(mersennne_numbers(100)))
# print([i for i in mersennne_numbers(60) if is_prime(i)])
# import timeit
# print(
#     'is_prime(1999) ->',
#     timeit.timeit(
#         'is_prime(1999)',
#         setup="from __main__ import is_prime",
#         number=1000
#     )
# )
# print(
#     'aks(1999) ->',
#     timeit.timeit(
#         'aks(1999)',
#         setup="from __main__ import aks",
#         number=1000
#     )
# )
# print(
#     'is_prime(2047) ->',
#     timeit.timeit(
#         'is_prime(1999)',
#         setup="from __main__ import is_prime",
#         number=1000
#     )
# )
# print(
#     'aks(2047) ->',
#     timeit.timeit(
#         'aks(1999)',
#         setup="from __main__ import aks",
#         number=1000
#     )
# )

# print(
#     'is_prime(1999993) ->',
#     timeit.timeit(
#         'is_prime(1999993)',
#         setup="from __main__ import is_prime",
#         number=10000
#     )
# )
# print(
#     'aks(1299007) ->',
#     timeit.timeit(
#         'aks(1299007)',
#         setup="from __main__ import aks",
#         number=1
#     )
# )
