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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, val in self.__objects.items():
            obj_dict[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(obj_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                obj_dict = json.loads(f.read())
                for key, val in obj_dict.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
