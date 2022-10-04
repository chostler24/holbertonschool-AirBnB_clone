#!/usr/bin/python3
"""Unittests for file_storage"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_file_storage(self):
        """Tests proper initiation of file_storage"""
        self.file_storage_test = FileStorage()
        self.assertEqual(self.file_storage_test.__objects, {})
        self.assertEqual(self.file_storage_test.__file_path, "file.json")
        self.file_storage_test.__objects = {"a", 6}
        self.file_storage_test.__file_path = "newfile.json"
        self.assertEqual(self.file_storage_test.__objects, {"a", 6})
        self.assertEqual(self.file_storage_test.__file_path, "newfile.json")
