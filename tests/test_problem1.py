from src.problem1 import (
    sum_of_multiples_of_3_or_5,
    sum_of_multiples_of_3_or_5_brute_force
)


def test_sum_of_multiples_of_3_or_5_smaller_then_10_should_be_23():
    assert sum_of_multiples_of_3_or_5(10) == 23


def test_sum_of_multiples_of_3_or_5_smaller_then_1000_should_be_equal_to_sum_of_all_3s_and_all_5s_minus_count_of_15s():  # nopep8
    """
    see:
    https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000
    """

    counts = sum(3 * k for k in range(1, 334))  # count all threes
    counts += sum(5 * k for k in range(1, 200))  # count all fives
    counts -= sum(15 * k for k in range(1, 67))  # correct over counted 15 (3x5)  # nopep8
    assert sum_of_multiples_of_3_or_5(1000) == counts
    assert sum_of_multiples_of_3_or_5(1000) == 233168


def test_against_brute_force():
    assert all(
        sum_of_multiples_of_3_or_5_brute_force(n) == sum_of_multiples_of_3_or_5(n)  # nopep8
        for n in range(1_000)
    )
