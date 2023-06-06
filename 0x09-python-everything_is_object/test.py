#!/usr/bin/python3

class User:

	def __init__(self):
		pass

	def increment(x, y):
		x.append(0)
		x = y


if __name__ == '__main__':
	
	x = [1,2,3,4]
	y = [5,6,7,8]

	User.increment(x, y)
	print(x)