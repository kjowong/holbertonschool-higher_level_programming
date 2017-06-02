#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


file_name = "add_item.json"

if not os.path.isfile(file_name):
    load_from_json_file(filename)
