#!/usr/bin/python3
"""Unittests for amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing the amenity"""

    def test_amenity(self):
        """Tests proper initiation of Amenity"""
        self.amenity_test = Amenity()
        self.assertEqual(self.amenity_test.name, "")
        self.amenity_test.name = "In-unit Washer and Dryer"
        self.assertEqual(self.amenity_test.name, "In-unit Washer and Dryer")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(Amenity.__init__.__doc__), "")
        self.assertNotEqual(len(Amenity.__str__.__doc__), "")
        self.assertNotEqual(len(Amenity.__class__.__doc__), "")
