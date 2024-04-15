#!/usr/bin/python3
"""
    this module provides a function that return a list of object attributes
    and methodes
"""


def lookup(obj):
    """this function return list of attributes and methods of an object
        Args:
            obj: object
        return:
            list of object content
    """
    return dir(obj)
