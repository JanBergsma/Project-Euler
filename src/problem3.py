from math import sqrt


def largest_prime_factor(i):
    """Largest prime factor

    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.


    What is the largest prime factor of the number 600851475143 ?
    >>> largest_prime_factor(13195)
    29
    """
    return max(factor_brute_force(i))


def factor_brute_force(x):
    """]
    Brute force integer factorizing.

    Arguments:
        x {[Integer}-- an Natural number

    Returns:
        [Integer] -- the factors of x

    >>> factor_brute_force(13195)
    [5, 7, 13, 29]
    """
    roots = []
    for i in range(2, int(sqrt(x) + 1)):
        while x > 1 and x % i == 0:
            x = x // i
            roots.append(i)
    if x > 1:
        roots.append(x)
    return roots


def main():
    print(f'factor_brute_force(13195) = {factor_brute_force(13195)}')
    print(f'factor_brute_force(600851475143) = {factor_brute_force(600851475143)}')  # nopep8
    print(f'largest_prime_factor(13195) = {largest_prime_factor(13195)}')
    print(f'largest_prime_factor(600851475143) = {largest_prime_factor(600851475143)}')  # nopep8


if __name__ == "__main__":
    main()
