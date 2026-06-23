#!/usr/bin/python3
"""Module for duck typing with abstract base classes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Class representing a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize Circle with a radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape: Any object implementing area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
