#!/usr/bin/python3
"""Unittests for base model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest class for Base Model"""
    def test___init__(self):
        """Testing for init"""
        self.assertNotEqual(self.id, "")
    
    def test___str__(self):
        self.assertTrue(self)

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(BaseModel.__init__.__doc__), "")
        self.assertNotEqual(len(BaseModel.__str__.__doc__), "")
        self.assertNotEqual(len(BaseModel.save.__doc__), "")
        self.assertNotEqual(len(BaseModel.to_dict.__doc__), "")
    
    def test_creation(self):
        """Tests creation of BaseModel object"""
        obj = BaseModel()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
