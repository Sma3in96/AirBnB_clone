#!/usr/bin/python3
""" testing base model"""
import unittest
import datetime
from models.base_model import BaseModel


class testbasemodel(unittest.TestCase):
    """ test for base model """

    exemple = BaseModel()

    def test_base_model(self):
        """test attribute of base model"""

        self.exemple.name = "ismail"
        self.exemple.number = "20"
        self.exemple.save()
        json_save = self.exemple.to_dict()

        self.assertEqual(self.exemple.name, json_save['name'])
        self.assertEqual(self.exemple.number, json_save['number'])
        self.assertEqual('BaseModel', json_save['__class__'])
        self.assertEqual(self.exemple.id, json_save['id'])

    def test_save(self):
        """ test save methode """

        self.exemple.name = "value"
        self.exemple.save()
        dict1 = self.exemple.to_dict()

        self.exemple.name = "2nd value"
        self.exemple.save()
        dict2 = self.exemple.to_dict()

        self.assertIsInstance(self.exemple.id, str)
        self.assertIsInstance(self.exemple.updated_at, datetime.datetime)

        self.assertEqual(dict1['created_at'], dict2['created_at'])
        self.assertNotEqual(dict2['updated_at'], dict1['updated_at'])


if __name__ == '__main__':
    unittest.main()
