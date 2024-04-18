#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list) - 1
    if idx > length or idx < 0:
        return None
    return my_list[idx]
