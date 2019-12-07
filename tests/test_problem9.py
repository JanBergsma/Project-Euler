from src.problem9 import find_pythagorean_triple


def test_product_of_pytagorian_triplet_which_sum_of_a_b_c_is_1000_should_be_31875000():  # nopep8
    a, b, c = find_pythagorean_triple(1000)
    assert a + b + c == 1000
    assert a**2 + b**2 == c**2
    assert a * b * c == 31875000
