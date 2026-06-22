#!/usr/bin/python3
"""Module that defines Shape, Circle, Rectangle classes and shape_info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """An abstract class that serves as a base for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A class that represents a circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class that represents a rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
