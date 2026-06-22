#!/usr/bin/python3
"""Module that defines Fish, Bird, and FlyingFish classes."""


class Fish:
    """A class that represents a fish."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message indicating the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A class that represents a bird."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message indicating the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class that inherits from both Fish and Bird."""

    def swim(self):
        """Print a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print a message indicating the flying fish is flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print a message indicating the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
