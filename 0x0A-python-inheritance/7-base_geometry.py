#!/usr/bin/python3
"""
    this module contains a class named BaseGeometry
    and this BaseGeometry have two method one for
    area and the second for integer validation

"""


class BaseGeometry:
    """class named BaseGeometry """
    def area(self):
        """area method have only one function is raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            function raise exception in two caces when value is less than 0
            and when value is not integer.

            Args:
                name: is name
                value: is number
            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))