#!/usr/bin/python3
"""
    this module is for testtunite of base class and all
    it methodes
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    """
        this class for testing all base methodes one by one
    """
    def test__init__(self):
        """ initiliaze object"""
        pass

    def test_bade_id(self):
        """
            this function for testing object id
            incremented
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base4 = Base()
        self.assertEqual(base4.id, 4)

    def test_init_twi(self):
        """
            this function for testing id asignment
        """
        base5 = Base()
        base5.id = 10
        self.assertEqual(base5.id, 10)

    def test_to_json_string(self):
        """
            this function for testing to_json_string and see the
            return value of the function if it's like what we expected
            we test 3 cses when input is None or empty list or full list
        """
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
        """this function for testing save_to_file function
            is working we check the file was created or not
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        file_name = Rectangle.__name__
        result = os.path.exists(f"{file_name}.json")
        self.assertTrue(result)

    def test_from_json_string(self):
        """this function for test from_json_string method
            if its can turn string into json object
        """
        r1 = Rectangle(10, 7, 2, 8)
        result = r1.from_json_string(None)
        self.assertEqual(result, [])
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = r1.to_json_string(list_input)
        list_output = r1.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
