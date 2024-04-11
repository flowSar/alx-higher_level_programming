#!/usr/bin/python3
"""
This is module-level documentation
In this module has one empty class names Rectangle.
"""


class Rectangle:
    """
    This is a class named Rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter function for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        this function set a new width value.
        args:
            new value.
        """
        if not isinstance(value, int):
            """
            raise exception TypeError if value isn't int.
            """
            raise TypeError("width must be an integer")
        elif value < 0:
            """
            raise exception ValueError if value less than 0.
            """
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter function for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        this function set a new height value.
        args:
            new value.
        """
        if not isinstance(value, int):
            """
            raise exception TypeError if value isn't int.
            """
            raise TypeError("height must be an integer")
        elif value < 0:
            """
            raise exception ValueError if value less than 0.
            """
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculte the erea of the Rectangle.
        Returns:
            A numbre representing the earea of a Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of a Rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        shape = """"""
        if self.width == 0 or self.height == 0:
            return shape
        for i in range(self.height):
            for j in range(self.width):
                shape += "#"
            if i < self.height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        """function returns a string representation of an object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")