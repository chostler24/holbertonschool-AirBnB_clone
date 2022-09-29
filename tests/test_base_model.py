#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittest for Base Model"""
    def test___init__(self):
        self.id(BaseModel.id)