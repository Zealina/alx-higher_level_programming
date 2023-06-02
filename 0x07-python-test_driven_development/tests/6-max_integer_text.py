#!/usr/bin/python3
"""This module contains the unit test for the function 'max_integer'"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.Testcase):
    def testFloats(self):
        self.assertEqual(max_integer([2.4, 3, 4.15], 
