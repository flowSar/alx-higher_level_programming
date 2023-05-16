#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
    	print()
    	return
    for i in range(3):
    	for j in range(3):
    		print("{}".format(matrix[i][j]), end='')
    		if (j < 2):
    			print(" ", end='')
    	print("")
