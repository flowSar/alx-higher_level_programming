#!/usr/bin/python3
"""
This is module-level documentation
In this module has one empty class names Rectangle.
"""


class Rectangle:
    """
    This is a class named Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        this function set a new width value.
        args:
            new value.
        """
        if not isinstance(value, int):
            """
            raise exception TypeError if value isn't int.
            """
            raise TypeError("width must be an integer")
        elif value < 0:
            """
            raise exception ValueError if value less than 0.
            """
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter function for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        this function set a new height value.
        args:
            new value.
        """
        if not isinstance(value, int):
            """
            raise exception TypeError if value isn't int.
            """
            raise TypeError("height must be an integer")
        elif value < 0:
            """
            raise exception ValueError if value less than 0.
            """
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
