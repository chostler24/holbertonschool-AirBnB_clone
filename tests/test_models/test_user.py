#!/usr/bin/python3
"""Unittests for user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing the user"""

    def test_user(self):
        """Tests proper initiation of user"""
        self.user_test = User()
        self.assertEqual(self.user_test.email, "")
        self.assertEqual(self.user_test.password, "")
        self.assertEqual(self.user_test.first_name, "")
        self.assertEqual(self.user_test.last_name, "")
        self.user_test.email = "doug@iscool.com"
        self.user_test.password = "teachMeHowToDougie"
        self.user_test.first_name = "Douglas"
        self.user_test.last_name = "Davison"
        self.assertEqual(self.user_test.email, "doug@iscool.com")
        self.assertEqual(self.user_test.password, "teachMeHowToDougie")
        self.assertEqual(self.user_test.first_name, "Douglas")
        self.assertEqual(self.user_test.last_name, "Davison")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(User.__init__.__doc__), "")
        self.assertNotEqual(len(User.__str__.__doc__), "")
        self.assertNotEqual(len(User.__class__.__doc__), "")
