from src.problem2 import a014445, a014445_iter

A014445 = [
    0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578,
    14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074,
    86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288,
    117669030460994
]


def test_a014445_even_fibonacci_numbers():
    assert all(
        e == r
        for e, r in
        zip(A014445, (a014445(n) for n in range(len(A014445))))
    )


def test_a014445_iter_even_fibonacci_numbers():
    assert all(
        e == r
        for e, r in
        zip(A014445, a014445_iter(A014445[-1]))
    )


def test_sum_of_a014445_iter_for_smaller_then_4_000_000_should_be_4613732():
    expected = sum(n for n in A014445 if n <= 4_000_000)
    result = sum(n for n in a014445_iter())
    assert expected == result
    assert 4613732 == result
