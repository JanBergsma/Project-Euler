def sum_of_multiples_of_3_or_5(n):
    """
    Multiples of 3 and 5

    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    >>> sum_of_multiples_of_3_or_5(10)
    23
    """
    n = n - 1
    return (
        sum_divisible_by(3, n) +
        sum_divisible_by(5, n) -
        sum_divisible_by(15, n)
    )


def sum_divisible_by(d, n):
    p = n // d
    return d * (p * (p + 1)) // 2


def sum_of_multiples_of_3_or_5_brute_force(n):
    """
    Multiples of 3 and 5

    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    >>> sum_of_multiples_of_3_or_5_brute_force(10)
    23
    """
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)


def main():
    print(f'sum_of_multiples_of_3_or_5(10) = {sum_of_multiples_of_3_or_5(10)}')
    print(f'sum_of_multiples_of_3_or_5(1000) = {sum_of_multiples_of_3_or_5(1000)}')  # nopep8
    """
    see:
    https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000
    """
    counts = sum(3 * k for k in range(1, 334))  # count all threes
    counts += sum(5 * k for k in range(1, 200))  # count all fives
    counts -= sum(15 * k for k in range(1, 67))  # correct over counted 15 (3x5)  # nopep8
    print(f'sum_of_multiples_of_3_or_5(1000) = {sum_of_multiples_of_3_or_5(1000)}, counts = {counts}')  # nopep8

    print(f'sum_of_multiples_of_3_or_5(1) = {sum_of_multiples_of_3_or_5(1)}')  # nopep8
    print(f'sum_of_multiples_of_3_or_5(1_000) = {sum_of_multiples_of_3_or_5(1_000)}')  # nopep8
    print(f'sum_of_multiples_of_3_or_5(1_000_000) = {sum_of_multiples_of_3_or_5(1_000_000)}')  # nopep8
    print(f'sum_of_multiples_of_3_or_5(1_000_000_000) = {sum_of_multiples_of_3_or_5(1_000_000_000)}')  # nopep8


if __name__ == "__main__":
    main()
