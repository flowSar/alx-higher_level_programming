#!/usr/bin/python3


def print_square(size):
    """
        function print square of #
        Args:
            size: size of squre
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end='')
            print("")
