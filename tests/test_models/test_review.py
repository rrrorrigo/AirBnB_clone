#!/usr/bin/python3
"""
        import modules of class ReviewTest
"""
import unittest
from models.review import Review
import models
import os


class ReviewTest(unittest.TestCase):
        """test cases for class object Review"""
        def test_Init(self):
                """test instance"""
                t = Review()
                self.assertIsInstance(t, Review)

        def test_unique_id(self):
                """ test if it generate unique id"""
                Review1 = Review()
                Review2 = Review()
                self.assertNotEqual(Review1, Review2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(models.Review.__doc__)
                self.assertIsNotNone(Review.__doc__)

if __name__ == "__main__":
    unittest.main()
