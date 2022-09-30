#!/bin/usr/python3
"""File storage"""
import json

class FileStorage:
    """File Storage Class"""
    __objects = {}
    
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""