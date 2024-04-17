#!/usr/bin/python3
"""

In this module has one function names load_from_json_file.
"""
import json
import sys

save_to_json = __import__("5-save_to_json_file")
load_from_json = __import__("6-load_from_json_file")


my_list = []

if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        my_list.append(item)


with open("python_list.json", 'w') as file:
    json.dump(my_list, file)

loaded_data = load_from_json.load_from_json_file("python_list.json")
save_to_json.save_to_json_file(loaded_data, "add_item.json")
