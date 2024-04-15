#!/usr/bin/python3
"""
This is module-level documentation
In this module has one class names MyList.
"""


class MyList(list):

    def print_sorted(self):
        """sort a list and print it"""
        my_list = [elm for elm in self]
        my_list.sort()
        print(my_list)
