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
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_unique_id(self):
        """ test if it generate unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1, user2)

    def test_user_module_docstring(self):
        """asdas asd asd asd"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """asdas asd asd asd"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """asdas asd asd asd"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

if __name__ == "__main__":
    unittest.main()
