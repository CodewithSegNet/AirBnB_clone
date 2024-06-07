#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_initialization(self):
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_attributes(self):
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_str(self):
        model_str = str(self.my_model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn(f'({self.my_model.id})', model_str)
        self.assertIn(f"'name': 'My First Model'", model_str)
        self.assertIn(f"'my_number': 89", model_str)

    def test_save(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)
        self.assertTrue(self.my_model.updated_at > old_updated_at)

    def test_to_dict(self):
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['id'], self.my_model.id)
        self.assertEqual(model_dict['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.my_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
