#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    
    __size = 0
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area of the Rectangle"""
        return self.__size * self.__size
