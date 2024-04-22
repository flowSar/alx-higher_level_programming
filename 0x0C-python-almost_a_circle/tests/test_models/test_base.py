#!/usr/bin/python3

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base4 = Base()
        self.assertEqual(base4.id, 4)

    def test_init_twi(self):
        base5 = Base()
        base5.id = 10
        self.assertEqual(base5.id, 10)

    def test_to_json_string(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_string = rect.to_json_string(dictionary)
        expected = """{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}"""
        self.assertEqual(json_string, expected)

        json_string2 = rect.to_json_string(None)
        expected2 = "[]"
        self.assertEqual(json_string2, expected2)

        json_string3 = rect.to_json_string([])
        expected3 = "[]"
        self.assertEqual(json_string3, expected3)

    def test_save_to_file(self):
        pass

    def test_from_json_string(self):
        pass