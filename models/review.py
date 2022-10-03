#!/usr/bin/python3
"""review.py module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class defining review"""
    place_id = ""
    user_id = ""
    text = ""
