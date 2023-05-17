#!/usr/bin/python3

def search_replace(my_list, search, replace):
    length = len(my_list)
    new_matrix = [0 for _ in range(length)]

    for i in range(length):
        if search == my_list[i]:
            new_matrix[i] = replace
        else:
            new_matrix[i] = my_list[i]
    return new_matrix
