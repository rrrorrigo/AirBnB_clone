#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
from models import review
from models.base_model import BaseModel
import unittest
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.city_f = inspect.getmembers(Review, inspect.isfunction)

    def test_city_module(self):
        """test cases for class object Amenity"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_city_class(self):
        """test cases for class object Amenity"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_city_func(self):
        """test cases for class object Amenity"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """test cases for class object Amenity"""
    def test_is_subclass(self):
        """test cases for class object Amenity"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_pl(self):
        """test cases for class object Amenity"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_usr(self):
        """test cases for class object Amenity"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_to_dic(self):
        """test cases for class object Amenity"""
        c = Review()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict(self):
        """test cases for class object Amenity"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Review()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test cases for class object Amenity"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

if __name__ == "__main__":
    unittest.main()
