def largest_palindrome_product(number_of_digits):
    """
    Problem 4
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    A002113 Palindromes in base 10.

    >>> largest_palindrome_product(3)
    906609
    """
    max_palindrone = -1

    n = sum(9 * 10**i for i in range(number_of_digits))
    m = n // 11 * 11

    for i in range(n, n // 10, -1):
        n1 = m if i % 11 else n
        st = -11 if i % 11 else -1
        for j in range(n1, i - 1, st):
            ij = i * j
            if ij > max_palindrone and _is_palindrome(ij):
                max_palindrone = ij
    return max_palindrone


def largest_palindrome_product_bf(number_of_digits):
    """
    Problem 4
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    A002113 Palindromes in base 10.
    >>> largest_palindrome_product_bf(2)
    9009
    """
    max_number_in_digits = int(''.join('9' for _ in range(number_of_digits)))
    return max(a002113(max_number_in_digits))


def a002113(n):
    """
        A002113	Palindromes in base 10.
    """
    yield 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            ij = i * j
            if _is_palindrome(ij):
                yield ij


def _is_palindrome(i):
    """
    A palindromic number reads the same both ways.
    """
    mstr = str(i)
    return mstr == mstr[::-1]


A002113 = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111,
    121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262,
    272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414,
    424, 434, 444, 454, 464, 474, 484, 494, 505, 515
]


def main(speed_test=False):
    print(f'largest_palindrome_product(2) = {largest_palindrome_product(2)}, largest_palindrome_product_bf(2) ={largest_palindrome_product_bf(2)}')  # nopep8
    print(f'largest_palindrome_product(3) = {largest_palindrome_product(3)}, largest_palindrome_product_bf(3) ={largest_palindrome_product_bf(3)}')  # nopep8
    print(f'largest_palindrome_product(5) = {largest_palindrome_product(4)}')
    print(f'list(a002113(1000)) = {list(a002113(99))}')
    if not speed_test: return

    import timeit
    print(
        'largest_palindrome_product_bf(3) ->',
        timeit.timeit(
            'largest_palindrome_product_bf(3)',
            setup="from __main__ import largest_palindrome_product_bf",
            number=100
        )
    )
    print(
        'largest_palindrome_product(3) ->',
        timeit.timeit(
            'largest_palindrome_product(3)',
            setup="from __main__ import largest_palindrome_product",
            number=100
        )
    )


if __name__ == "__main__":
    main(speed_test=True)
