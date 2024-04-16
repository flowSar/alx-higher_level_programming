#!/usr/bin/python3
"""
In this module has one function names is_same_class.
"""


def is_same_class(obj, a_class):
    """
    function check if obj is instance of a_class and return True it it's
    and False if not

    Args:
        obj: object 1
        a_class: object 2

    Return: True if obj instance of a_class and False if not

    """
    return isinstance(obj, a_class)
