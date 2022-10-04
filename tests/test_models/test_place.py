#!/usr/bin/python3
"""Unittests for place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing the place"""

    def test_place(self):
        """Tests proper initiation of place"""
        self.place_test = Place()
        self.assertEqual(self.place_test.name, "")
        self.assertEqual(self.place_test.city_id, "")
        self.assertEqual(self.place_test.user_id, "")
        self.place_test.name = "Wisconsin"
        self.place_test.city_id = "Madison"
        self.place_test.user_id = "Madi"
        self.place_test.description = "Lovely location"
        self.place_test.number_rooms = 6
        self.place_test.number_bathrooms = 2
        self.place_test.max_guest = 12
        self.place_test.price_by_night = 120
        self.place_test.latitude = 26.3
        self.place_test.longitude = 77.9
        self.place_test.amenity_ids = [1, 2, 3, 4]
        self.assertEqual(self.place_test.name, "Wisconsin")
        self.assertEqual(self.place_test.city_id, "Madison")
        self.assertEqual(self.place_test.user_id, "Madi")
        self.assertEqual(self.place_test.description, "Lovely location")
        self.assertEqual(self.place_test.number_rooms, 6)
        self.assertEqual(self.place_test.number_bathrooms, 2)
        self.assertEqual(self.place_test.max_guest, 12)
        self.assertEqual(self.place_test.price_by_night, 120)
        self.assertEqual(self.place_test.latitude, 26.3)
        self.assertEqual(self.place_test.longitude, 77.9)
        self.assertEqual(self.place_test.amenity_ids, [1, 2, 3, 4])

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(Place.__init__.__doc__), "")
        self.assertNotEqual(len(Place.__str__.__doc__), "")
        self.assertNotEqual(len(Place.__class__.__doc__), "")
