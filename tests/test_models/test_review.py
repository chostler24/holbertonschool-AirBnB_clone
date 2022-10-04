#!/usr/bin/python3
"""Unittests for review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing the review"""

    def test_review(self):
        """Tests proper initiation of review"""
        self.review_test = Review()
        self.assertEqual(self.review_test.place_id, "")
        self.assertEqual(self.review_test.user_id, "")
        self.assertEqual(self.review_test.text, "")
        self.review_test.place_id = "A-B-1"
        self.review_test.state_id = "N-Y-2"
        self.review_test.text = "yoyo"
        self.assertEqual(self.review_test.place_id, "A-B-1")
        self.assertEqual(self.review_test.state_id, "N-Y-2")
        self.assertEqual(self.review_test.text, "yoyo")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(Review.__init__.__doc__), "")
        self.assertNotEqual(len(Review.__str__.__doc__), "")
        self.assertNotEqual(len(Review.__class__.__doc__), "")
