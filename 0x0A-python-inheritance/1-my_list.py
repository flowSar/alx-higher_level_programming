#!/usr/bin/python3
"""
This is module-level documentation
In this module has one class names MyList.
"""


class MyList(list):
    """
        Print the elements of the list in sorted order
        This method creates a copy of the list, sorts it in ascending order,
        and then prints the sorted list.
        Args:
            None
        Returns:
            None

    """
    def print_sorted(self):
        """sort a list and print it"""
        my_list = [elm for elm in self]
        my_list.sort()
        print(my_list)
