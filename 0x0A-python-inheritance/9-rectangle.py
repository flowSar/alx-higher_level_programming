#!/usr/bin/python3
"""
    this module continue a Rectangle class  with constractor method
    and he's a subclass on BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
        Rectangle is a subclass of BaseGeometry
        Attribute:
            __width: width of Rectange
            __height: height of Rectangle

    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
            this function is implementation of area function from superclass
            Return:
                return the area of rctangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            this function is a magic function that print instance of this class
        """
        return "[Rectangle] "+str(self.__width)+"/"+str(self.__height)
