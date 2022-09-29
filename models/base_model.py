#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime


class BaseModel:
    """AirBnB Base class"""

    def __init__(self, id=None):
        """__init__ of self"""
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """overriding __str__ to print custom string"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """update update_at to current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
