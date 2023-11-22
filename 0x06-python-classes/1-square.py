#!usr/bin/python3
""" creating class with element square """

class Square:
    """
    Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """ 
        initializes a square

        Args:
            size (int): The size of the square.
         """
        self.__size = size

    def square_1(self):
        self.__square = self.__size * 2
