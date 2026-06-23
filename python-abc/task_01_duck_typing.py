#!/usr/bin/env python3
"""Module that defines Shape abstract class with Circle and Rectangle."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method that returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """A class that defines a Circle."""

    def __init__(self, radius):
        """Instantiates a Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Returns the perimeter (circumference) of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """A class that defines a Rectangle."""

    def __init__(self, width, height):
        """Instantiates a Rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
