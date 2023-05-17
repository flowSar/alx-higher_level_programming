#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dic = {}

    for key in sorted(a_dictionary):
    	print("{}: {}".format(key, a_dictionary[key]))

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 5, 3] }
print_sorted_dictionary(a_dictionary)