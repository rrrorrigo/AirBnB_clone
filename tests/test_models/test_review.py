#!/usr/bin/python3
"""
        import modules of class ReviewTest
"""
import unittest
from models.review import Review
from models import review
import inspect
Review = review.Review


class ReviewTest(unittest.TestCase):
        """test cases for class object Review"""
        @classmethod
        def setUp(cls):
                """test instance"""
                cls.review_f = inspect.getmembers(Review, inspect.isfunction)

        def tearDown(self):
                """test instance"""
                pass

        def test_Init(self):
                """test instance"""
                t = Review()
                self.assertIsInstance(t, Review)
                self.assertTrue(hasattr(t, "id"))
                self.assertTrue(hasattr(t, "created_at"))
                self.assertTrue(hasattr(t, "updated_at"))

        def test_unique_id(self):
                """ test if it generate unique id"""
                Review1 = Review()
                Review2 = Review()
                self.assertNotEqual(Review1, Review2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(review.__doc__)
                self.assertIsNotNone(Review.__doc__)

if __name__ == "__main__":
    unittest.main()
