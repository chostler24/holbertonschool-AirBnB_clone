#!/usr/bin/python3
"""user.py module: creates a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """defines class User inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
