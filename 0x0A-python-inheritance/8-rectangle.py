#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    this module continue a Rectangle class  with constractor method
    and he's a subclass on BaseGeometry class
"""


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
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
