#!/usr/bin/python3
"""this module for testing squre class"""
import unittest
import os
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

    def test_area(self):
        """ this test funcion for testing area if it was calculte
            right
        """
        sqt = Square(size=4, x=1, y=1, id=9)
        self.assertEqual(sqt.area(), 16)

    def test_update_args(self):
        """
            this test function for checking if update was done as
            was suppose to be using args or tuple
        """
        sqt = Square(2, 1, 2, 23)
        sqt.update(9)
        self.assertEqual(sqt.id, 9)
        sqt.update(9, 2)
        self.assertEqual(sqt.size, 2)
        sqt.update(9, 2, 7)
        self.assertEqual(sqt.x, 7)
        sqt.update(9, 2, 7, 0)
        self.assertEqual(sqt.y, 0)

    def test_update_kwargs(self):
        """
            this test function for checking if update was done as
            was suppose to be using kwargs or dictionay
        """
        sqt = Square(4, 1, 2, 23)
        sqt.update(size=9, x=2, y=7, id=9)
        self.assertEqual(sqt.size, 9)
        self.assertEqual(sqt.x, 2)
        self.assertEqual(sqt.y, 7)
        self.assertEqual(sqt.id, 9)

        sqt2 = Square(7, 10, 20, 3)
        sqt2.update(id=2, size=7, y=10, x=9)
        self.assertEqual(sqt2.size, 7)
        self.assertEqual(sqt2.x, 9)
        self.assertEqual(sqt2.y, 10)
        self.assertEqual(sqt2.id, 2)

        sqt3 = Square(4, 10, 20, 3)
        sqt3.update()
        self.assertEqual(sqt3.size, 4)
        self.assertEqual(sqt3.x, 10)
        self.assertEqual(sqt3.y, 20)
        self.assertEqual(sqt3.id, 3)

    def test_to_dictionary(self):
        """
            this test function for checking if the return of
            to_dictionarywas
        """
        rect = Square(4, 1, 2, 23)
        result = rect.to_dictionary()
        dictionary = {"id": 23, "size": 4, "x": 1, "y": 2}
        self.assertEqual(result, dictionary)

    def test_save_to_file(self):
        """this function for testing save_to_file function
            is working we check the file was created or not
        """
        sq1 = Square(3, 2, 8)
        sq2 = Square(2)
        Square.save_to_file([sq1, sq2])
        file_name = Square.__name__
        result = os.path.exists(f"{file_name}.json")
        self.assertTrue(result)

    def test_create(self):
        """this method for test create methode from base class"""
        sq1 = Square(4, 7, 2)
        dummpy = Square.create(**{"size": 2})
        self.assertTrue((dummpy is not None))

    def test_to_json_string(self):
        """
            this function for testing to_json_string and see the
            return value of the function if it's like what we expected
            we test 3 cses when input is None or empty list or full list
        """
        sqt = Square(7, 2, 8, 1)
        dictionary = sqt.to_dictionary()
        json_string = Square.to_json_string(dictionary)
        expected = """{"id": 1, "size": 7, "x": 2, "y": 8}"""
        self.assertEqual(json_string, expected)

        json_string2 = Square.to_json_string(None)
        expected2 = "[]"
        self.assertEqual(json_string2, expected2)

        json_string3 = Square.to_json_string([])
        expected3 = "[]"
        self.assertEqual(json_string3, expected3)

    def test_from_json_string(self):
        """this function for test from_json_string method
            if its can turn string into json object
        """
        sqt = Square(7, 2, 8)
        result = Square.from_json_string(None)
        self.assertEqual(result, [])
        list_input = [
                    {'id': 89, 'size': 4},
                    {'id': 7, 'size': 7}
                    ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
