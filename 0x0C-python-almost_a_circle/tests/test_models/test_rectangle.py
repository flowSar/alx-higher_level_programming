#!/usr/bin/python3
"""
    this module for testing rectangle module
"""
import unittest
import os
from models.rectangle import Rectangle
from models.rectangle import check_for_exception


class TestRectangle(unittest.TestCase):

    """this function for testing asignment of id of rectangle instance
        id ws effected by base module because id is a class attribute
        each time we create instance from the classs we increment it.
    """
    def test_init(self):
        rect = Rectangle(1, 4)
        self.assertEqual(rect.id, 14)
        rect1 = Rectangle(1, 4)
        self.assertEqual(rect1.id, 15)
        rect = Rectangle(4, 2, 1, 2, 5)
        self.assertEqual(rect.id, 5)

    def test_init_exception(self):
        """
            this function for test the raised exception in __init__
            method
        """
        self.assertRaises(TypeError, Rectangle, "3", 4, 5, 1)
        self.assertRaises(TypeError, Rectangle, 3, "4", 5, 1)
        self.assertRaises(ValueError, Rectangle, -1, 4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 0, 4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 1, -4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 10, 0, 5, 1)

    def test_check_for_exception(self):
        """
            this function for test the raised exception in
            check_for_exception method
        """
        self.assertRaises(TypeError, check_for_exception, "l", "height")
        self.assertRaises(ValueError, check_for_exception, 0, "height")
        self.assertRaises(ValueError, check_for_exception, -1, "height")

    def test_set_with_raise_exception(self):
        """
            this function test raised exception during asignment of
            rectangle attribute width
        """
        with self.assertRaises(TypeError):
            rect = Rectangle(width=3, height=3, x=1, y=6, id=5)
            rect.width = "3"
        with self.assertRaises(ValueError):
            rect1 = Rectangle(4, 3, 2, 1)
            rect1.width = -1
        with self.assertRaises(ValueError):
            rect2 = Rectangle(4, 3, 2, 1)
            rect2.width = 0

    def test_set_height_raise_exception(self):
        """
            this function test raised exception during asignment of
            rectangle attribute height
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle(width=4, height=3, x=2, y=1, id=4)
            rect1.height = "k"
        with self.assertRaises(ValueError):
            rect2 = Rectangle(width=4, height=3, x=2, y=1, id=5)
            rect2.height = -5
        with self.assertRaises(ValueError):
            rect3 = Rectangle(width=4, height=3, x=2, y=1, id=6)
            rect3.height = 0

    def test_set_x_raise_exception(self):
        """
            this function test raised exception during asignment of
            rectangle attribute x
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle(width=4, height=3, x=1, y=1, id=7)
            rect1.x = "9"
        with self.assertRaises(ValueError):
            rect2 = Rectangle(width=4, height=4, x=0, y=0, id=8)
            rect2.x = -5

    def test_set_y_raise_Exception(self):
        """
            this function test raised exception during asignment of
            rectangle attribute y
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle(width=4, height=3, x=1, y=1, id=9)
            rect1.y = "1"
        with self.assertRaises(ValueError):
            rect2 = Rectangle(width=4, height=4, x=0, y=0, id=92)
            rect2.y = -100

    def test_set_width(self):
        """ this test funcion for testing asignment of width attribute"""
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        rect.width = 10
        self.assertEqual(rect.width, 10)

    def test_set_height(self):
        """ this test funcion for testing asignment of height attribute"""
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_set_x(self):
        """ this test funcion for testing asignment of x attribute"""
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.x = 0
        self.assertEqual(rect.x, 0)

    def test_set_y(self):
        """ this test funcion for testing asignment of y attribute"""
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.y = 3
        rect.id = 10
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.y, 3)

    def test_get_width(self):
        """ this test funcion for testing width getter"""
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.width, 4)

    def test_get_height(self):
        """ this test funcion for testing height getter"""
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.height, 3)

    def test_get_x(self):
        """ this test funcion for testing x getter"""
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.x, 1)

    def test_get_y(self):
        """ this test funcion for testing y getter"""
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.y, 1)

    def test_area(self):
        """ this test funcion for testing area if it was calculte
            right
        """
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.area(), 12)

    def test_str(self):
        """this test function for test __str__ function is like
            what it was suppose to print
        """
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        msg = "[Rectangle] (9) 1/1 - 4/3"
        result = rect.__str__()
        self.assertEqual(result, msg)

    def test_update_args(self):
        """
            this test function for checking if update was done as
            was suppose to be using args or tuple
        """
        rect = Rectangle(4, 2, 1, 2, 23)
        rect.update(9)
        self.assertEqual(rect.id, 9)
        rect.update(9, 2)
        self.assertEqual(rect.width, 2)
        rect.update(9, 2, 7)
        self.assertEqual(rect.height, 7)
        rect.update(9, 2, 7, 0)
        self.assertEqual(rect.x, 0)
        rect.update(9, 2, 7, 0, 0)
        self.assertEqual(rect.y, 0)

    def test_update_kwargs(self):
        """
            this test function for checking if update was done as
            was suppose to be using kwargs or dictionay
        """
        rect = Rectangle(4, 2, 1, 2, 23)
        rect.update(width=9, x=2, y=7, height=10, id=9)
        self.assertEqual(rect.width, 9)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 9)

        rect2 = Rectangle(41, 7, 10, 20, 3)
        rect2.update(height=9, id=2, width=7, y=10, x=9)
        self.assertEqual(rect2.width, 7)
        self.assertEqual(rect2.height, 9)
        self.assertEqual(rect2.x, 9)
        self.assertEqual(rect2.y, 10)
        self.assertEqual(rect2.id, 2)

        rect3 = Rectangle(4, 7, 10, 20, 3)
        rect3.update()
        self.assertEqual(rect3.width, 4)
        self.assertEqual(rect3.height, 7)
        self.assertEqual(rect3.x, 10)
        self.assertEqual(rect3.y, 20)
        self.assertEqual(rect3.id, 3)

    def test_to_dictionary(self):
        """
            this test function for checking if the return of
            to_dictionarywas
        """
        rect = Rectangle(4, 2, 1, 2, 23)
        result = rect.to_dictionary()
        dictionary = {"id": 23, "width": 4, "height": 2, "x": 1, "y": 2}
        self.assertEqual(result, dictionary)

    def test_create(self):
        """this method for test create methode from base class"""
        r1 = Rectangle(10, 7, 2, 8)
        dummpy = Rectangle.create(**{"width": 2, "height": 2})
        self.assertTrue((dummpy is not None))

    def test_to_json_string(self):
        """
            this function for testing to_json_string and see the
            return value of the function if it's like what we expected
            we test 3 cses when input is None or empty list or full list
        """
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_string = Rectangle.to_json_string(dictionary)
        expected = """{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}"""
        self.assertEqual(json_string, expected)

        json_string2 = Rectangle.to_json_string(None)
        expected2 = "[]"
        self.assertEqual(json_string2, expected2)

        json_string3 = Rectangle.to_json_string([])
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
        result = Rectangle.from_json_string(None)
        self.assertEqual(result, [])
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
    
        
    def test_load_from_file(self):
        """this function test loding from file if it's much 
            object attribute
        """
        sq1 = Rectangle(4, 2, 1, 2)
        sq2 = Rectangle(2, 4, 0)
        list_rectangles_input = [sq1, sq2]
        Rectangle.save_to_file(list_rectangles_input)
        list_Rectangle_output = Rectangle.load_from_file()
        dictionary1 = list_Rectangle_output[0].to_dictionary()
        dictionary2 = list_Rectangle_output[1].to_dictionary()
        self.assertEqual(dictionary1, sq1.to_dictionary())
        self.assertEqual(dictionary2, sq2.to_dictionary())

