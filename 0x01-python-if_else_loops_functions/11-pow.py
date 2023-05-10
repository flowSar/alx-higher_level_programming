#!/usr/bin/python3
def pow(a, b):
    x = a
    pow = b
    if b < 0:
        pow =-pow
    if b == 0:
    	return 1
    for i in range(1,pow):
       x *= a
    if b < 0:
        return 1/x
    return x
