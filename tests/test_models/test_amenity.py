#!/usr/bin/python3
"""
        import modules of class AmenityTest
"""
from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import pep8
import unittest
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """la puta que lo aprio"""
    @classmethod
    def setUpClass(cls):
        """la puta que lo aprio"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8menity(self):
        """la puta que lo aprio"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8(self):
        """la puta que lo aprio"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_modoc(self):
        """la puta que lo aprio"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_cladoc(self):
        """la puta que lo aprio"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_adocstr(self):
        """la puta que lo aprio"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class AmenityTest(unittest.TestCase):
    """la puta que lo aprio"""
    def test_is_subclass(self):
        """la puta que lo aprio"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """la puta que lo aprio"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """la puta que lo aprio"""
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in am.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """la puta que lo aprio"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

if __name__ == "__main__":
    unittest.main()
