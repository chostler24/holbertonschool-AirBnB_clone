#!/bin/usr/python3
"""File storage"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        from sys import argv
        try:
            dict = {}
            for key, obj in self.__objects.items():
                dict[key] = obj.to_dict()
                save_to_json_file(dict, self.__file_path)
                pass
        except FileNotFoundError:
            dict = {}

    def reload(self):
        """deserializes the JSON file to __objects"""
