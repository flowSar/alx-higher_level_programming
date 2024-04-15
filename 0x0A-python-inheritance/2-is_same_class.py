#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names is_same_class.
"""


def is_same_class(obj, a_class):
    """
    function check if obj is instance of a_class and return True it it's
    and False if not

    Args:
        obj: object 1
        a_class: object 2

    """
    if isinstance(obj, a_class):
        return True
    return False
