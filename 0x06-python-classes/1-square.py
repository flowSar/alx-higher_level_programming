#!/usr/bin/python3
"""
This is module-level documentation
In this module we define a Square
"""


class Square:
    """
    This is a'Square' with private variable '_size'
    """
    __size = None

    def __init__(self, size):
        """
        Instantiate '_size' attribute with size
        """
        self.__size = size
