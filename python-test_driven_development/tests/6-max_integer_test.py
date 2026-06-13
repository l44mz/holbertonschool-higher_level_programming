#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_empty_list(self):
        """Test that an empty list returns None"""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test that calling with no argument returns None"""
        self.assertEqual(max_integer(), None)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_start(self):
        """Test when the max value is at the start of the list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_at_end(self):
        """Test when the max value is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test when the max value is in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_numbers(self):
        """Test a list with all negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -3, 2]), 5)

    def test_duplicate_max(self):
        """Test a list with duplicate maximum values"""
        self.assertEqual(max_integer([4, 4, 1, 2]), 4)

    def test_all_same_values(self):
        """Test a list where all elements are equal"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)


if __name__ == '__main__':
    unittest.main()
