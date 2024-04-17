#!/usr/bin/python3
"""

In this module has one function names load_from_json_file.
"""
import json
import sys

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

my_list = []

if len(sys.argv) > 1:
	for item in sys.argv[1:]:
		my_list.append(item)

print(my_list)

with open("python_list.txt", "w") as file:
	file.write("hello")

loaded_data = load_from_json_file("python_list.txt")
save_to_json_file(loaded_data, "add_item.json")
