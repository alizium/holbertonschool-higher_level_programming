#!/usr/bin/python3

"""Herite de la classe rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definis un carre a partir de la classe rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
