#!/usr/bin/python3

def print_square(size):
    """function print square of #"""
    if size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end='')
            print("")

# print_square(4)
# print("")
# print_square(10)
# print("")
# print_square(0)
# print("")
# print_square(1)
# print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
    