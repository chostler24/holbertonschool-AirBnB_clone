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
