#!/usr/bin/python3
"""
    this module have a function for checking if the object
    is an inheritance of a class
"""


def inherits_from(obj, a_class):
    """
    function for checking if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class and
    return True it it's and False if not
    we're not checking if obj is instance of a_class that was I put
    if statment to check the exact instance
    this function only check the inheritance not instance

    Args:
        obj: object 1
        a_class: object 2

    Return: True if obj instance of a_class and False if not
    """
    if type(obj) != a_class:
        if isinstance(obj, a_class):
            return True
    return False
