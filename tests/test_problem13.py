from src.problem13 import large_sum, one_hundred_50_digit_numbers


def test_large_sum():
    expect = 5537376230390876637302048746832985971773659831892672
    result = large_sum(one_hundred_50_digit_numbers)
    assert result == expect
