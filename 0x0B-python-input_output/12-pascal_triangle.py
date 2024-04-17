#!/usr/bin/python3
"""
This is module-level documentation
In this module has one function names load_from_json_file.
"""


def pascal_triangle(n):
    new_List = []
    big_list = []
    if n <= 0:
        return [[]]
    x = 0
    for i in range(n):
        new_List = [1]
        for j in range(i):
            if j == i - 1:
                new_List += [1]
            else:
                new_List += [x]

        for l in new_List[i:]:
            x += l
        big_list.append(new_List)
    return big_list
