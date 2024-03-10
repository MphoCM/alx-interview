#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle list
    triangle = []

    # Iterate over each row
    for i in range(n):
        # Initialize a new row with zeros
        new_row = [0] * (i + 1)

        # Set the first and last element of the row to 1
        new_row[0] = 1
        new_row[-1] = 1

        # Calculate values for non-edge elements
        for j in range(1, i):
            # Get the values from the previous row
            a = triangle[i - 1][j]
            b = triangle[i - 1][j - 1]
            # Calculate the new value for the current position
            new_row[j] = a + b

        # Append the new row to the triangle
        triangle.append(new_row)

    return triangle
