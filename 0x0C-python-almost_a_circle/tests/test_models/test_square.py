#!/usr/bin/python3
"""this module for testing squre class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """class for square testing """
    def test_init(self):
        """function for testing __init__ met"""
        pass

    def test_str(self):
        """this test function for test __str__ function is like
            what it was suppose to print
        """
        sq = Square(size=4, x=1, y=1, id=9)
        msg = "[Square] (9) 1/1 - 4"
        result = sq.__str__()
        self.assertEqual(result, msg)

    def test_set_size(self):
        sq = Square(size=4, x=1, y=1, id=9)
        sq.size = 10
        self.assertEqual(sq.size, 10)

    def test_get_size(self):
        sq = Square(size=4, x=1, y=1, id=9)
        self.assertEqual(sq.size, 4)
