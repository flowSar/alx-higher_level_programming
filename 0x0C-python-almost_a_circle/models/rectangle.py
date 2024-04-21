#!/usr/bin/python3
from base import Base
"""
    rectangle module
"""


def check_for_exception(value, name):
    """
    this function check if the value is suitable
    for the operation that we are doing in this class
    we check if value is int or it is >= 0 in some cases
    and we raise error is this value doesn't correspond with
    rectangle condition

    Attributes:
        value: this value sould be int and > 0 in same case.
        name: name of the variable that may raise exception.
                width, height, x, y.
    Return:
        None
    """

    if name == "width" or name == "height":
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be > 0")
    else:
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")


class Rectangle(Base):
    """
        __init__ is object constructor has 4 input argumente
        width , height, x, and y she takes them and asing them to
        instance attributes sequenstly __width , __height, __x, __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        check_for_exception(width, "width")
        check_for_exception(height, "height")
        check_for_exception(x, "x")
        check_for_exception(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        check_for_exception(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        check_for_exception(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        check_for_exception(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        check_for_exception(y, "y")
        self.__y = y

    def area(self):
        """rear method return area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """display function draw of represent a rectange with '#' """
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for w in range(self.__width + self.__x):
                if w < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """str is a mgic method for printing object"""
        piece1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        piece2 = f" - {self.__width}/{self.__height}"
        return piece1 + piece2

    def update(self, *args, **kwargs):
        """
            this function asigning argument to each attribute
            of object instance .
            Attribute:
                *args: this can pass multiple input from id
                width, height, x, y
                **kwrgs: this can pass multiple input from id
                width, height, x, y but by key they aren't organized
        """
        args_length = len(args)

        if args_length == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    check_for_exception(value, key)
                    self.__width = value
                elif key == "height":
                    check_for_exception(value, key)
                    self.__height = value
                elif key == "x":
                    check_for_exception(value, key)
                    self.__x = value
                elif key == "y":
                    check_for_exception(value, key)
                    self.__y = value
        else:
            if args_length >= 1:
                self.id = args[0]
            if args_length >= 2:
                check_for_exception(args[1], "width")
                self.__width = args[1]
            if args_length >= 3:
                check_for_exception(args[2], "height")
                self.__height = args[2]
            if args_length >= 4:
                check_for_exception(args[3], "x")
                self.__x = args[3]
            if args_length >= 5:
                check_for_exception(args[4], "y")
                self.__y = args[4]

    def to_dictionary(self):
        rect_dictionary = {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x,
            "y": self.y
        }
        return rect_dictionary
