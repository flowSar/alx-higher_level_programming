#!/usr/bin/python3
"""
This is module-level documentation
In this module we define a Square
"""


class Square:
    """ this is the class Square.
    __size is private attribute.
    """
    __size = None

    def __init__(self, size=0):
        """
        Instantiate '_size' attribute with size.
        """
        self.__size = size
        if not isinstance(size, int):
            """
            raise exception TypeError if size isn't int.
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
            raise exception ValueError if size less than 0.
            """
            raise ValueError("size must be >= 0")
