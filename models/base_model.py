#!/usr/bin/python3
"""Base Model"""
import uuid

class BaseModel:
    """AirBnB Base class"""
    id = uuid.uuid4()
    
    def __init__(self, id=None):
        if id is not None:
            self.id = str(id)
            # self.created_at = 
            