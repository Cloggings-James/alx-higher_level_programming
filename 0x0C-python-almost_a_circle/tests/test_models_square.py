#!/usr/bin/python3
"""
Unit tests for the Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_init(self):
        """
        Test the initialization of a Square instance.
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_size_property(self):
        """
        Test the size property of the Square class.
        """
        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_str(self):
        """
        Test the string representation of a Square instance.
        """
        s = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_str)

    def test_update(self):
        """
        Test the update method of the Square class.
        """
        s = Square(5, 2, 3, 1)
        s.update(10, 7, 8, 9)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

        s.update(size=15, y=5, x=3)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """
        s = Square(5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()

