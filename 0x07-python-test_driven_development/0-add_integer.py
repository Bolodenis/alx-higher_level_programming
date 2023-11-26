#!/usr/bin/python3
"""Defines an integer addition function."""
def add_integer(a, b=98):
    """
    a function that adds float or int.
    args:
        a(float, int): takes either a float or int as its first argument.
        b(float, int): takes either a float or int as its second argument.
    return:
        returns the addition of a and b as an integer.
    raise: 
        TypeError: when the arguments are neither int or float

    """
    if (not isinstance(a, (float)) and not isinstance(a, (int))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (float)) and not isinstance(b, (int))):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return int(a + b)

