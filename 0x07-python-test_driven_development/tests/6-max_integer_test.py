#!/usr/bin/python3
"""
Unittests for various max.integer([..])
"""


import unittest
from max_integer import max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_max_integer(self):
        """
        Test the max_integer function with different inputs.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

        self.assertEqual(max_integer([-5, 10, -3, 8, -1]), 10)

        self.assertEqual(max_integer([1.5, 2.7, 3.1, 4.9, 5.2]), 5.2)

        self.assertEqual(max_integer([42]), 42)

        self.assertIsNone(max_integer([]))

    def test_max_integer_raises_type_error(self):
        """
        Test that max_integer raises TypeError for invalid inputs.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4, 5])

        with self.assertRaises(TypeError):
            max_integer("not a list")

    def test_max_integer_raises_value_error(self):
        """
        Test that max_integer raises ValueError for an empty list.
        """
        with self.assertRaises(ValueError):
            max_integer([])


if __name__ == '__main__':
    unittest.main()
