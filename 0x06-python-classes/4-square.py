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
        self.size = size
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

    def area(self):
        """
        calculte the erea of the Square.
        Returns:
            A numbre eprestenting the earea of a Square.
        """
        return self.__size * self.__size

    def size(self, value):
        """
        this function set a new size value.
        args:
            new value.
        """
        if not isinstance(value, int):
            """
            raise exception TypeError if value isn't int.
            """
            raise TypeError("size must be an integer")
        elif value < 0:
            """
            raise exception ValueError if value less than 0.
            """
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
