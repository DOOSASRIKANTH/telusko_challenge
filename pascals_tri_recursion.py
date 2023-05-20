def pascals_triangle_recursive(n):
    if n == 1:
        return [[1]]
    else:
        previous_triangle = pascals_triangle_recursive(n - 1)
        previous_row = previous_triangle[-1]

        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)

        previous_triangle.append(current_row)
        return previous_triangle


def print_pascals_triangle_pyramid(n):
    triangle = pascals_triangle_recursive(n)
    max_value = triangle[-1][-1]
    max_width = len(str(max_value))

    for row in triangle:
        num_spaces = max_width // 2 * (n - len(row))
        row_values = [str(val).center(max_width) for val in row]
        row_str = ' ' * num_spaces + ' '.join(row_values)
        print(row_str)


n = 5
print_pascals_triangle_pyramid(n)
