#!/usr/bin/python3
"""

In this module has one function names load_from_json_file.
"""
import json
import sys
from os import path

save_to_json = __import__("5-save_to_json_file")
load_from_json = __import__("6-load_from_json_file")

my_list = []
file_name = "add_item.json"

if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        my_list.append(item)

if not path.exists("add_item.json"):
    save_to_json.save_to_json_file([], file_name)

loaded_data = load_from_json.load_from_json_file(file_name)
loaded_data += my_list
save_to_json.save_to_json_file(loaded_data, file_name)
