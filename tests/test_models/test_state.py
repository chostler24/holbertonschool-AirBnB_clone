#!/usr/bin/python3
"""Unittests for state"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing the state"""

    def test_state(self):
        """Tests proper initiation of state"""
        self.state_test = State()
        self.assertEqual(self.state_test.name, "")
        self.state_test.name = "Oklahoma"
        self.assertEqual(self.state_test.name, "Oklahoma")

    def test_docs(self):
        """Testing for documentation"""
        self.assertNotEqual(len(State.__init__.__doc__), "")
        self.assertNotEqual(len(State.__str__.__doc__), "")
        self.assertNotEqual(len(State.__class__.__doc__), "")
