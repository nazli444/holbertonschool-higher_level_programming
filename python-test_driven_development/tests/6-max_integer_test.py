#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list where max is at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_at_end(self):
        """Test list where max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_negatives(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_int_float(self):
        """Test list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0]), 3)

    def test_duplicate_max(self):
        """Test list with multiple max values"""
        self.assertEqual(max_integer([3, 1, 3, 2]), 3)

    def test_strings_error(self):
        """Test list with strings raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

if __name__ == '__main__':
    unittest.main()
