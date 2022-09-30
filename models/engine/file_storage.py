#!/bin/usr/python3
"""File storage"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """Write to text file from object"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))


def load_from_json_file(filename):
    """Create object from JSON"""
    with open(filename, 'r') as file:
        return json.load(file)


class FileStorage:
    """File Storage Class"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects = "{}.id".format(obj.__class__)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        from sys import argv
        try:
            lst = (load_from_json_file(self.__file_path))
        except FileNotFoundError:
            lst = []
        save_to_json_file(lst + argv[1:], self.__file_path)

    def reload(self):
        """deserializes the JSON file to __objects"""
