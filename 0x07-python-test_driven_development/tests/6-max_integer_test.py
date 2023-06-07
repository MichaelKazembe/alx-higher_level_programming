#!/usr/bin/python3
"""Unittests for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_max_integer(self):
        # Test with a list containing positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with a list containing negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

        # Test with a list containing both positive and negative integers
        self.assertEqual(max_integer([-5, 0, 5]), 5)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing a single element
        self.assertEqual(max_integer([42]), 42)

        # Test with a list containing duplicate maximum values
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test with a list containing floating-point numbers
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.5]), 3.2)


if __name__ == '__main__':
    unittest.main()
