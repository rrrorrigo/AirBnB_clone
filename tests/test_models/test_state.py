#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import unittest
State = state.State


class TestStateDocs(unittest.TestCase):
    """test cases for class object Amenity"""
    @classmethod
    def setUpClass(cls):
        """test cases for class object Amenity"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_state_module(self):
        """test cases for class object Amenity"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_state_class(self):
        """test cases for class object Amenity"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func(self):
        """test cases for class object Amenity"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """test cases for class object Amenity"""
    def test_is_subclass(self):
        """test cases for class object Amenity"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_nam(self):
        """test cases for class object Amenity"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dic(self):
        """test cases for class object Amenity"""
        c = State()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict(self):
        """test cases for class object Amenity"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = State()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test cases for class object Amenity"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

if __name__ == "__main__":
    unittest.main()
