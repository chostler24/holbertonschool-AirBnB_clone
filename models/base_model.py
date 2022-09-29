#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime, timezone

class BaseModel:
    """AirBnB Base class"""
    id = uuid.uuid4()
    
    def __init__(self, id=None):
        """__init__ of self"""
        if id is not None:
            self.id = str(id)
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
            
    def __str__(self):
        """overriding __str__ to print custom string"""
        print("[{}] {} <{}>".format(__class__, self.id, __dict__))

    def save(self):
        """update update_at to current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        
    def to_dict(self):
        """Returns dictionary of __dict__"""
        