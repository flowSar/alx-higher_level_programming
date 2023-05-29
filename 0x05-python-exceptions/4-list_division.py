#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lst = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            lst +=[result]
        except ZeroDivisionError as e:
            print("division by zero")
            lst += [0]
            continue
        except TypeError as e1:
            print("wrong type")
            lst += [0]
            continue
       	except IndexError as e2:
       	    print("out of range")
            lst += [0]
            continue
    return lst
