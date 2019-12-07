def pascal_triangle(n):
    triangle = [[1]]
    for i in range(n):
        triangle.append(
            [1] +
            [
                triangle[-1][i] + triangle[-1][i + 1]
                for i in range(len(triangle[-1]) - 1)
            ] +
            [1]
        )
    return triangle


def pascal_triangle_row(n):
    t = [1]
    for i in range(n):
        t = [1] + [t[i] + t[i + 1] for i in range(len(t) - 1)] + [1]
    return t


# pt = create_triangle_simple(1000)
# print('\n'.join(' '.join(f'{i}' for i in row) for row in pt))

def row_to_string(n):
    return ' + '.join(
        f'{i}*x^{n - p}'
        for p, i in enumerate(pascal_triangle_row(n))
    )

for i in range(14):
    print(row_to_string(i))
