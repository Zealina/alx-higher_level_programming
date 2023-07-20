#!/usr/bin/python3
"""
Test cases for the base module
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Contains the test cases for the base module
    """
    def test_instance_id(self):
        dummy1 = Base()
        self.assertEqual(dummy1.id, 1)
        dummy2 = Base()
        self.assertEqual(dummy2.id, 2)
        dummy3 = Base(13)
        self.assertEqual(dummy3.id, 13)
        dummy4 = Base()
        self.assertEqual(dummy4.id, 3)
        self.assertIn('_Base__nb_objects', dir(Base))
