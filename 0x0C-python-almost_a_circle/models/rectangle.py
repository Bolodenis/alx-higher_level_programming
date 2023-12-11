#!/usr/bin/python3
'''
   Defines the Class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a new instance of the Rectangle class.
        width (property): Getter and setter methods for the width property.
        height (property): Getter and setter methods for the height property.
        x (property): Getter and setter methods for the x property.
        y (property): Getter and setter methods for the y property.
        area(self): Method for finding the area of the rectangle.
        display(self): Method for printing the rectangle using the `#` character.
        __str__(self): String representation of the Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle (default is 0).
            y (int, optional): The y-coordinate of the rectangle (default is 0).
            id (int, optional): An identifier for the object. If not provided, it is automatically generated.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width property."""
        return self._width
    
    @width.setter
    def width(self, value):
        """Setter method for the width property."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """Getter method for the height property."""
        return self._height
    
    @height.setter
    def height(self, value):
        """Setter method for the height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def x(self):
        """Getter method for the x property."""
        return self._x
    
    @x.setter
    def x(self, value):
        """Setter method for the x property."""
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @property
    def y(self):
        """Getter method for the y property."""
        return self._y
    
    @y.setter
    def y(self, value):
        """Setter method for the y property."""
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """Method for finding the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Method for printing the rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]

            print("")
    
    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        
    def to_dictionary(self):
         """Returns the dictionary representation of a Rectangle."""
         return {
        'id': self.id,
        'width': self.width,
        'height': self.height,
        'x': self.x,
        'y': self.y
        }

     def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
