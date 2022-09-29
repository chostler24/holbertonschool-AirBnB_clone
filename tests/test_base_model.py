#!/usr/bin/python3
"""Unittests for base model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest class for Base Model"""
    def test___init__(self):
        """Testing for init"""
        self.assertNotEqual(self.id, "")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(BaseModel.__init__.__doc__, "")
        self.assertNotEqual(BaseModel.__str__.__doc__, "")
        self.assertNotEqual(BaseModel.save.__doc__, "")
        self.assertNotEqual(BaseModel.to_dict.__doc__, "")
