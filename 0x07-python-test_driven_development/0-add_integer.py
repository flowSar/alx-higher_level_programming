#!/usr/bin/python3

""" function for adding two integers"""


def add_integer(a, b=98):
    """
        this function take two argument and return sum
        Args:
            a: first argument
            b: scon argument

        Return:
            the sum of a and b
    """
    try:
        a = int(a)
    except Exception as e:
        return TypeError("a must be an integer")

    try:
        b1 = int(b)
        if not isinstance(b, int):
            return TypeError("b must be an integer")
    except Exception as e:
        return TypeError("b must be an integer")
    return a + b1
