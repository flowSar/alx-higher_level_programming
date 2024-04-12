#!/usr/bin/python3
""" Doc """

print_square = __import__('4-print_square').print_square

try:
    print_square("3")
except Exception as e:
    print(e)