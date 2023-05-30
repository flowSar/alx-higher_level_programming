#!/usr/bin/python3
"""
This is module-level documentation
In this module we define a Square
"""


class Square:
    """
    This is a'Square'
    Has a private attribute 'size'
    """

    __size = None

    def __init__(self, size):
        """
        Instantiate 'size' attribute
        """

        self.__size = size