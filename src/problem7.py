from math import sqrt


def nth_prime(n):
    """
    10001st prime

    Problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number
    >>> nth_prime(6)
    13
    """
    return max(primes(n))


def primes(n=100):
    if n > 0: yield 2
    else: yield 0
    i, number_of_primes = 0, 1
    while number_of_primes < n:
        i += 1
        odd_i = 2 * i + 1
        if is_prime(odd_i):
            number_of_primes += 1
            yield odd_i


def is_prime(p):
    if p < 2: return False
    if p == 2 or p == 3: return True
    if p % 2 == 0 or p % 3 == 0: return False
    return all(p % i and p % (i + 2) for i in range(5, int(sqrt(p)) + 1, 6))


def main():
    print(f'nth_rime(6) = {nth_prime(6)}')
    print(f'nth_rime(10_001) = {nth_prime(10_001)}')
    print(f'primes(10_001) = {list(primes(10_001))}')

if __name__ == "__main__":
    main()
