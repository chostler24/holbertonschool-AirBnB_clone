#!/usr/bin/python3
"""user.py module: creates a class User"""
from base_model import BaseModel


class User(BaseModel):
    """defines class User inheriting from BaseModel"""
    def __init__(self):
        """attributes"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
