#!/usr/bin/python3

""" function divides all elements of a matrix by div """


def matrix_divided(matrix, div):

    """
        function divides all elements of a matrix by div

        Args:
            matrix: matrix
            div: div

        Return:
            if all goes will return matrix/div
    """

    new_matrix = []
    inside_matrix = []
    first_row = len(matrix[0])
    row_number = 0
    if not isinstance(div, int | float):
        raise TypeError("div must be a number\n")
    if div == 0:
        raise ZeroDivisionError("division by zero\n")

    for mat in matrix:
        for elm in mat:
            row_number += 1
            if not isinstance(elm, int | float):
                raise TypeError("""matrix must be a matrix"""
                                """(list of lists) of integers/floats\n""")
            value = format(elm/div, ".2f")
            inside_matrix += [float(value)]
        if row_number != first_row:
            raise TypeError("Each row of the matrix must have the same size\n")
        row_number = 0
        new_matrix += [inside_matrix]
        inside_matrix = []

    return new_matrix
