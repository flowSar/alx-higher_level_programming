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
    __width = 0
    __height = 0

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
