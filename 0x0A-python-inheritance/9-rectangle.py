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

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] "+str(self.__width)+"/"+str(self.__height)
