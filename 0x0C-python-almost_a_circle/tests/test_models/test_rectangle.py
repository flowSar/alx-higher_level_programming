#!/usr/bin/python3

import unittest
import sys
from models.rectangle import Rectangle
from models.rectangle import check_for_exception


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(1, 4)
        self.assertEqual(rect.id, 1)
        rect1 = Rectangle(1, 4)
        self.assertEqual(rect1.id, 2)
        rect = Rectangle(4, 2, 1, 2, 5)
        self.assertEqual(rect.id, 5)

    def test_init_exception(self):
        self.assertRaises(TypeError, Rectangle, "3", 4, 5, 1)
        self.assertRaises(TypeError, Rectangle, 3, "4", 5, 1)
        self.assertRaises(ValueError, Rectangle, -1, 4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 0, 4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 1, -4, 5, 1)
        self.assertRaises(ValueError, Rectangle, 10, 0, 5, 1)

    def test_check_for_exception(self):
        self.assertRaises(TypeError, check_for_exception, "l", "height")
        self.assertRaises(ValueError, check_for_exception, 0, "height")
        self.assertRaises(ValueError, check_for_exception, -1, "height")

    def test_set_with_raise_exception(self):
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
        with self.assertRaises(TypeError):
            rect1 = Rectangle(width=4, height=3, x=1, y=1, id=7)
            rect1.x = "9"
        with self.assertRaises(ValueError):
            rect2 = Rectangle(width=4, height=4, x=0, y=0, id=8)
            rect2.x = -5

    def test_set_y_raise_Exception(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(width=4, height=3, x=1, y=1, id=9)
            rect1.y = "1"
        with self.assertRaises(ValueError):
            rect2 = Rectangle(width=4, height=4, x=0, y=0, id=92)
            rect2.y = -100

    def test_set_width(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        rect.width = 10
        self.assertEqual(rect.width, 10)

    def test_set_height(self):
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.height = 5
        self.assertEqual(rect.height, 5)

    def test_set_x(self):
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.x = 0
        self.assertEqual(rect.x, 0)

    def test_set_y(self):
        rect = Rectangle(width=4, height=1, x=1, y=1, id=9)
        rect.y = 3
        rect.id = 10
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.y, 3)

    def test_get_width(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.width, 4)

    def test_get_height(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.height, 3)

    def test_get_x(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.x, 1)

    def test_get_y(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.y, 1)

    def test_area(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        self.assertEqual(rect.area(), 12)

    def test_str(self):
        rect = Rectangle(width=4, height=3, x=1, y=1, id=9)
        msg = "[Rectangle] (9) 1/1 - 4/3"
        result = rect.__str__()
        self.assertEqual(result, msg)

    def test_display(self):
        pass

    def test_update_args(self):
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
