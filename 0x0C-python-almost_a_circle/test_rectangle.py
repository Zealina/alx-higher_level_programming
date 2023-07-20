#!/usr/bin/python3
"""
Unittests for the rectangle module
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Contains the test cases of class 'Rectangle'"""
    def setUp(self):
        self.dummy = Rectangle(1, 2, 3, 4)
        self.dummy2 = Rectangle(2, 4, 6, 8)
        self.dummy3 = Rectangle(3, 6, 9, 12, 15)
        self.dummy_base = Base()

    def test_inheritance(self):
         self.assertTrue(issubclass(Rectangle, Base))
         self.assertIn(Base, Rectangle.__bases__)

    def test_assign_values(self):
        self.assertEqual(self.dummy3.width, 3)
        self.assertEqual(self.dummy3.height, 6)
        self.assertEqual(self.dummy3.x, 9)
        self.assertEqual(self.dummy3.y, 12)
        self.assertEqual(self.dummy3.id, 15)

    def test_init(self):
        self.assertIn('__init__', dir(Rectangle))

    def test_super_id(self):
        self.assertTrue(self.dummy.id, 1)
        self.assertTrue(self.dummy2.id, 2)
        self.assertTrue(self.dummy_base.id, 3)

    def test_privacy(self):
        pass

    def test_validate_attributes(self):
        pass
        """
        a = {'width':self.dummy.width, 'height':self.dummy.height, 
             'x':self.dummy.x, 'y':self.dummy.y}
        for key, value in a.items():
            if key in ['width', 'height']:
                self.assertRaises(ValueError, 0)
                self.assertRaises(ValueError, -5)
                self.assertRaises(ValueError, -66)
            elif key in ['x', 'y']:
                self.assertRaises(ValueError, -6)
                self.assertRaises(ValueError, -999)
                self.dummy.x(0)
                self.Equal(self.dummy.x, 0)
        """

    def test_area(self):
        self.assertEqual(self.dummy.area(), 2)
        self.assertEqual(self.dummy2.area(), 8)
        self.assertEqual(self.dummy3.area(), 18)

    def test_display(self):
        pass

    def test_string_representation(self):
        self.assertEqual(self.dummy2.__str__(), '[Rectangle] (2) 6/8 - 4/2]')
        self.assertEqual(self.dummy3.__str__(), '[Rectangle] (15) 9/12 - 3/6]')

    def test_update(self):
        pass
