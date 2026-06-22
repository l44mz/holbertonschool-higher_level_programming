#!/usr/bin/python3
"""Module that defines a VerboseList class that extends the list class."""


class VerboseList(list):
    """A list subclass that prints a message on every add or remove."""

    def append(self, item):
        """Add an item to the list and print a notification.

        Args:
            item: The item to add to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and print a notification with the count added.

        Args:
            items: An iterable of items to add to the list.
        """
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and print a notification.

        Args:
            item: The item to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item by index and print a notification.

        Args:
            index (int): The index of the item to pop. Defaults to -1.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
