#!/usr/bin/python3
"""
Unittest for rectangle.py
"""


import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init_valid_arguments(self):
        # Test valid arguments
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_init_invalid_width(self):
        # Test invalid width
        with self.assertRaises(ValueError):
            Rectangle(0, 10)

    def test_init_invalid_height(self):
        # Test invalid height
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_init_invalid_x(self):
        # Test invalid x
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2)

    def test_init_invalid_y(self):
        # Test invalid y
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_setter_width(self):
        rectangle = Rectangle(5, 10)
        # Test valid width
        rectangle.width = 7
        self.assertEqual(rectangle.width, 7)

        # Test invalid width
        with self.assertRaises(ValueError):
            rectangle.width = -5

    def test_setter_height(self):
        rectangle = Rectangle(5, 10)
        # Test valid height
        rectangle.height = 12
        self.assertEqual(rectangle.height, 12)

        # Test invalid height
        with self.assertRaises(ValueError):
            rectangle.height = -10

    def test_setter_x(self):
        rectangle = Rectangle(5, 10)
        # Test valid x
        rectangle.x = 3
        self.assertEqual(rectangle.x, 3)

        # Test invalid x
        with self.assertRaises(ValueError):
            rectangle.x = -2

    def test_setter_y(self):
        rectangle = Rectangle(5, 10)
        # Test valid y
        rectangle.y = 4
        self.assertEqual(rectangle.y, 4)

        # Test invalid y
        with self.assertRaises(ValueError):
            rectangle.y = -3

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(5, 3, 2, 1)
        expected_output = "\n\n  #####\n  #####\n  #####\n"
        with unittest.mock.patch(
                'sys.stdout', new=unittest.mock.StringIO()) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_to_string(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10\n"
        self.assertEqual(str(rectangle), expected_output)

    def test_update_args(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(2, 8, 12, 4, 5)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_update_kwargs(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(width=8, height=12, x=4, y=5, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_update_invalid_attribute(self):
        rectangle = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            rectangle.update(invalid_attribute=8)

    def test_to_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 3
        }
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
