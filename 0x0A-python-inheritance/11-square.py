#!/usr/bin/python3
"""
    this module continue a Rectangle class  with constractor method
    and he's a subclass on Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
        Rectangle is a subclass of Rectangle
        Attribute:
            __size: size of square

    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
            this function is implementation of area function from superclass
            Return:
                return the area of Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
            this function is a magic function that print instance of this class
        """
        return "[Square] "+str(self.__size)+"/"+str(self.__size)
