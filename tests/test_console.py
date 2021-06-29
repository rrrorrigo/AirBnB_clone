#!/usr/bin/python3


import console
import inspect
import pep8 as textstyles
import unittest
HBNBCommand = console.HBNBCommand


class Console_test(unittest.TestCase):
    def checkeamelpep8(self):
        pepa = textstyles.StyleGuide(quiet=True)
        result = pepa.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
