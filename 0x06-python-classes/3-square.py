#!usr/bin/python3
"""
this module is a class defination

"""
class Square:
    """
    this class represent a square with a private instance attribute size
    Attribute:
         __size (int): The size of the square. It is a private attribute.
    """
    def __init__(self, size=0):
        """
        initilaizied the class object.
        args:
            size(int, option) default set to zero.
        raises:
            raises TypeError
            raises ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        a public instance method that returns the current square area

        """
        return  = self.__size ** 2
        
