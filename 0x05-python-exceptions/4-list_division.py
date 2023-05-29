#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as e:
            print("division by zero")
            result = 0
        except TypeError as e1:
            print("wrong type")
            result = 0
       	except IndexError as e2:
       	    print("out of range")
            result = 0
        finally:
            lst +=[result]

    return lst
