#!/usr/bin/python3

""" function print square of #"""


def print_square(size):
    """
        function print square of #
        Args:
            size: size of squre
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end='')
            print("")
