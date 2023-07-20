#!/usr/bin/python3
"""
Unittests for the square module
"""

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Contains the test cases of class 'Square'"""
    def setUp(self):
        self.dummy = Square(1, 2, 3)
        self.dummy2 = Square(2, 4, 6)
        self.dummy3 = Square(3, 6, 9, 12)
        self.dummy_base = Base()

    def test_inheritance(self):
         self.assertTrue(issubclass(Square, Rectangle))
         self.assertIn(Rectangle, Square.__bases__)

    def test_assign_values(self):
        self.assertEqual(self.dummy3.size, 3)
        self.assertEqual(self.dummy3.x, 6)
        self.assertEqual(self.dummy3.y, 9)
        self.assertEqual(self.dummy3.id, 12)

    def test_init(self):
        self.assertIn('__init__', dir(Square))

    def test_super_id(self):
        self.assertTrue(self.dummy.id, 1)
        self.assertTrue(self.dummy2.id, 2)
        self.assertTrue(self.dummy_base.id, 3)
        self.assertTrue(self.dummy3.id, 12)

    def test_privacy(self):
        pass

    def test_area(self):
        self.assertEqual(self.dummy.area(), 1)
        self.assertEqual(self.dummy2.area(), 4)
        self.assertEqual(self.dummy3.area(), 9)

    def test_display(self):
        pass

    def test_string_representation(self):
        pass

    def test_update(self):
        pass
