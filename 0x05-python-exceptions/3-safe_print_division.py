#!/usr/bin/python3
def safe_print_division(a, b):
	result = 0
	try:
		result = a / b
		print("Inside result: {}".format(result))
	except Exception as e:
		print("Inside result: {}".format(None))
	finally:
		if (result == 0):
			return None
		return result
