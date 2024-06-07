#!/usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models



class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up environment for test case"""
        self.storage = FileStorage()
        self.test_file_path = "test_file.json"
        self.storage._FileStorage__file_path = self.test_file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_file_path_exists(self):
        """Test that the __file_path attribute exists and is set correctly"""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertEqual(self.storage._FileStorage__file_path, self.test_file_path)

    def test_new(self):
        """Test adding new object to storage"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f'BaseModel.{obj.id}'
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test saving object to file"""
        obj = BaseModel()
        self.storage.new(obj)
        old_updated_at = obj.updated_at
        self.storage.save()

        self.assertNotEqual(obj.updated_at, old_updated_at)

        # Check if file exists and contains the saved object
        self.assertTrue(os.path.exists(self.test_file_path))
        with open(self.test_file_path, 'r') as file:
            data = json.load(file)
            key = f'BaseModel.{obj.id}'
            self.assertIn(key, data)
            self.assertEqual(data[key]['id'], obj.id)

    def test_reload(self):
        """Test reloading objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Clear current objects and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = f'BaseModel.{obj.id}'
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)


if __name__ == '__main__':
    unittest.main()
