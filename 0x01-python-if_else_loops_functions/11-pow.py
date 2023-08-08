#!/usr/bin/python3
def pow(a, b):
    x = a
    p = b
    if b < 0:
        p =-p
    if b == 0:
    	return 1
    for i in range(1, p):
       x *= a
    if b < 0:
        return 1/x
    return x
