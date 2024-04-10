#!/usr/bin/python3


def matrix_divided(matrix, div):

    """ function divides all elements of a matrix"""

    new_matrix = []
    inside_matrix = []
    for mat in matrix:
        for elm in mat:
            value = format(elm/div, ".2f")
            inside_matrix += [float(value)]
        new_matrix += [inside_matrix]
        inside_matrix = []

    return new_matrix
