#!/usr/bin/python3
"""
        import modules of class ReviewTest
"""
import unittest
import models
import os
from models.review import Review
from models.base_model import BaseModel


class ReviewTest(unittest.TestCase):
    """test cases for class object Review"""

    @classmethod
    def setUp(self):
        """test instance"""
        self.t = Review()

    def tearDown(self):
        """test instance"""
        pass

    def test_Init(self):
        """test instance"""
        self.assertIsInstance(self.t, BaseModel)

    def test_unique_id(self):
        """ test if it generate unique id"""
        Review1 = Review()
        Review2 = Review()
        self.assertNotEqual(Review1, Review2)

    def test_doc(self):
        """ test if class has docstring"""
        self.assertIsNotNone(models.review.__doc__)
        self.assertIsNotNone(Review.__doc__)

if __name__ == "__main__":
    unittest.main()
