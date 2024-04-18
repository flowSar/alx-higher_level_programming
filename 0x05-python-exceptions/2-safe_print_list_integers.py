#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
	try:
		d_printed = 0
		for i in range(x):
			if (isinstance(my_list[i], int) != True):
				continue
			print("{:d}".format(my_list[i]), end = '')
			d_printed += 1
		print("")
		return d_printed
	except IndexError as e:
		print("")
		return d_printed

lis = [1,2,3,'g']
print("{}".format(safe_print_list_integers(lis, 4)));
