#!/usr/bin/python3
"""
    this module continue a Rectangle class  with constractor method
    and he's a subclass on BaseGeometry class
"""

# Importing the BaseGeometry class from the 7-base_geometry module
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
