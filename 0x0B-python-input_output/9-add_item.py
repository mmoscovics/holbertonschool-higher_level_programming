#!/usr/bin/python3
""" Script that adds all arguments to a Python list
and then save them to a file.
"""
import json
from sys import argv
from os.path import exists


if __name__ == "__main__":
    save = __import__('7-save_to_json_file').save_to_json_file
    load = __import__('8-load_from_json_file').load_from_json_file

    py_list = []

    if exists("add_item.json"):
        py_list = load("add_item.json")
    py_list.extend(argv[1:])
    save(py_list, "add_item.json")
