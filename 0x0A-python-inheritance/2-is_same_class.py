#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names is_same_class.
"""


def is_same_class(obj, a_class):
    """function return true if obj is instance of a_class and false If not"""
    if isinstance(obj, a_class):
        return True
    return False
