import unittest  # Import the unittest module

# Import the function to test from the pascal_triangle module
from pascal_triangle import pascal_triangle

class TestPascalTriangle(unittest.TestCase):  # Define a test case class
    # Test case for n = 5
    def test_n_5(self):
        # Define the expected output for n = 5
        expected_output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        # Assert that the output of pascal_triangle(5) matches the expected output
        self.assertEqual(pascal_triangle(5), expected_output)

    # Test case for n = 1
    def test_n_1(self):
        # Define the expected output for n = 1
        expected_output = [[1]]
        # Assert that the output of pascal_triangle(1) matches the expected output
        self.assertEqual(pascal_triangle(1), expected_output)

    # Test case for n = 0 (should raise a ValueError)
    def test_n_0(self):
        # Assert that calling pascal_triangle(0) raises a ValueError
        with self.assertRaises(ValueError):
            pascal_triangle(0)

    # Test case for n = 10
    def test_n_10(self):
        # Define the expected output for n = 10
        expected_output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]
        # Assert that the output of pascal_triangle(10) matches the expected output
        self.assertEqual(pascal_triangle(10), expected_output)

    # Test case for n = 100 (only checks the number of rows)
    def test_n_100(self):
        # Assert that the number of rows in the output of pascal_triangle(100) is 100
        self.assertEqual(len(pascal_triangle(100)), 100)

if __name__ == '__main__':
    unittest.main()
