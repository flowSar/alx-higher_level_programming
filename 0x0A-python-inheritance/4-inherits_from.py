#!/usr/bin/python3
"""this module have a function for checking if the object
    is an inheritence of a class """


def inherits_from(obj, a_class):
    """
    function for checking if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class and
    return True it it's and False if not

    Args:
        obj: object 1
        a_class: object 2

    Return: True if obj instance of a_class and False if not
    """
    if type(obj) != a_class:
        if isinstance(obj, a_class):
            return True
    return False
