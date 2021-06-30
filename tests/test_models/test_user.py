#!/usr/bin/python3
"""
        import modules of class UserTest
"""
import unittest
from datetime import datetime
import os
import inspect
from models import user
from models.base_model import BaseModel
User = user.User

class UserTest(unittest.TestCase):
    """test cases for class object User"""

    @classmethod
    def setUp(cls):
        """test instance"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

    def test_unique_id(self):
        """ test if it generate unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1, user2)

    def test_doc(self):
        """ test if class has docstring"""
        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)

if __name__ == "__main__":
    unittest.main()
