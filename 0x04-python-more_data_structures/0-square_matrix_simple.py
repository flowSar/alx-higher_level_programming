#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    length = len(matrix)
    len_in = len(matrix[0])
    new_matrix = [[0 for _ in range(len_in)] for _ in range(length)]

    for i in range(length):
        for j in range(len_in):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
