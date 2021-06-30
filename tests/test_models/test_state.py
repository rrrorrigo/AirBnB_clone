#!/usr/bin/python3
"""
        import modules of class StateTest
"""
import unittest
from models.state import State
from models import state
import inspect
State = state.State


class StateTest(unittest.TestCase):
        """test cases for class object State"""
        @classmethod
        def setUp(cls):
                """test instance"""
                cls.state_f = inspect.getmembers(State, inspect.isfunction)

        def tearDown(self):
                """test instance"""
                pass

        def test_Init(self):
                """test instance"""
                t = State()
                self.assertIsInstance(t, State)
                self.assertTrue(hasattr(t, "id"))
                self.assertTrue(hasattr(t, "created_at"))
                self.assertTrue(hasattr(t, "updated_at"))

        def test_unique_id(self):
                """ test if it generate unique id"""
                State1 = State()
                State2 = State()
                self.assertNotEqual(State1, State2)

        def test_doc(self):
                """ test if class has docstring"""
                self.assertIsNotNone(state.__doc__)
                self.assertIsNotNone(State.__doc__)

if __name__ == "__main__":
    unittest.main()
