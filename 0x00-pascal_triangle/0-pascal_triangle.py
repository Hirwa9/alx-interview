#!/usr/bin/python3


# Defining the function
def pascal_triangle(n):
    # Return / exit function if number given is less than 1
    if n <= 0:
        return []
    triangle = [[1]]
    # Set a range of rows equal to n
    for i in range(1, n):
        row = [1]  # 1 always on first row
        prev_row = triangle[i - 1]
        # Creating current rows numbers
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # 1 always on last row
        triangle.append(row)
    return triangle
