#!/usr/bin/python3

"""function print full name"""


def say_my_name(first_name, last_name=""):
    """
        function take two argumen first name and last name and print
        if they're string if not raise exception
        Args:
            first_name: first name
            last_name: last name

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
