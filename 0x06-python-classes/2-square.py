#!/usr/bin/python3
"""
The class type defination

"""
class Square:
    """
    the class represent a square.
    attributes:
    __init__(self, size=0): size of the square with value zero
    """
    def __init__(self, size=0):
        """
        Initializes a square
         Args:
            size (int): size of aiii side of the square
         Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
