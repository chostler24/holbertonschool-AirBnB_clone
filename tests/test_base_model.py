#!/usr/bin/python3
"""Unittests for base model"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittest class for Base Model"""
    def test___init__(self):
        self.assertEqual(BaseModel.id, "")