#!/usr/bin/python3

class BaseGeometry:
    """class named BaseGeometry """
    def area(self):
        """empty function raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            function raise exception in two caces when value is less than 0
            and when value is not integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
