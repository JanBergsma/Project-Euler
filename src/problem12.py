from math import inf, sqrt


def triangle_number(n):
    triangle_number = 0
    add_factor = 1
    while add_factor <= n:
        yield triangle_number
        triangle_number += add_factor
        add_factor += 1


def divisors(x):
    sqrt_x = sqrt(x)
    return (
        sum(2 for i in range(1, int(sqrt_x) + 1) if x % i == 0) -
        1 if sqrt_x**2 == x else 0
    )


def find_first_triangle_number_with_divisors(n):

    for tn in triangle_number(inf):
        if divisors(tn) >= n:
            return tn


A000217 = [
    0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120,
    136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378,
    406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780,
    820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275,
    1326, 1378, 1431
]


def main():
    print(
        f'find_first_triangle_number_with_divisors(500)={find_first_triangle_number_with_divisors(500)}')  # nopep8
    import timeit
    print(
        'find_first_triangle_number_with_divisors(500) ->',
        timeit.timeit(
            'find_first_triangle_number_with_divisors(500)',
            setup="from __main__ import find_first_triangle_number_with_divisors",  # nopep8
            number=10
        )
    )


if __name__ == "__main__":
    main()
