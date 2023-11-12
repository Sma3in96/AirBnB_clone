#!/usr/bin/python3
""" unitests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
"""import json"""


class StorageTests(unittest.TestCase):
    """ testing storage write """

    model = BaseModel()

    def testInstance(self):
        """ Check if storage is instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreModel(self):
        """ Testing save and reload """
        self.model.full_name = "BaseModel Instance"
        self.model.save()
        dict1 = self.model.to_dict()
        all_objs = storage.all()

        key = dict1['__class__'] + "." + dict1['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ Test save, reload and update functions """
        self.model.my_name = "name 1st"
        self.model.save()
        dict2 = self.model.to_dict()
        all_objs = storage.all()

        key = dict2['__class__'] + "." + dict2['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(dict2['my_name'], "name 1st")

        created_1st = dict2['created_at']
        updated_2nd = dict2['updated_at']

        self.model.my_name = "name 2nd"
        self.model.save()
        dict2 = self.model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        created_2nd = dict2['created_at']
        update2 = dict2['updated_at']

        self.assertEqual(created_1st, created_2nd)
        self.assertNotEqual(updated_2nd, update2)
        self.assertEqual(dict2['my_name'], "name 2nd")

    def testjsonsaving(self):
        """json file testing"""
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testHasAttributes(self):
        """testing if path and objects exists"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_reload(self):
        """test if reload after empty obejcts """
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        temp_objects = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(temp_objects, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(temp_objects[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
