def sum_square_difference(n):
    """
    Sum square difference

    Problem 6
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    >>> sum_square_difference(10)
    2640
    """
    return n * (n - 1) * (n + 1) * (3 * n + 2) // 12


def sum_square_difference_bf(n):
    """
    Sum square difference

    Problem 6
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    >>> sum_square_difference_bf(10)
    2640
    """
    return (
        sum(i for i in range(1, n + 1))**2 -
        sum(i**2 for i in range(1, n + 1))
    )


def main():
    print(sum_square_difference(10))
    print(sum_square_difference(1))
    print(sum_square_difference(10))
    print(sum_square_difference(100))
    print(sum_square_difference(1000))
    print(sum_square_difference(10000))
    print(sum_square_difference(100000))
    print(sum_square_difference(1000000))


if __name__ == "__main__":
    main()
