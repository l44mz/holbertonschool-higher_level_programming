#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract class that serves as a base for all animal types."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """A class that represents a dog, inheriting from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """A class that represents a cat, inheriting from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
