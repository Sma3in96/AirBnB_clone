#!/usr/bin/python3
"""Unittest for user.py"""

import unittest
import datetime
from models.user import User


class UserCase(unittest.TestCase):
    """testing user class"""

    user1 = User()

    def class_exist(self):
        """class exists"""
        self.assertEqual(str(type(self.user1)), "<class 'models.user.User'>")

    def subclass_test(self):
        """testing if User is subclass of BaseModel class"""
        self.assertIsInstance(self.user1, User)

    def Attributes_exist(self):
        """testing if attr is created"""
        self.assertTrue(hasattr(self.user1, 'email'))
        self.assertTrue(hasattr(self.user1, 'password'))
        self.assertTrue(hasattr(self.user1, 'first_name'))
        self.assertTrue(hasattr(self.user1, 'last_name'))
        self.assertTrue(hasattr(self.user1, 'id'))
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))

    def testing_type_of_attrib(self):
        """testing if attr has correct data type"""
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.id, str)
        self.assertIsInstance(self.user1.created_at, datetime.datetime)
        self.assertIsInstance(self.user1.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
