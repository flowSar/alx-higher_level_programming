#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    length_in = len(matrix[0])
    if length_in == 1:
    	print(matrix[0][0])
    	return
    if len(matrix) == 1:
    	print()
    	return
    for lst in matrix:
    	i = 0
    	for etm in lst:
    		print("{}".format(etm), end='')
    		if i < len(lst) -1:
    			print(" ", end = '')
    		i += 1
    	print("")
