def find_pythagorean_triple(n):
    """
    Special Pythagorean triplet

    Problem 9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,
    a² + b² = c²
    For example, 3² + 4² = 9 + 16 = 25 = 5².

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    >>> find_pythagorean_triple(1000)
    (375, 200, 425)
    """
    for c in range(3, n + 1):
        for b in range(2, c):
            a = n - b - c
            if a > 0 and a**2 + b**2 == c**2:
                return a, b, c
    return 0, 0, 0


def main():
    a, b, c = find_pythagorean_triple(1000)
    print(f'a = {a}, b = {b} and c = {c}')

    print(f'a + b + c = {a + b + c} == 1000')
    print(f'a**2 + b**2 == c**2 => {a**2 + b**2} == {c**2}')
    print(f'a * b * c = {a * b * c}')


if __name__ == "__main__":
    main()
