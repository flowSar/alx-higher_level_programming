#!/usr/bin/python3
"""function check if obj is instance of a_class"""


def is_kind_of_class(obj, a_class):
    """
    function check if obj is instance of a_class or if the object
    is an instance of a class that inherited from and return True it it's
    and False if not

    Args:
        obj: object 1
        a_class: object 2

    Return: True if obj instance of a_class and False if not

    """
    return type(obj) == a_class
