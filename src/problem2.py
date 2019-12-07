def a001076(n):
    """
    A001076 Denominators of continued fraction convergents to sqrt(5).

        t
    """
    a1, a2 = 1, 0
    for _ in range(n):
        a1, a2 = 4 * a1 + a2, a1
    return a2


def a014445(n):
    """
    A014445	Even Fibonacci numbers; or, Fibonacci(3*n).
    >>> a014445(4)
    144
    """
    return 2 * a001076(n)


def a001076_iter():
    """
    A001076 Denominators of continued fraction convergents to sqrt(5).

        a(n) = 4*a(n-1) + a(n-2), n > 1. a(0)=0, a(1)=1.
    """
    a1, a2 = 1, 0
    yield a2
    yield a1
    while True:
        a1, a2 = 4 * a1 + a2, a1
        yield a1


def a014445_iter(upper_bound=4_000_000):
    """
    A014445	Even Fibonacci numbers; or, Fibonacci(3*n).
    >>> sum(a014445_iter(4_000_000))
    4613732
    """
    for a in a001076_iter():
        aa = 2 * a
        if aa > upper_bound:
            break
        yield aa


A014445 = [
    0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578,
    14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074,
    86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288,
    117669030460994
]


def main():
    expected = sum(n for n in A014445 if n <= 4_000_000)
    result = sum(a014445_iter())
    print(f'expected = {expected}, result = {result}')

if __name__ == "__main__":
    main()
