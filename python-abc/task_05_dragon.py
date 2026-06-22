#!/usr/bin/python3
"""Module that defines SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """A mixin that provides swimming ability to a class."""

    def swim(self):
        """Print a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying ability to a class."""

    def fly(self):
        """Print a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that represents a dragon with swimming and flying abilities."""

    def roar(self):
        """Print a message indicating the dragon is roaring."""
        print("The dragon roars!")
