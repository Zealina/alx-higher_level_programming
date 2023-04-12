#!/usr/bin/python3
"""Defines a rebel child of 'Int' object"""


class MyInt(int):
    """Swaps the '==' and the '!=' for one another"""
    def __eq__(self, other):
        """overrides the '==' and replace with '!='"""
        return int(self) != int(other)

    def __ne__(self, other):
        """overrides the '!=' and replace with'=='"""
        return int(self) == int(other)
