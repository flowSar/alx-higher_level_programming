#!/usr/bin/python3
"""
    this module have a class named as BaseGeometry and within this
    there's an ares function that raise exception
"""


class BaseGeometry:
    """class named BaseGeometry """
    def area(self):
        """empty function raise Exception"""
        raise Exception("area() is not implemented")
