#!/usr/bin/python3
"""Unittests for city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testing the city"""

    def test_city(self):
        """Tests proper initiation of city"""
        self.city_test = City()
        self.assertEqual(self.city_test.name, "")
        self.assertEqual(self.city_test.state_id, "")
        self.city_test.name = "New York City"
        self.city_test.state_id = "New York"
        self.assertEqual(self.city_test.name, "New York City")
        self.assertEqual(self.city_test.state_id, "New York")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(City.__init__.__doc__), "")
        self.assertNotEqual(len(City.__str__.__doc__), "")
        self.assertNotEqual(len(City.__class__.__doc__), "")
