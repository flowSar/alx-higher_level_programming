#!/usr/bin/python3

import unittest

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1,4,5,6,7,0]), 7)
        self.assertEqual(max_integer([100, 4, 300, 4, 0, 2]), 300)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_enmpty_lest(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

if __name__ == '__main__':
    unittest.main()
