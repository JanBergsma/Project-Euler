from src.problem4 import (
    largest_palindrome_product,
    largest_palindrome_product_bf,
    a002113,
    A002113
)


def test_a002113():
    assert all(e == r for e, r in zip(A002113, a002113(1000)))


def test_largest_palindrome_product_size_2():
    assert largest_palindrome_product(2) == 9009


def test_largest_palindrome_product_size_3():
    assert largest_palindrome_product(3) == 906609


def test_largest_palindrome_product_bf_size_2():
    assert largest_palindrome_product_bf(2) == 9009


def test_largest_palindrome_product_bf_size_3():
    assert largest_palindrome_product_bf(3) == 906609
