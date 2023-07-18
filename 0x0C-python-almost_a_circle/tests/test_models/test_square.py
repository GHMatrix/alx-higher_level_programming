#!/usr/bin/python3
"""
Unittest for square.py
"""


import unittest
from square import Square


class TestSquare(unittest.TestCase):

    def test_init_valid_arguments(self):
        # Test valid arguments
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_init_invalid_size(self):
        # Test invalid size
        with self.assertRaises(ValueError):
            Square(0)

    def test_init_invalid_x(self):
        # Test invalid x
        with self.assertRaises(ValueError):
            Square(5, x=-2)

    def test_init_invalid_y(self):
        # Test invalid y
        with self.assertRaises(ValueError):
            Square(5, y=-3)

    def test_setter_size(self):
        square = Square(5)
        # Test valid size
        square.size = 7
        self.assertEqual(square.size, 7)

        # Test invalid size
        with self.assertRaises(ValueError):
            square.size = -5

    def test_setter_width_height(self):
        square = Square(5)
        # Test valid width and height
        square.width = 8
        square.height = 8
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.size, 8)

        # Test invalid width and height
        with self.assertRaises(ValueError):
            square.width = -5
        with self.assertRaises(ValueError):
            square.height = -5

    def test_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_to_string(self):
        square = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5\n"
        self.assertEqual(str(square), expected_output)

    def test_update_args(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_kwargs(self):
        square = Square(5, 2, 3, 1)
        square.update(size=8, x=4, y=5, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_update_invalid_attribute(self):
        square = Square(5)
        with self.assertRaises(TypeError):
            square.update(invalid_attribute=8)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
