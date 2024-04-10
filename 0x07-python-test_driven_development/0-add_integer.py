#!/usr/bin/python3

""" function for adding two integers"""


def add_integer(a, b=98):

    try:
        a = int(a)
    except Exception as e:
        return "a must be an integer"

    try:
        b = int(b)
    except Exception as e:
        return "b must be an integer"
    return a + b
