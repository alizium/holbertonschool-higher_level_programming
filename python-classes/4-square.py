#!/usr/bin/python3
"""Definie une classe Square avec property getter et setter."""


class Square:
    """represente un  square avec size et area methods."""

    def __init__(self, size=0):
        """Initialise le square avec une taille optionnelle."""
        self.size = size  # Trigger le setter pour la validation

    @property
    def size(self):
        """Getter pour la taille."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter la taille avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return la zone courrante du carré."""
        return self.__size ** 2
