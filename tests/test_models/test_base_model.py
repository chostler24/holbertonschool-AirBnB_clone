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
        """Testing for str"""
        self.assertTrue(self)

    def test_save(self):
        """Testing for save"""
        test_it = BaseModel()
        self.assertIsNotNone(test_it.updated_at)

    def test_to_dict(self):
        """Testing for to_dict"""
        check_it = BaseModel()
        new_dict = check_it.to_dict()
        self.assertIsNotNone(new_dict)

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
