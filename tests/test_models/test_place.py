#!/usr/bin/python3
"""
Contains the TestplaceDocs classes
"""

from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import unittest
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_place_module(self):
        """test cases for class object Amenity"""
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class(self):
        """test cases for class object Amenity"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func(self):
        """test cases for class object Amenity"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """test cases for class object Amenity"""
    def test_is_subclass(self):
        """test cases for class object Amenity"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_nam(self):
        """test cases for class object Amenity"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_to_dic(self):
        """test cases for class object Amenity"""
        c = Place()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict(self):
        """test cases for class object Amenity"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = Place()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test cases for class object Amenity"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

if __name__ == "__main__":
    unittest.main()
