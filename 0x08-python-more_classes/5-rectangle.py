
#!/usr/bin/python3

"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that finds the area of the rectangle.
        Returns: area of the rectangle.
        """
        rectangle_area = self.width * self.height
        return rectangle_area

    def perimeter(self):
        """
        Method that finds the perimeter of a rectangle.
        Returns: rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        rectangle_perimeter = 2 * (self.width + self.height)
        return rectangle_perimeter

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for j in range(self.__height))
        return string

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
