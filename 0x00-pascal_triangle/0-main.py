#!/usr/bin/python3

# This script generates and prints Pascal's triangle using the pascal_triangle function.

# Import the pascal_triangle function from the 0-pascal_triangle module
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

# Define a function to print the triangle
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:  # Iterate over each row in the triangle
        print("[{}]".format(",".join([str(x) for x in row])))  # Print each row as a comma-separated list

# Execute the code only if the script is run directly
if __name__ == "__main__":
    # Call the pascal_triangle function with n = 5 and print the resulting triangle
    print_triangle(pascal_triangle(5))
