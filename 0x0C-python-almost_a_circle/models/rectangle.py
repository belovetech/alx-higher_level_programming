#!/usr/bin/python3
"""Representation of Rectangle class inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Defines Rectangle class with its attributes

    Args:
        Base (Class): Class inherits from
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle with optional width and height

        Args:
            width  (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x of the rectangle
            y (int): y of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property getter: retrieve the wdith of the class.

        Returns:
            width (int): the width instance attribute

        width.setter: set the width of the class.
        it also checks for TypeError and ValueError.

        Args:
            value (int): value to set the width to

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property getter: retrieve the height of the class.

        Returns:
            height (int): the height instance attribute

        height.setter: set the height of the class
        it also checks for TypeError and valueError

        Args:
            value (int): value to set the height to

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x property getter: retrieve the x of the class

        Returns:
            x (int): the x instance of the class

        x.setter: set the x of the class
        it also checks for TypeError and ValueError

        Args:
            value (int): value to set the x to

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y property getter: retrieve the y of the class

        Returns:
            y (int): the y instance of the class

        y.setter: set the y of the class
        it also checks for TypeError and ValueError

        Args:
            value (int): value to set the y to

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes area of the rectangle.

        Returns:
            Area value of the rectangle instances
        """
        return self.__width * self.__height
