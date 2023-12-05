#!/usr/bin/python3
""" 
This module checks for the list of available 
attributes and methods of an object
"""
def lookup(obj):
    """
    a function that checks for list of available attributes
    args:
        Takes obj as parameter to be tested
    Return:
        list of available 
        attributes and methods of an object
    """
    return dir(obj)
