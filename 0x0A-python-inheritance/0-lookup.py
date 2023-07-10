#!/usr/bin/python3
"""
Title: Lookup Function
Description: A function that returns the list of available attributes and
methods of an object.
Author: Your Name
Date: July 10, 2023
"""

def lookup(obj):
    """Return the list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
    
    Returns:
        A list of strings representing the names of the attributes and methods
        of the object.
    """
    return dir(obj)
