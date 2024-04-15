#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Rectangle is a subclass of BaseGeometry"""
    __width = 0
    __height = 0

    def __init__(self, width, height):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = width
        if type(height)is not int:
            raise TypeError("height must be an integer")
        self.__height = height
