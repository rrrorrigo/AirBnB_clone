#!/usr/bin/python3
"""
        import modules of class UserTest
"""
import unittest
from models.user import User
import models
from datetime import datetime
import os


class UserTest(unittest.TestCase):
    """test cases for class object User"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = User()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, User)

    def test_unique_id(self):
        """ test if it generate unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1, user2)

    def test_doc(self):
        """ test if class has docstring"""
        self.assertIsNotNone(models.user.__doc__)
        self.assertIsNotNone(User.__doc__)

if __name__ == "__main__":
    unittest.main()
